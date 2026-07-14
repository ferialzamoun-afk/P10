"""Shared French schema helpers for notebooks and pipeline glue code."""

from __future__ import annotations

from pathlib import Path
from typing import Dict


SCHEMAS_SOURCES_FR: Dict[str, Dict[str, str]] = {
    "population": {
        "Country": "pays",
        "Granularity": "granularite",
        "Year": "annee",
        "Population": "population",
    },
    "zone": {
        "REGION (DISPLAY)": "region",
        "COUNTRY (DISPLAY)": "pays",
    },
    "stabilite_politique": {
        "Country": "pays",
        "Year": "annee",
        "Political_Stability": "stabilite_politique",
        "Granularity": "granularite",
    },
    "mortalite_eau": {
        "Year": "annee",
        "Country": "pays",
        "Granularity": "granularite",
        "Mortality rate attributed to exposure to unsafe WASH services": "mortalite_wash_services_non_surs",
        "WASH deaths": "deces_wash",
    },
    "services_eau": {
        "Year": "annee",
        "Country": "pays",
        "Granularity": "granularite",
        "Population using at least basic drinking-water services (%)": "acces_eau_potable_base_pct",
        "Population using safely managed drinking-water services (%)": "acces_eau_potable_gere_securise_pct",
    },
}


COLONNES_NOTEBOOK_FR: Dict[str, str] = {
    "Country": "Pays",
    "COUNTRY (DISPLAY)": "Pays",
    "country": "pays",
    "country_clean": "pays_normalise",
    "country_raw": "pays_source",
    "country_source": "pays_source",
    "Year": "Année",
    "year": "annee",
    "Granularity": "Granularité",
    "granularity": "granularite",
    "Population": "Population",
    "population": "population",
    "Political_Stability": "Stabilité_politique",
    "stabilite_politique": "stabilite_politique",
    "REGION (DISPLAY)": "Région",
    "region": "region",
    "value": "valeur",
    "indicator": "indicateur",
    "unit": "unite",
    "source": "source",
    "scope_note": "note_portee",
    "rows": "lignes",
    "non_null_values": "valeurs_non_nulles",
    "countries": "nb_pays",
    "years": "nb_annees",
    "missing_regions": "regions_manquantes",
    "countries_in_latest_year": "pays_derniere_annee",
    "population_total_people": "population_totale",
    "population_rural_people": "population_rurale",
    "basic_drinking_water_pct": "acces_eau_potable_pct",
    "safely_managed_drinking_water_pct": "service_eau_gere_securise_pct",
    "wash_mortality_rate_per_100k": "mortalite_wash_pour_100k",
    "wash_deaths": "deces_wash",
    "rural_share_pct": "part_rurale_pct",
    "basic_minus_safe_gap_pct": "ecart_basique_vs_gere_securise_pct",
    "risk_low_basic": "risque_faible_acces_basique",
    "risk_low_safe": "risque_faible_acces_gere_securise",
    "risk_high_gap": "risque_ecart_qualite_eleve",
    "risk_high_mortality": "risque_mortalite_elevee",
    "risk_low_stability": "risque_faible_stabilite",
    "risk_high_rurality": "risque_ruralite_elevee",
    "score_creation_services": "score_creation_services",
    "score_modernisation_services": "score_modernisation_services",
    "score_gouvernance": "score_gouvernance",
    "action_prioritaire": "action_prioritaire",
    "components_sum": "somme_composantes",
    "delta_china_minus_components": "ecart_chine_moins_composantes",
    "Mortality rate attributed to exposure to unsafe WASH services": "Mortalité attribuée à une exposition à des services WASH non sûrs",
    "mortalite_wash_services_non_surs": "mortalite_wash_services_non_surs",
    "WASH deaths": "Décès_WASH",
    "deces_wash": "deces_wash",
    "Population using at least basic drinking-water services (%)": "Population utilisant au moins un service d'eau potable de base (%)",
    "acces_eau_potable_base_pct": "acces_eau_potable_base_pct",
    "Population using safely managed drinking-water services (%)": "Population utilisant un service d'eau potable géré en toute sécurité (%)",
    "acces_eau_potable_gere_securise_pct": "acces_eau_potable_gere_securise_pct",
}


VALEURS_NOTEBOOK_FR: Dict[str, Dict[str, str]] = {
    "Granularity": {
        "Total": "Total",
        "Rural": "Rural",
        "Urban": "Urbain",
        "Female": "Femmes",
        "Male": "Hommes",
    },
    "Granularité": {
        "Total": "Total",
        "Rural": "Rural",
        "Urban": "Urbain",
        "Female": "Femmes",
        "Male": "Hommes",
    },
    "granularite": {
        "Total": "Total",
        "Rural": "Rural",
        "Urban": "Urbain",
        "Female": "Femmes",
        "Male": "Hommes",
    },
    "indicator": {
        "population_people": "population_habitants",
        "political_stability": "stabilite_politique",
        "basic_drinking_water_pct": "acces_eau_potable_pct",
        "safely_managed_drinking_water_pct": "service_eau_gere_securise_pct",
        "wash_mortality_rate_per_100k": "mortalite_wash_pour_100k",
        "wash_deaths": "deces_wash",
    },
    "indicateur": {
        "population_people": "population_habitants",
        "political_stability": "stabilite_politique",
        "basic_drinking_water_pct": "acces_eau_potable_pct",
        "safely_managed_drinking_water_pct": "service_eau_gere_securise_pct",
        "wash_mortality_rate_per_100k": "mortalite_wash_pour_100k",
        "wash_deaths": "deces_wash",
    },
}


