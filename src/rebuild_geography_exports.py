import ast
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent.parent
FR_PROCESSED = PROJECT_ROOT / "data" / "processed" / "csv_enrichis" / "fr"
STAR_PROCESSED = PROJECT_ROOT / "data" / "processed" / "pbi_star"

GEO_PATH = FR_PROCESSED / "dim_geographie_fr.csv"

FR_FILES_TO_ENRICH = [
    FR_PROCESSED / "country_region_reference_fr.csv",
    FR_PROCESSED / "dashboard_water_country_year_fr.csv",
    FR_PROCESSED / "priority_snapshot_2016_fr.csv",
    FR_PROCESSED / "priority_snapshot_focus_2016_fr.csv",
    FR_PROCESSED / "water_indicators_long_fr.csv",
]

FACT_PATH = STAR_PROCESSED / "fact_dashboard_star_fr.csv"
DIM_PAYS_PATH = STAR_PROCESSED / "dim_pays_star_fr.csv"

COUNTRY_ALIASES_EN = {
    "China": "China, mainland",
    "Netherlands Antilles (former)": "Netherlands Antilles",
}

COUNTRY_DISPLAY_OVERRIDES_EN = {
    "China, mainland": "Chine",
    "China, Taiwan Province of": "Taiwan",
    "China, Hong Kong SAR": "Hong Kong",
    "China, Macao SAR": "Macao",
}

COUNTRY_GEO_OVERRIDES_EN = {
    "China, Taiwan Province of": {
        "continent": "Asia",
        "sous_region_onu": "Eastern Asia",
    },
    "China, Hong Kong SAR": {
        "continent": "Asia",
        "sous_region_onu": "Eastern Asia",
    },
    "China, Macao SAR": {
        "continent": "Asia",
        "sous_region_onu": "Eastern Asia",
    },
}

CONTINENT_LABEL_OVERRIDES = {
    "America": "Americas",
}


def load_geo_reference() -> pd.DataFrame:
    geo = pd.read_csv(GEO_PATH, sep=";")
    return geo


def normalize_geo_value(value: object) -> object:
    if not isinstance(value, str):
        return value

    stripped = value.strip()
    if not stripped.startswith("["):
        return value

    try:
        parsed = ast.literal_eval(stripped)
    except (SyntaxError, ValueError):
        return value

    if not isinstance(parsed, list) or not parsed:
        return value

    normalized = [item for item in parsed if pd.notna(item)]
    if not normalized:
        return value
    if len(set(normalized)) == 1:
        return normalized[0]
    return normalized[0]


def normalize_continent_value(value: object) -> object:
    normalized = normalize_geo_value(value)
    if isinstance(normalized, str):
        return CONTINENT_LABEL_OVERRIDES.get(normalized, normalized)
    return normalized


def build_geo_record(row: pd.Series) -> dict[str, str]:
    source_name = row["pays_en"]
    record = {
        "iso3": row["iso3"],
        "pays": COUNTRY_DISPLAY_OVERRIDES_EN.get(source_name, row["pays_fr"]),
        "region": row["region_oms"],
        "continent": normalize_continent_value(row["continent"]),
        "sous_region_onu": normalize_geo_value(row["sous_region_onu"]),
        "pays_source_en": source_name,
    }
    record.update(COUNTRY_GEO_OVERRIDES_EN.get(source_name, {}))
    return record


def build_country_name_maps(geo: pd.DataFrame) -> tuple[dict[str, str], dict[str, dict[str, str]]]:
    english_lookup = {
        row["pays_en"]: build_geo_record(row)
        for _, row in geo.iterrows()
    }
    french_to_english = {
        row["pays_fr"]: row["pays_en"] for _, row in geo.iterrows()
    }
    return french_to_english, english_lookup


def resolve_source_country_name(country_name: str, french_to_english: dict[str, str]) -> str:
    if pd.isna(country_name):
        return country_name
    if country_name in COUNTRY_ALIASES_EN:
        return COUNTRY_ALIASES_EN[country_name]
    if country_name in french_to_english:
        return french_to_english[country_name]
    return country_name


