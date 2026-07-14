from __future__ import annotations

from pathlib import Path
from typing import Dict, Tuple

import pandas as pd


CATEG_LABELS = {0: "Categorie 0", 1: "Categorie 1", 2: "Categorie 2"}


def default_data_dir() -> Path:
	"""Return the default data directory from this module location."""
	return Path(__file__).resolve().parents[1] / "data"


def load_csv_tables(data_dir: str | Path | None = None) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
	"""Load raw CSV tables (transactions, customers, products)."""
	root = Path(data_dir) if data_dir else default_data_dir()

	transactions = pd.read_csv(root / "Transactions.csv", sep=";", low_memory=False)
	customers = pd.read_csv(root / "customers.csv", sep=";")
	products = pd.read_csv(root / "products.csv", sep=";")

	return transactions, customers, products


def build_enriched_transactions(
	transactions: pd.DataFrame,
	customers: pd.DataFrame,
	products: pd.DataFrame,
	segment_threshold: float = 100000,
) -> pd.DataFrame:
	"""Apply core cleaning + joins used by business analyses."""
	tx = transactions.copy()

	tx = tx.dropna(how="all")
	tx = tx.drop(columns=["birth", "sex"], errors="ignore")
	tx["date"] = pd.to_datetime(tx["date"], errors="coerce")

	df = tx.merge(products, on="id_prod", how="left")
	df = df.merge(customers, on="client_id", how="left")

	df["date"] = pd.to_datetime(df["date"], errors="coerce")
	if "birth" in df.columns:
		df["birth"] = pd.to_numeric(df["birth"], errors="coerce")
		df["age"] = df["date"].dt.year - df["birth"]

	df["mois"] = df["date"].dt.to_period("M")
	df["annee"] = df["date"].dt.year

	if "categ" in df.columns:
		df["categ_label"] = df["categ"].map(CATEG_LABELS)

	if "price" in df.columns:
		df["price"] = pd.to_numeric(df["price"], errors="coerce")

	if {"client_id", "price"}.issubset(df.columns):
		client_revenue = (
			df.groupby("client_id", as_index=False)["price"]
			.sum()
			.rename(columns={"price": "ca_total_client"})
		)
		client_revenue["segment_client"] = client_revenue["ca_total_client"].apply(
			lambda value: "BtoB" if value > segment_threshold else "BtoC"
		)
		df = df.merge(client_revenue[["client_id", "ca_total_client", "segment_client"]], on="client_id", how="left")
		df["Segment_Client"] = df["segment_client"]

	return df


def load_transactions_enriched(
	data_dir: str | Path | None = None,
	segment_threshold: float = 100000,
) -> pd.DataFrame:
	"""One-call loader used by analysis modules and notebooks."""
	transactions, customers, products = load_csv_tables(data_dir=data_dir)
	return build_enriched_transactions(
		transactions,
		customers,
		products,
		segment_threshold=segment_threshold,
	)


def get_data_overview(df: pd.DataFrame) -> Dict[str, object]:
	"""Quick metadata helper for logs/tests."""
	return {
		"rows": int(len(df)),
		"columns": int(df.shape[1]),
		"date_min": df["date"].min() if "date" in df.columns else None,
		"date_max": df["date"].max() if "date" in df.columns else None,
		"na_total": int(df.isna().sum().sum()),
	}