EXPORT_PBI_FR: Dict[str, str] = {
    "country": "pays",
    "region": "region",
    "year": "annee",
    "population_total_people": "population_totale",
    "population_rural_people": "population_rurale",
    "political_stability": "stabilite_politique",
    "basic_drinking_water_pct": "acces_eau_potable_pct",
    "safely_managed_drinking_water_pct": "service_safely_managed_pct",
    "wash_mortality_rate_per_100k": "mortalite_wash_pour_100k",
    "wash_deaths": "deces_wash",
}


COLONNES_ANALYSE_FR: Dict[str, str] = {
    "country": "Pays",
    "country_clean": "Pays",
    "region": "Région",
    "year": "Année",
    "population_total_people": "Population totale",
    "population_rural_people": "Population rurale",
    "population_total_millions": "Population (millions)",
    "urban_share_pct": "Part urbaine (%)",
    "rural_share_pct": "Part rurale (%)",
    "political_stability": "Stabilité politique",
    "basic_drinking_water_pct": "Accès à l'eau potable (%)",
    "safely_managed_drinking_water_pct": "Service d'eau géré en toute sécurité (%)",
    "service_quality_gap_pct": "Écart de qualité de service",
    "basic_minus_safe_gap_pct": "Écart service basique - service géré en toute sécurité",
    "wash_mortality_rate_per_100k": "Mortalité WASH pour 100k",
    "wash_deaths": "Décès WASH",
    "government_effectiveness_proxy": "Proxy efficacité politique eau",
    "gov_effectiveness_score": "Score d'effectivité gouvernementale",
    "score_creation_services": "Score création de services",
    "score_modernisation_services": "Score modernisation des services",
    "score_gouvernance": "Score gouvernance",
    "action_prioritaire": "Action prioritaire",
    "domain": "Domaine",
    "visual": "Visuel",
    "x": "Axe X",
    "y": "Axe Y",
    "usage": "Usage métier",
    "constraint": "Contrainte",
    "implementation": "Implémentation",
    "filter_type": "Type de filtre",
    "parameter": "Paramètre",
    "value": "Valeur",
}


VISUELS_NOTEBOOK_3_FR: Dict[str, Dict[str, object]] = {
    "courbe_temporelle": {
        "labels": {
            "year": "Année",
            "value": "Valeur moyenne",
            "region": "Région",
            "metric": "Indicateur",
        },
        "title": "Évolution régionale moyenne de l'accès à l'eau potable et de la stabilité politique",
        "facet_labels": {
            "avg_basic_drinking_water_pct": "Accès à l'eau potable (%)",
            "avg_political_stability": "Stabilité politique moyenne",
        },
        "legend_title": "Région",
    },
    "creation_services": {
        "title": "Domaine 1 - Création de services : accès à l'eau vs urbanisation",
        "legend_title": "Région",
    },
    "structure_population": {
        "labels": {
            "country": "Pays",
            "share_pct": "Part de population (%)",
            "population_split": "Composition",
        },
        "split_labels": {
            "urban_share_pct": "Part urbaine",
            "rural_share_pct": "Part rurale",
        },
        "title": "Domaine 1 - Structure urbaine et rurale des pays prioritaires",
        "legend_title": "Composition",
    },
    "modernisation_services": {
        "labels": {
            "coverage_pct": "Couverture (%)",
            "service_level": "Niveau de service",
        },
        "service_level_labels": {
            "basic_drinking_water_pct": "Service de base",
            "safely_managed_drinking_water_pct": "Service géré en toute sécurité",
        },
        "title": "Domaine 2 - Comparaison entre service de base et service géré en toute sécurité",
        "legend_title": "Niveau de service",
    },
    "gouvernance": {
        "title": "Domaine 3 - Gouvernance : efficacité observable vs stabilité politique",
        "legend_title": "Région",
    },
    "carte_gouvernance": {
        "title": "Carte mondiale du score de gouvernance - Snapshot 2016",
    },
}