def enrich_country_frame(df: pd.DataFrame, geo: pd.DataFrame) -> pd.DataFrame:
    french_to_english, english_lookup = build_country_name_maps(geo)

    working = df.copy()
    if "pays_source_en" in working.columns:
        working["pays_source_en"] = working["pays_source_en"].replace(COUNTRY_ALIASES_EN)
    else:
        working["pays_source_en"] = working["pays"].map(
            lambda country: resolve_source_country_name(country, french_to_english)
        )

    geo_columns = ["iso3", "continent", "sous_region_onu"]
    for column in geo_columns:
        if column in working.columns:
            working = working.drop(columns=[column])

    mapped = working["pays_source_en"].map(english_lookup)
    if mapped.isna().any():
        unmatched = sorted(working.loc[mapped.isna(), "pays_source_en"].dropna().unique())
        raise ValueError(f"Pays sans correspondance geographique: {unmatched}")

    mapped_df = pd.DataFrame(mapped.tolist(), index=working.index)
    for column in mapped_df.columns:
        working[column] = mapped_df[column]

    return working


def reorder_columns(df: pd.DataFrame, preferred_columns: list[str]) -> pd.DataFrame:
    existing_preferred = [column for column in preferred_columns if column in df.columns]
    other_columns = [column for column in df.columns if column not in existing_preferred]
    return df[existing_preferred + other_columns]


def normalize_integer_population_columns(df: pd.DataFrame) -> pd.DataFrame:
    working = df.copy()
    for column in ["population_totale", "population_rurale"]:
        if column in working.columns:
            working[column] = pd.to_numeric(working[column], errors="coerce").round().astype("Int64")
    return working


def rebuild_fr_exports() -> None:
    geo = load_geo_reference()

    for path in FR_FILES_TO_ENRICH:
        df = pd.read_csv(path, sep=";")
        enriched = enrich_country_frame(df, geo)
        enriched = normalize_integer_population_columns(enriched)

        if path.name == "country_region_reference_fr.csv":
            enriched = enriched[["pays", "region", "iso3", "continent", "sous_region_onu", "pays_source_en"]]
        else:
            enriched = reorder_columns(
                enriched,
                [
                    "pays",
                    "iso3",
                    "region",
                    "continent",
                    "sous_region_onu",
                    "annee",
                ],
            )

        enriched.to_csv(path, sep=";", index=False, encoding="utf-8")
        print(f"Updated {path.name}: {len(enriched):,} rows")


def rebuild_star_exports() -> None:
    geo = load_geo_reference()

    fact = pd.read_csv(FACT_PATH, sep=";")
    fact = fact.drop(columns=["cle_pays"], errors="ignore")
    enriched_fact = enrich_country_frame(fact, geo)
    enriched_fact = normalize_integer_population_columns(enriched_fact)

    dim_pays = (
        enriched_fact[["iso3", "pays", "region", "continent", "sous_region_onu", "pays_source_en"]]
        .drop_duplicates()
        .sort_values(["continent", "sous_region_onu", "pays"], na_position="last")
        .reset_index(drop=True)
    )
    dim_pays.insert(0, "cle_pays", dim_pays.index + 1)

    enriched_fact = enriched_fact.merge(
        dim_pays,
        on=["iso3", "pays", "region", "continent", "sous_region_onu", "pays_source_en"],
        how="left",
        validate="many_to_one",
    )

    dim_pays = reorder_columns(
        dim_pays,
        ["cle_pays", "iso3", "pays", "region", "continent", "sous_region_onu", "pays_source_en"],
    )
    dim_pays.to_csv(DIM_PAYS_PATH, sep=";", index=False, encoding="utf-8")

    enriched_fact = reorder_columns(
        enriched_fact,
        [
            "cle_pays",
            "cle_annee",
            "cle_action",
            "iso3",
            "pays",
            "region",
            "continent",
            "sous_region_onu",
            "annee",
        ],
    )
    enriched_fact.to_csv(FACT_PATH, sep=";", index=False, encoding="utf-8")

    print(f"Updated {DIM_PAYS_PATH.name}: {len(dim_pays):,} rows")
    print(f"Updated {FACT_PATH.name}: {len(enriched_fact):,} rows")


if __name__ == "__main__":
    rebuild_fr_exports()
    rebuild_star_exports()