from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Dict

import numpy as np
import pandas as pd


@dataclass(frozen=True)
class ReportConfig:
    """Configuration for KPI report generation."""

    date_col: str = "date"
    client_col: str = "client_id"
    amount_col: str = "price"
    segment_col: str = "segment_client"
    freq: str = "M"
    top_n: int = 10


def _validate_input(df: pd.DataFrame, cfg: ReportConfig) -> pd.DataFrame:
    required = {cfg.date_col, cfg.client_col, cfg.amount_col}
    missing = required - set(df.columns)
    if missing:
        missing_list = ", ".join(sorted(missing))
        raise ValueError(f"Colonnes manquantes: {missing_list}")

    clean = df.copy()
    clean[cfg.date_col] = pd.to_datetime(clean[cfg.date_col], errors="coerce")
    clean[cfg.amount_col] = pd.to_numeric(clean[cfg.amount_col], errors="coerce")
    clean = clean.dropna(subset=[cfg.date_col, cfg.amount_col, cfg.client_col])
    return clean


def _customer_revenue(df: pd.DataFrame, cfg: ReportConfig) -> pd.DataFrame:
    out = (
        df.groupby(cfg.client_col, as_index=False)[cfg.amount_col]
        .sum()
        .rename(columns={cfg.amount_col: "ca_total"})
        .sort_values("ca_total", ascending=False)
        .reset_index(drop=True)
    )
    return out


def gini_index(values: np.ndarray) -> float:
    """Compute Gini index on non-negative values."""
    arr = np.asarray(values, dtype=float)
    arr = arr[np.isfinite(arr)]
    arr = arr[arr >= 0]

    if arr.size == 0:
        return 0.0

    total = arr.sum()
    if total == 0:
        return 0.0

    arr = np.sort(arr)
    n = arr.size
    cum = np.cumsum(arr)
    gini = (n + 1 - 2 * (cum.sum() / total)) / n
    return float(gini)


def lorenz_curve(values: np.ndarray) -> pd.DataFrame:
    """Return Lorenz points as a DataFrame."""
    arr = np.asarray(values, dtype=float)
    arr = arr[np.isfinite(arr)]
    arr = arr[arr >= 0]

    if arr.size == 0:
        return pd.DataFrame(
            {
                "part_clients": [0.0, 1.0],
                "part_ca": [0.0, 1.0],
            }
        )

    arr = np.sort(arr)
    total = arr.sum()
    if total == 0:
        return pd.DataFrame(
            {
                "part_clients": np.linspace(0, 1, arr.size + 1),
                "part_ca": np.zeros(arr.size + 1),
            }
        )

    cum_ca = np.insert(np.cumsum(arr) / total, 0, 0.0)
    part_clients = np.linspace(0, 1, arr.size + 1)

    return pd.DataFrame({"part_clients": part_clients, "part_ca": cum_ca})


def compute_global_kpis(df: pd.DataFrame, cfg: ReportConfig) -> pd.DataFrame:
    ca_total = float(df[cfg.amount_col].sum())
    nb_transactions = int(len(df))
    nb_clients = int(df[cfg.client_col].nunique())

    panier_moyen = ca_total / nb_transactions if nb_transactions else 0.0
    freq_achat = nb_transactions / nb_clients if nb_clients else 0.0
    ca_moyen_client = ca_total / nb_clients if nb_clients else 0.0

    customer_ca = _customer_revenue(df, cfg)
    gini = gini_index(customer_ca["ca_total"].to_numpy())

    rows = [
        {"kpi": "ca_total", "value": ca_total},
        {"kpi": "nb_transactions", "value": nb_transactions},
        {"kpi": "nb_clients_actifs", "value": nb_clients},
        {"kpi": "panier_moyen", "value": panier_moyen},
        {"kpi": "frequence_achat", "value": freq_achat},
        {"kpi": "ca_moyen_par_client", "value": ca_moyen_client},
        {"kpi": "gini_ca_clients", "value": gini},
    ]

    if cfg.segment_col in df.columns:
        seg = (
            df.groupby(cfg.segment_col, as_index=False)[cfg.amount_col]
            .sum()
            .rename(columns={cfg.amount_col: "ca"})
        )
        seg_total = float(seg["ca"].sum())

        ca_btob = float(seg.loc[seg[cfg.segment_col] == "BtoB", "ca"].sum())
        ca_btoc = float(seg.loc[seg[cfg.segment_col] == "BtoC", "ca"].sum())

        rows.extend(
            [
                {"kpi": "ca_BtoB", "value": ca_btob},
                {"kpi": "ca_BtoC", "value": ca_btoc},
            ]
        )

        for _, item in seg.iterrows():
            share = (float(item["ca"]) / seg_total) if seg_total else 0.0
            rows.append(
                {
                    "kpi": f"part_ca_{item[cfg.segment_col]}",
                    "value": share,
                }
            )

    return pd.DataFrame(rows)