MARTS_ANALYTIQUES_EN_FR: Dict[str, Dict[str, str]] = {
    "dashboard_water_country_year": {
        "country": "pays",
        "region": "region",
        "year": "annee",
        "population_total_people": "population_totale",
        "population_rural_people": "population_rurale",
        "political_stability": "stabilite_politique",
        "basic_drinking_water_pct": "acces_eau_potable_pct",
        "safely_managed_drinking_water_pct": "service_safely_managed_pct",
        "wash_mortality_rate_per_100k": "mortalite_wash_pour_100k",
        "wash_deaths": "deces_wash",
        "rural_share_pct": "part_rurale_pct",
        "basic_minus_safe_gap_pct": "ecart_basique_safely_managed_pct",
        "risk_low_basic": "risque_faible_acces_basique",
        "risk_low_safe": "risque_faible_acces_safely_managed",
        "risk_high_gap": "risque_ecart_qualite_eleve",
        "risk_high_mortality": "risque_mortalite_elevee",
        "risk_low_stability": "risque_faible_stabilite",
        "risk_high_rurality": "risque_ruralite_elevee",
        "gov_effectiveness_score": "score_effectivite_gouvernementale",
        "score_creation_services": "score_creation_services",
        "score_modernisation_services": "score_modernisation_services",
        "score_gouvernance": "score_gouvernance",
        "action_prioritaire": "action_prioritaire",
    },
    "priority_snapshot_2016": {
        "country": "pays",
        "region": "region",
        "year": "annee",
        "population_total_people": "population_totale",
        "population_rural_people": "population_rurale",
        "political_stability": "stabilite_politique",
        "basic_drinking_water_pct": "acces_eau_potable_pct",
        "safely_managed_drinking_water_pct": "service_safely_managed_pct",
        "wash_mortality_rate_per_100k": "mortalite_wash_pour_100k",
        "wash_deaths": "deces_wash",
        "rural_share_pct": "part_rurale_pct",
        "basic_minus_safe_gap_pct": "ecart_basique_safely_managed_pct",
        "risk_low_basic": "risque_faible_acces_basique",
        "risk_low_safe": "risque_faible_acces_safely_managed",
        "risk_high_gap": "risque_ecart_qualite_eleve",
        "risk_high_mortality": "risque_mortalite_elevee",
        "risk_low_stability": "risque_faible_stabilite",
        "risk_high_rurality": "risque_ruralite_elevee",
        "gov_effectiveness_score": "score_effectivite_gouvernementale",
        "score_creation_services": "score_creation_services",
        "score_modernisation_services": "score_modernisation_services",
        "score_gouvernance": "score_gouvernance",
        "action_prioritaire": "action_prioritaire",
    },
    "priority_snapshot_focus_2016": {
        "country": "pays",
        "region": "region",
        "year": "annee",
        "population_total_people": "population_totale",
        "population_rural_people": "population_rurale",
        "political_stability": "stabilite_politique",
        "basic_drinking_water_pct": "acces_eau_potable_pct",
        "safely_managed_drinking_water_pct": "service_safely_managed_pct",
        "wash_mortality_rate_per_100k": "mortalite_wash_pour_100k",
        "wash_deaths": "deces_wash",
        "rural_share_pct": "part_rurale_pct",
        "basic_minus_safe_gap_pct": "ecart_basique_safely_managed_pct",
        "risk_low_basic": "risque_faible_acces_basique",
        "risk_low_safe": "risque_faible_acces_safely_managed",
        "risk_high_gap": "risque_ecart_qualite_eleve",
        "risk_high_mortality": "risque_mortalite_elevee",
        "risk_low_stability": "risque_faible_stabilite",
        "risk_high_rurality": "risque_ruralite_elevee",
        "gov_effectiveness_score": "score_effectivite_gouvernementale",
        "score_creation_services": "score_creation_services",
        "score_modernisation_services": "score_modernisation_services",
        "score_gouvernance": "score_gouvernance",
        "action_prioritaire": "action_prioritaire",
    },
}


def normaliser_table_source(df, nom_table):
    mapping = SCHEMAS_SOURCES_FR.get(nom_table, {})
    return df.rename(columns=mapping).copy()


def vue_notebook_fr(df):
    vue = df.copy()
    vue = vue.rename(columns=COLONNES_NOTEBOOK_FR)
    for colonne, mapping in VALEURS_NOTEBOOK_FR.items():
        if colonne in vue.columns:
            vue[colonne] = vue[colonne].replace(mapping)
    return vue


def construire_libelles_analyse_fr(extra_labels: Dict[str, str] | None = None) -> Dict[str, str]:
    labels = {**COLONNES_NOTEBOOK_FR, **COLONNES_ANALYSE_FR}
    if extra_labels:
        labels.update(extra_labels)
    return labels


def construire_visuels_notebook_3_fr() -> Dict[str, Dict[str, object]]:
    return VISUELS_NOTEBOOK_3_FR.copy()


def construire_marts_analytiques_en_fr() -> Dict[str, Dict[str, str]]:
    return {nom_mart: mapping.copy() for nom_mart, mapping in MARTS_ANALYTIQUES_EN_FR.items()}


def resolve_project_paths(base_path: Path | None = None) -> Dict[str, Path]:
    cwd = (base_path or Path.cwd()).resolve()
    project_root = cwd if (cwd / "data").exists() else cwd.parent
    processed_data_path = project_root / "data" / "processed"
    return {
        "PROJECT_ROOT": project_root,
        "RAW_DATA_PATH": project_root / "data" / "raw",
        "PROCESSED_DATA_PATH": processed_data_path,
        "CSV_EN_PATH": processed_data_path / "csv_enrichis" / "en",
        "CSV_FR_PATH": processed_data_path / "csv_enrichis" / "fr",
        "PBI_STAR_PATH": processed_data_path / "pbi_star",
    }