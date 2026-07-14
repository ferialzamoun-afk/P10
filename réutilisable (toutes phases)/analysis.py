from __future__ import annotations

from pathlib import Path
from typing import Dict

import pandas as pd

try:
	from .data_loader import load_transactions_enriched
except ImportError:
	from data_loader import load_transactions_enriched


def compute_kpis_globaux(df: pd.DataFrame) -> pd.DataFrame:
	"""Compute core global KPIs for business reporting."""
	ca_total = float(df["price"].sum())
	nb_transactions = int(len(df))
	nb_clients = int(df["client_id"].nunique())

	panier_moyen = ca_total / nb_transactions if nb_transactions else 0.0
	frequence_achat = nb_transactions / nb_clients if nb_clients else 0.0
	ca_moyen_par_client = ca_total / nb_clients if nb_clients else 0.0

	rows = [
		{"kpi": "ca_total", "value": ca_total},
		{"kpi": "nb_transactions", "value": nb_transactions},
		{"kpi": "nb_clients_actifs", "value": nb_clients},
		{"kpi": "panier_moyen", "value": panier_moyen},
		{"kpi": "frequence_achat", "value": frequence_achat},
		{"kpi": "ca_moyen_par_client", "value": ca_moyen_par_client},
	]
	return pd.DataFrame(rows)


def compute_ca_mensuel(df: pd.DataFrame) -> pd.DataFrame:
	out = df.groupby("mois", as_index=False)["price"].sum().rename(columns={"price": "ca"})
	out["mois_dt"] = out["mois"].dt.to_timestamp()
	out["mm3"] = out["ca"].rolling(window=3, min_periods=1).mean()
	return out


def compute_ca_par_categorie(df: pd.DataFrame) -> pd.DataFrame:
	group_col = "categ_label" if "categ_label" in df.columns else "categ"
	out = df.groupby(group_col, as_index=False)["price"].sum().rename(columns={"price": "ca"})
	total = float(out["ca"].sum())
	out["pct"] = (out["ca"] / total * 100).round(1) if total else 0.0
	return out


def compute_clients_actifs_mensuel(df: pd.DataFrame) -> pd.DataFrame:
	out = df.groupby("mois", as_index=False)["client_id"].nunique().rename(columns={"client_id": "nb_clients"})
	out["mois_dt"] = out["mois"].dt.to_timestamp()
	return out


def compute_volume_transactions_mensuel(df: pd.DataFrame) -> pd.DataFrame:
	transactions = df.groupby("mois").size().reset_index(name="nb_transactions")
	produits = df.groupby("mois")["id_prod"].count().reset_index(name="nb_produits")
	out = transactions.merge(produits, on="mois", how="left")
	out["mois_dt"] = out["mois"].dt.to_timestamp()
	return out


def compute_tops_flops(df: pd.DataFrame, n: int = 10) -> Dict[str, pd.DataFrame]:
	ca_produit = (
		df.groupby("id_prod", as_index=False)["price"]
		.sum()
		.rename(columns={"price": "ca"})
		.sort_values("ca", ascending=False)
		.reset_index(drop=True)
	)
	return {
		"ca_produit": ca_produit,
		"top": ca_produit.head(n).copy(),
		"flop": ca_produit.tail(n).copy(),
	}


def run_annabelle_business_analysis(data_dir: str | None = None, top_n: int = 10) -> Dict[str, pd.DataFrame]:
	"""Single entrypoint to reproduce and reuse Annabelle's business analysis."""
	df = load_transactions_enriched(data_dir=data_dir)

	tops_flops = compute_tops_flops(df, n=top_n)

	outputs: Dict[str, pd.DataFrame] = {
		"transactions_enrichies": df,
		"kpis_globaux": compute_kpis_globaux(df),
		"ca_mensuel": compute_ca_mensuel(df),
		"ca_par_categorie": compute_ca_par_categorie(df),
		"clients_actifs_mensuel": compute_clients_actifs_mensuel(df),
		"volume_transactions_mensuel": compute_volume_transactions_mensuel(df),
		"ca_produit": tops_flops["ca_produit"],
		"top_produits": tops_flops["top"],
		"flop_produits": tops_flops["flop"],
	}
	return outputs


def _prepare_table_for_export(table: pd.DataFrame) -> pd.DataFrame:
	"""Return a copy safe for CSV/Excel export."""
	export_table = table.copy()

	# Excel/CSV do not always handle pandas Period cleanly.
	for col in export_table.columns:
		if pd.api.types.is_period_dtype(export_table[col]):
			export_table[col] = export_table[col].astype(str)

	return export_table


def export_analysis_tables(
	tables: Dict[str, pd.DataFrame],
	output_dir: str | Path = "../reports/exports",
	file_stem: str = "annabelle_business_analysis",
	include_csv: bool = True,
	include_excel: bool = True,
) -> Dict[str, Path]:
	"""Export analysis outputs to Excel (multi-sheet) and optional CSV files."""
	root = Path(output_dir)
	root.mkdir(parents=True, exist_ok=True)

	exported: Dict[str, Path] = {}

	if include_excel:
		excel_path = root / f"{file_stem}.xlsx"
		with pd.ExcelWriter(excel_path, engine="openpyxl") as writer:
			for name, table in tables.items():
				clean_table = _prepare_table_for_export(table)
				clean_table.to_excel(writer, sheet_name=name[:31], index=False)
		exported["excel"] = excel_path

	if include_csv:
		csv_dir = root / f"{file_stem}_csv"
		csv_dir.mkdir(parents=True, exist_ok=True)
		for name, table in tables.items():
			clean_table = _prepare_table_for_export(table)
			csv_path = csv_dir / f"{name}.csv"
			clean_table.to_csv(csv_path, index=False)
		exported["csv_dir"] = csv_dir

	return exported


def run_annabelle_pipeline(
	data_dir: str | None = None,
	top_n: int = 10,
	export_dir: str | Path = "../reports/exports",
	file_stem: str = "annabelle_business_analysis",
	include_csv: bool = True,
	include_excel: bool = True,
) -> Dict[str, object]:
	"""Run analysis + exports in one call for notebooks and scripts."""
	tables = run_annabelle_business_analysis(data_dir=data_dir, top_n=top_n)
	export_paths = export_analysis_tables(
		tables=tables,
		output_dir=export_dir,
		file_stem=file_stem,
		include_csv=include_csv,
		include_excel=include_excel,
	)

	return {
		"tables": tables,
		"exports": export_paths,
	}