def compute_monthly_kpis(df: pd.DataFrame, cfg: ReportConfig) -> pd.DataFrame:
    monthly = (
        df.set_index(cfg.date_col)
        .resample(cfg.freq)
        .agg(
            ca_total=(cfg.amount_col, "sum"),
            nb_transactions=(cfg.amount_col, "count"),
            nb_clients=(cfg.client_col, "nunique"),
        )
        .reset_index()
    )

    monthly["panier_moyen"] = monthly["ca_total"] / monthly["nb_transactions"].replace(0, np.nan)
    monthly["ca_moyen_client"] = monthly["ca_total"] / monthly["nb_clients"].replace(0, np.nan)
    monthly["croissance_mom"] = monthly["ca_total"].pct_change()
    monthly["mm3_ca"] = monthly["ca_total"].rolling(3, min_periods=1).mean()
    return monthly


def compute_top_clients(df: pd.DataFrame, cfg: ReportConfig) -> pd.DataFrame:
    top = _customer_revenue(df, cfg).head(cfg.top_n).copy()
    total = float(df[cfg.amount_col].sum())
    top["part_ca"] = top["ca_total"] / total if total else 0.0
    top["part_ca_cumulee"] = top["part_ca"].cumsum()
    return top


def compute_data_quality(df: pd.DataFrame, cfg: ReportConfig) -> pd.DataFrame:
    out = pd.DataFrame(
        {
            "metric": [
                "nb_lignes",
                "nb_colonnes",
                "nb_valeurs_manquantes",
                "date_min",
                "date_max",
            ],
            "value": [
                len(df),
                df.shape[1],
                int(df.isna().sum().sum()),
                df[cfg.date_col].min(),
                df[cfg.date_col].max(),
            ],
        }
    )
    return out


def build_kpi_report_tables(df: pd.DataFrame, cfg: ReportConfig | None = None) -> Dict[str, pd.DataFrame]:
    """Build all report tables to enrich an existing export."""
    cfg = cfg or ReportConfig()
    clean = _validate_input(df, cfg)
    customers = _customer_revenue(clean, cfg)

    tables = {
        "summary_kpi": compute_global_kpis(clean, cfg),
        "kpi_mensuels": compute_monthly_kpis(clean, cfg),
        "top_clients": compute_top_clients(clean, cfg),
        "ca_par_client": customers,
        "lorenz": lorenz_curve(customers["ca_total"].to_numpy()),
        "diagnostics_data": compute_data_quality(clean, cfg),
    }

    if cfg.segment_col in clean.columns:
        segment = (
            clean.groupby(cfg.segment_col)
            .agg(
                ca_total=(cfg.amount_col, "sum"),
                nb_transactions=(cfg.amount_col, "count"),
                nb_clients=(cfg.client_col, "nunique"),
            )
            .reset_index()
        )
        tables["segmentation_clients"] = segment

    meta = pd.DataFrame(
        {
            "key": ["generated_at", "freq", "top_n", "rows_source"],
            "value": [
                pd.Timestamp.now().isoformat(),
                cfg.freq,
                cfg.top_n,
                len(clean),
            ],
        }
    )
    tables["meta_export"] = meta

    return tables


def export_kpi_report(
    tables: Dict[str, pd.DataFrame],
    output_path: str | Path,
    include_index: bool = False,
) -> Path:
    """Export report tables to one Excel file (one sheet per table)."""
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)

    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        for sheet, table in tables.items():
            table.to_excel(writer, sheet_name=sheet[:31], index=include_index)

    return output
