from __future__ import annotations

from pathlib import Path
from typing import Iterable

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.ticker import FuncFormatter


def _save_if_needed(fig: plt.Figure, save_path: str | Path | None, dpi: int = 300) -> None:
	if save_path is None:
		return
	out = Path(save_path)
	out.parent.mkdir(parents=True, exist_ok=True)
	fig.savefig(out, dpi=dpi, bbox_inches="tight", facecolor="white")


def plot_line(
	df: pd.DataFrame,
	x: str,
	y: str,
	title: str,
	xlabel: str | None = None,
	ylabel: str | None = None,
	color: str = "steelblue",
	marker: str | None = None,
	figsize: tuple[int, int] = (12, 5),
	rotation: int = 45,
	grid_alpha: float = 0.3,
	save_path: str | Path | None = None,
) -> tuple[plt.Figure, plt.Axes]:
	fig, ax = plt.subplots(figsize=figsize)
	ax.plot(df[x], df[y], color=color, marker=marker)
	ax.set_title(title)
	ax.set_xlabel(xlabel or x)
	ax.set_ylabel(ylabel or y)
	ax.grid(True, alpha=grid_alpha)
	ax.tick_params(axis="x", rotation=rotation)
	plt.tight_layout()
	_save_if_needed(fig, save_path)
	return fig, ax


def plot_ca_mensuel(
	ca_mensuel: pd.DataFrame,
	x_col: str = "mois_dt",
	ca_col: str = "ca",
	mm_col: str = "mm3",
	title: str = "Evolution du chiffre d'affaires mensuel",
	figsize: tuple[int, int] = (12, 5),
	save_path: str | Path | None = None,
) -> tuple[plt.Figure, plt.Axes]:
	fig, ax = plt.subplots(figsize=figsize)
	ax.plot(ca_mensuel[x_col], ca_mensuel[ca_col], color="steelblue", linewidth=2, label="CA mensuel")
	if mm_col in ca_mensuel.columns:
		ax.plot(ca_mensuel[x_col], ca_mensuel[mm_col], color="orange", linewidth=2, linestyle="--", label="Moyenne mobile")
	ax.set_title(title)
	ax.set_xlabel("Mois")
	ax.set_ylabel("CA (EUR)")
	ax.legend()
	ax.tick_params(axis="x", rotation=45)
	ax.grid(True, alpha=0.3)
	plt.tight_layout()
	_save_if_needed(fig, save_path)
	return fig, ax


def plot_bar(
	df: pd.DataFrame,
	x: str,
	y: str,
	title: str,
	xlabel: str | None = None,
	ylabel: str | None = None,
	color: str | Iterable[str] = "steelblue",
	annotate: bool = False,
	figsize: tuple[int, int] = (10, 5),
	rotation: int = 0,
	save_path: str | Path | None = None,
) -> tuple[plt.Figure, plt.Axes]:
	fig, ax = plt.subplots(figsize=figsize)
	bars = ax.bar(df[x], df[y], color=color)
	ax.set_title(title)
	ax.set_xlabel(xlabel or x)
	ax.set_ylabel(ylabel or y)
	ax.tick_params(axis="x", rotation=rotation)
	ax.grid(True, axis="y", alpha=0.3)

	if annotate:
		for bar in bars:
			h = bar.get_height()
			ax.text(bar.get_x() + bar.get_width() / 2, h, f"{h:,.0f}", ha="center", va="bottom", fontsize=9)

	plt.tight_layout()
	_save_if_needed(fig, save_path)
	return fig, ax


def plot_top_flop(
	top_df: pd.DataFrame,
	flop_df: pd.DataFrame,
	label_col: str,
	value_col: str,
	figsize: tuple[int, int] = (16, 6),
	save_path: str | Path | None = None,
) -> tuple[plt.Figure, np.ndarray]:
	fig, axes = plt.subplots(1, 2, figsize=figsize)

	axes[0].barh(top_df[label_col], top_df[value_col], color="steelblue")
	axes[0].set_title("Top")
	axes[0].set_xlabel("CA (EUR)")
	axes[0].invert_yaxis()

	axes[1].barh(flop_df[label_col], flop_df[value_col], color="tomato")
	axes[1].set_title("Flop")
	axes[1].set_xlabel("CA (EUR)")
	axes[1].invert_yaxis()

	plt.tight_layout()
	_save_if_needed(fig, save_path)
	return fig, axes


def plot_pie_segments(
	values: Iterable[float],
	labels: Iterable[str],
	title: str = "Repartition",
	colors: Iterable[str] | None = None,
	figsize: tuple[int, int] = (7, 7),
	save_path: str | Path | None = None,
) -> tuple[plt.Figure, plt.Axes]:
	fig, ax = plt.subplots(figsize=figsize)
	ax.pie(values, labels=labels, autopct="%1.1f%%", startangle=90, colors=colors)
	ax.set_title(title)
	plt.tight_layout()
	_save_if_needed(fig, save_path)
	return fig, ax


def compute_lorenz_points(values: np.ndarray | pd.Series) -> pd.DataFrame:
	arr = np.asarray(values, dtype=float)
	arr = arr[np.isfinite(arr)]
	arr = arr[arr >= 0]

	if arr.size == 0:
		return pd.DataFrame({"part_clients": [0.0, 1.0], "part_ca": [0.0, 1.0]})

	arr = np.sort(arr)
	total = arr.sum()
	if total == 0:
		return pd.DataFrame({"part_clients": [0.0, 1.0], "part_ca": [0.0, 0.0]})

	part_clients = np.linspace(0, 1, arr.size + 1)
	part_ca = np.insert(np.cumsum(arr) / total, 0, 0.0)
	return pd.DataFrame({"part_clients": part_clients, "part_ca": part_ca})


def plot_lorenz(
	values: np.ndarray | pd.Series,
	title: str = "Courbe de Lorenz du chiffre d'affaires",
	figsize: tuple[int, int] = (8, 6),
	save_path: str | Path | None = None,
) -> tuple[plt.Figure, plt.Axes, pd.DataFrame]:
	lorenz = compute_lorenz_points(values)

	fig, ax = plt.subplots(figsize=figsize)
	ax.plot(lorenz["part_clients"], lorenz["part_ca"], color="steelblue", label="Courbe de Lorenz")
	ax.plot([0, 1], [0, 1], linestyle="--", color="gray", label="Egalite parfaite")
	ax.set_xlabel("Proportion cumulee de clients")
	ax.set_ylabel("Proportion cumulee du CA")
	ax.set_title(title)
	ax.grid(True, alpha=0.3)
	ax.legend()
	plt.tight_layout()
	_save_if_needed(fig, save_path)
	return fig, ax, lorenz


def _require_columns(df: pd.DataFrame, required: list[str]) -> None:
	if df is None:
		raise ValueError(
			"Le DataFrame fourni est None. Verifiez que vous ne faites pas `df = inspecter_dataframe(...)` "
			"car cette fonction affiche un rapport mais ne retourne pas le DataFrame."
		)
	missing = [c for c in required if c not in df.columns]
	if missing:
		raise ValueError(f"Colonnes manquantes pour la visualisation: {missing}")


def generate_annabelle_figures(
	df: pd.DataFrame,
	output_dir: str | Path = "../reports/figures",
	selected: list[str] | None = None,
	top_n: int = 10,
	segment_threshold: float = 100000,
	include_decomposition: bool = True,
) -> dict[str, plt.Figure]:
	"""
	Generate and export all reusable Annabelle figures from an enriched DataFrame.

	Parameters
	----------
	df : pd.DataFrame
		Enriched transactions DataFrame.
	output_dir : str | Path
		Folder where PNG files are saved.
	selected : list[str] | None
		Optional list of figure keys to generate.
	top_n : int
		Top/Flop size for product rankings.
	segment_threshold : float
		Threshold to split BtoB and BtoC on client revenue.
	include_decomposition : bool
		Whether to include seasonal decomposition figure.

	Returns
	-------
	dict[str, matplotlib.figure.Figure]
		Generated figures indexed by keys.
	"""
	_require_columns(df, ["date", "price", "client_id", "id_prod"])

	work = df.copy()
	work["date"] = pd.to_datetime(work["date"], errors="coerce")
	work["price"] = pd.to_numeric(work["price"], errors="coerce")
	work = work.dropna(subset=["date", "price", "client_id"])

	if "mois" not in work.columns:
		work["mois"] = work["date"].dt.to_period("M")
	if "annee" not in work.columns:
		work["annee"] = work["date"].dt.year

	# Build reusable tables
	ca_annuel = work.groupby("annee", as_index=False)["price"].sum().rename(columns={"price": "ca"})
	ca_mensuel = work.groupby("mois", as_index=False)["price"].sum().rename(columns={"price": "ca"})
	ca_mensuel["mois_dt"] = ca_mensuel["mois"].dt.to_timestamp()
	ca_mensuel["mm3"] = ca_mensuel["ca"].rolling(window=3, min_periods=1).mean()

	categ_col = "categ_label" if "categ_label" in work.columns else ("categ" if "categ" in work.columns else None)
	if categ_col is None:
		work["categ"] = "Inconnue"
		categ_col = "categ"

	ca_categ = work.groupby(categ_col, as_index=False)["price"].sum().rename(columns={"price": "ca"})
	ca_mensuel_categ = work.groupby(["mois", categ_col], as_index=False)["price"].sum()
	ca_mensuel_categ["mois_dt"] = ca_mensuel_categ["mois"].dt.to_timestamp()

	clients_mois = work.groupby("mois", as_index=False)["client_id"].nunique().rename(columns={"client_id": "nb_clients"})
	clients_mois["mois_dt"] = clients_mois["mois"].dt.to_timestamp()

	transactions_mois = work.groupby("mois").size().reset_index(name="nb_transactions")
	produits_mois = work.groupby("mois")["id_prod"].count().reset_index(name="nb_produits")
	volume_mois = transactions_mois.merge(produits_mois, on="mois", how="left")
	volume_mois["mois_dt"] = volume_mois["mois"].dt.to_timestamp()

	ca_produit = work.groupby("id_prod", as_index=False)["price"].sum().rename(columns={"price": "ca"}).sort_values("ca", ascending=False)
	top_df = ca_produit.head(top_n)
	flop_df = ca_produit.tail(top_n)

	ca_client = work.groupby("client_id", as_index=False)["price"].sum().rename(columns={"price": "ca_total"}).sort_values("ca_total", ascending=False)
	ca_client["Segment_Client"] = np.where(ca_client["ca_total"] > segment_threshold, "BtoB", "BtoC")
	ca_segments = ca_client.groupby("Segment_Client", as_index=False)["ca_total"].sum()

	out_dir = Path(output_dir)
	out_dir.mkdir(parents=True, exist_ok=True)

	wanted = set(selected) if selected else None

	def is_wanted(key: str) -> bool:
		return wanted is None or key in wanted

	figures: dict[str, plt.Figure] = {}

	# fig0.1 annual revenue
	if is_wanted("fig0_1"):
		fig, ax = plt.subplots(figsize=(12, 6))
		ax.plot(ca_annuel["annee"], ca_annuel["ca"], marker="o", color="steelblue")
		ax.yaxis.set_major_formatter(FuncFormatter(lambda x, pos: f"{x/1e6:.1f} M EUR"))
		ax.set_title("Evolution du chiffre d'affaire annuel")
		ax.set_xlabel("Annee")
		ax.set_ylabel("Chiffre d'affaires")
		ax.grid(True, alpha=0.3)
		_save_if_needed(fig, out_dir / "fig0_1_ca_annuel.png")
		figures["fig0_1"] = fig

	# fig0.2 annual revenue by category
	if is_wanted("fig0_2"):
		ann_cat = work.groupby(["annee", categ_col], as_index=False)["price"].sum().rename(columns={"price": "ca"})
		pivot = ann_cat.pivot(index="annee", columns=categ_col, values="ca").fillna(0)
		fig, ax = plt.subplots(figsize=(12, 6))
		pivot.plot(kind="bar", ax=ax)
		ax.yaxis.set_major_formatter(FuncFormatter(lambda x, pos: f"{x/1e6:.1f} M EUR"))
		ax.set_title("Chiffre d'affaires annuel par categorie")
		ax.set_xlabel("Annee")
		ax.set_ylabel("Chiffre d'affaires")
		ax.legend(title="Categorie")
		plt.tight_layout()
		_save_if_needed(fig, out_dir / "fig0_2_ca_annuel_categorie.png")
		figures["fig0_2"] = fig

	# fig3 global category share
	if is_wanted("fig3"):
		fig, ax = plt.subplots(figsize=(6, 6))
		ax.pie(ca_categ["ca"], labels=ca_categ[categ_col], autopct="%1.1f%%")
		ax.set_title("Repartition du CA global par categorie")
		plt.tight_layout()
		_save_if_needed(fig, out_dir / "fig3_repartition_categorie.png")
		figures["fig3"] = fig

	# fig4 monthly revenue
	if is_wanted("fig4"):
		fig, _ = plot_ca_mensuel(ca_mensuel, save_path=out_dir / "fig4_ca_mensuel.png")
		figures["fig4"] = fig

	# fig5 daily moving averages
	if is_wanted("fig5"):
		daily = work.groupby(pd.Grouper(key="date", freq="D"))["price"].sum().reset_index()
		daily["CA_7j"] = daily["price"].rolling(window=7).mean()
		daily["CA_30j"] = daily["price"].rolling(window=30).mean()
		fig, ax = plt.subplots(figsize=(12, 6))
		ax.plot(daily["date"], daily["price"], label="CA Journalier", alpha=0.5)
		ax.plot(daily["date"], daily["CA_7j"], label="Moyenne Mobile 7j", color="orange")
		ax.plot(daily["date"], daily["CA_30j"], label="Moyenne Mobile 30j", color="red")
		ax.set_xlabel("Date")
		ax.set_ylabel("Chiffre d'Affaires")
		ax.set_title("Comparaison des series temporelles")
		ax.legend()
		ax.grid(True, alpha=0.3)
		plt.tight_layout()
		_save_if_needed(fig, out_dir / "fig5_moyennes_mobiles.png")
		figures["fig5"] = fig

	# fig6 decomposition
	if include_decomposition and is_wanted("fig6") and len(ca_mensuel) >= 24:
		try:
			from statsmodels.tsa.seasonal import seasonal_decompose

			ca_ts = ca_mensuel.set_index("mois_dt")["ca"]
			decomp = seasonal_decompose(ca_ts, model="additive", period=12)

			fig, axes = plt.subplots(4, 1, figsize=(12, 10))
			axes[0].plot(decomp.observed, color="steelblue", linewidth=2)
			axes[0].set_title("CA observe")
			axes[1].plot(decomp.trend, color="seagreen", linewidth=2)
			axes[1].set_title("Tendance")
			axes[2].plot(decomp.seasonal, color="orange", linewidth=2)
			axes[2].set_title("Saisonnalite")
			axes[3].plot(decomp.resid, color="tomato", linewidth=2)
			axes[3].set_title("Residus")
			plt.suptitle("Decomposition de la serie temporelle du CA")
			plt.tight_layout()
			_save_if_needed(fig, out_dir / "fig6_decomposition_ca.png")
			figures["fig6"] = fig
		except Exception:
			pass

	# fig7 category bars
	if is_wanted("fig7"):
		fig, _ = plot_bar(
			df=ca_categ,
			x=categ_col,
			y="ca",
			title="Chiffre d'affaires par categorie",
			annotate=True,
			save_path=out_dir / "fig7_ca_categorie_bar.png",
		)
		figures["fig7"] = fig

	# fig8 monthly by category
	if is_wanted("fig8"):
		fig, ax = plt.subplots(figsize=(12, 6))
		for cat, grp in ca_mensuel_categ.groupby(categ_col):
			ax.plot(grp["mois_dt"], grp["price"], marker="o", linewidth=2, label=str(cat))
		ax.set_title("Evolution du CA mensuel par categorie")
		ax.set_xlabel("Mois")
		ax.set_ylabel("CA")
		ax.legend()
		ax.grid(True, alpha=0.3)
		ax.tick_params(axis="x", rotation=45)
		plt.tight_layout()
		_save_if_needed(fig, out_dir / "fig8_ca_mensuel_categorie.png")
		figures["fig8"] = fig

	# fig9 active clients
	if is_wanted("fig9"):
		fig, _ = plot_line(
			df=clients_mois,
			x="mois_dt",
			y="nb_clients",
			title="Nombre de clients actifs par mois",
			xlabel="Mois",
			ylabel="Nombre de clients",
			marker="o",
			save_path=out_dir / "fig9_clients_actifs.png",
		)
		figures["fig9"] = fig

	# fig10 transactions and products volume
	if is_wanted("fig10"):
		fig, axes = plt.subplots(2, 1, figsize=(12, 8))
		axes[0].plot(volume_mois["mois_dt"], volume_mois["nb_transactions"], color="steelblue", marker="o")
		axes[0].set_title("Nombre de transactions par mois")
		axes[1].plot(volume_mois["mois_dt"], volume_mois["nb_produits"], color="seagreen", marker="o")
		axes[1].set_title("Nombre de produits vendus par mois")
		for ax in axes:
			ax.tick_params(axis="x", rotation=45)
			ax.grid(True, alpha=0.3)
		plt.tight_layout()
		_save_if_needed(fig, out_dir / "fig10_volume_transactions_produits.png")
		figures["fig10"] = fig

	# fig11 top/flop products
	if is_wanted("fig11"):
		fig, _ = plot_top_flop(
			top_df=top_df,
			flop_df=flop_df,
			label_col="id_prod",
			value_col="ca",
			save_path=out_dir / "fig11_top_flop.png",
		)
		figures["fig11"] = fig

	# fig12 Lorenz
	if is_wanted("fig12"):
		fig, _, _ = plot_lorenz(
			ca_client["ca_total"],
			title="Courbe de Lorenz du chiffre d'affaires",
			save_path=out_dir / "fig12_lorenz.png",
		)
		figures["fig12"] = fig

	# Optional segment pie
	if is_wanted("fig_segments"):
		fig, _ = plot_pie_segments(
			values=ca_segments["ca_total"],
			labels=ca_segments["Segment_Client"],
			title="Repartition CA BtoB vs BtoC",
			colors=["tomato", "steelblue"],
			save_path=out_dir / "fig_segments_btob_btoc.png",
		)
		figures["fig_segments"] = fig

	return figures


def generate_julie_figures(
	df: pd.DataFrame,
	output_dir: str | Path = "../reports/figures",
	selected: list[str] | None = None,
) -> dict[str, plt.Figure]:
	"""Génère les figures de l'analyse Julie (corrélations BtoC).

	Paramètres
	----------
	df : DataFrame des transactions BtoC (colonnes requises : sex, categ, age, price, client_id).
	output_dir : répertoire de sauvegarde des figures.
	selected : liste optionnelle de clés à générer. None = toutes.

	Clés disponibles
	----------------
	julie_41_stacked_bar, julie_41_heatmap_residus,
	julie_42_scatter_age_ca, julie_42_hist, julie_42_qqplots,
	julie_43_scatter_freq, julie_44_scatter_panier, julie_45_boxplot_categ
	"""
	_require_columns(df, ["sex", "categ", "age", "price", "client_id"])

	out_dir = Path(output_dir)
	out_dir.mkdir(parents=True, exist_ok=True)

	wanted = set(selected) if selected else None

	def is_wanted(key: str) -> bool:
		return wanted is None or key in wanted

	figures: dict[str, plt.Figure] = {}

	# --- Pré-calculs communs ---
	table = pd.crosstab(df["sex"], df["categ"])

	df_client = (
		df.groupby(["client_id", "age"], as_index=False)["price"]
		.sum()
		.rename(columns={"price": "ca_total"})
	)

	freq_col = next((c for c in ["session_id", "transaction_id"] if c in df.columns), None)
	if freq_col:
		df_freq = (
			df.groupby(["client_id", "age"])[freq_col]
			.nunique()
			.reset_index()
			.rename(columns={freq_col: "frequence_achat"})
		)
	else:
		df_freq = df.groupby(["client_id", "age"]).size().reset_index(name="frequence_achat")

	df_panier = df.groupby(["client_id", "age"], as_index=False).agg(
		ca_total=("price", "sum"),
		nb_achats=("price", "count"),
	)
	df_panier["panier_moyen"] = df_panier["ca_total"] / df_panier["nb_achats"]

	# --- 4.1 Barres empilées 100 % sexe × catégorie ---
	if is_wanted("julie_41_stacked_bar"):
		pct = table.div(table.sum(axis=1), axis=0) * 100
		colors = list(plt.cm.Set2.colors)
		fig, ax = plt.subplots(figsize=(8, 5))
		bottom = np.zeros(len(pct))
		for i, col in enumerate(pct.columns):
			vals = pct[col].values
			ax.bar(pct.index, vals, bottom=bottom, label=str(col), color=colors[i % len(colors)])
			for j, (b, v) in enumerate(zip(bottom, vals)):
				if v > 5:
					ax.text(j, b + v / 2, f"{v:.1f}%", ha="center", va="center",
						fontsize=9, color="white", fontweight="bold")
			bottom += vals
		ax.set_xlabel("Sexe")
		ax.set_ylabel("Proportion (%)")
		ax.set_title("Répartition des catégories par sexe (100 %)")
		ax.legend(title="Catégorie", bbox_to_anchor=(1.05, 1), loc="upper left")
		plt.tight_layout()
		_save_if_needed(fig, out_dir / "julie_41_stacked_bar.png")
		figures["julie_41_stacked_bar"] = fig

	# --- 4.1 Heatmap résidus standardisés chi² ---
	if is_wanted("julie_41_heatmap_residus"):
		from scipy.stats import chi2_contingency
		_, _, _, expected = chi2_contingency(table)
		residus = (table.values - expected) / np.sqrt(expected)
		fig, ax = plt.subplots(figsize=(8, 4))
		im = ax.imshow(residus, cmap="RdBu_r", aspect="auto", vmin=-3, vmax=3)
		plt.colorbar(im, ax=ax, label="Résidu standardisé")
		ax.set_xticks(range(len(table.columns)))
		ax.set_xticklabels(table.columns)
		ax.set_yticks(range(len(table.index)))
		ax.set_yticklabels(table.index)
		for i in range(residus.shape[0]):
			for j in range(residus.shape[1]):
				ax.text(j, i, f"{residus[i, j]:.2f}", ha="center", va="center", fontsize=10)
		ax.set_title("Résidus standardisés — Sexe × Catégorie")
		ax.set_xlabel("Catégorie")
		ax.set_ylabel("Sexe")
		plt.tight_layout()
		_save_if_needed(fig, out_dir / "julie_41_heatmap_residus.png")
		figures["julie_41_heatmap_residus"] = fig

	# --- 4.2 Scatter âge vs CA total ---
	if is_wanted("julie_42_scatter_age_ca"):
		fig, ax = plt.subplots(figsize=(8, 5))
		ax.scatter(df_client["age"], df_client["ca_total"], alpha=0.5, color="steelblue", edgecolors="none")
		m, b = np.polyfit(df_client["age"], df_client["ca_total"], 1)
		x_line = np.linspace(df_client["age"].min(), df_client["age"].max(), 100)
		ax.plot(x_line, m * x_line + b, color="tomato", linewidth=2, label="Tendance linéaire")
		ax.set_xlabel("Âge")
		ax.set_ylabel("CA total (€)")
		ax.set_title("Âge vs CA total par client")
		ax.legend()
		plt.tight_layout()
		_save_if_needed(fig, out_dir / "julie_42_scatter_age_ca.png")
		figures["julie_42_scatter_age_ca"] = fig

	# --- 4.2 Histogrammes âge + CA total ---
	if is_wanted("julie_42_hist"):
		fig, axes = plt.subplots(1, 2, figsize=(12, 5))
		axes[0].hist(df_client["age"], bins=20, color="steelblue", edgecolor="white")
		axes[0].set_title("Distribution de l'âge")
		axes[0].set_xlabel("Âge")
		axes[0].set_ylabel("Fréquence")
		axes[1].hist(df_client["ca_total"], bins=20, color="seagreen", edgecolor="white")
		axes[1].set_title("Distribution du CA total")
		axes[1].set_xlabel("CA total (€)")
		axes[1].set_ylabel("Fréquence")
		plt.tight_layout()
		_save_if_needed(fig, out_dir / "julie_42_hist.png")
		figures["julie_42_hist"] = fig

	# --- 4.2 QQ plots âge + CA total ---
	if is_wanted("julie_42_qqplots"):
		from scipy.stats import probplot
		fig, axes = plt.subplots(1, 2, figsize=(12, 5))
		probplot(df_client["age"], dist="norm", plot=axes[0])
		axes[0].set_title("QQ plot — Âge")
		probplot(df_client["ca_total"], dist="norm", plot=axes[1])
		axes[1].set_title("QQ plot — CA total")
		plt.tight_layout()
		_save_if_needed(fig, out_dir / "julie_42_qqplots.png")
		figures["julie_42_qqplots"] = fig

	# --- 4.3 Scatter âge vs fréquence d'achat ---
	if is_wanted("julie_43_scatter_freq"):
		fig, ax = plt.subplots(figsize=(8, 5))
		ax.scatter(df_freq["age"], df_freq["frequence_achat"], alpha=0.5, color="mediumpurple", edgecolors="none")
		m, b = np.polyfit(df_freq["age"], df_freq["frequence_achat"], 1)
		x_line = np.linspace(df_freq["age"].min(), df_freq["age"].max(), 100)
		ax.plot(x_line, m * x_line + b, color="tomato", linewidth=2, label="Tendance linéaire")
		ax.set_xlabel("Âge")
		ax.set_ylabel("Fréquence d'achat")
		ax.set_title("Âge vs Fréquence d'achat par client")
		ax.legend()
		plt.tight_layout()
		_save_if_needed(fig, out_dir / "julie_43_scatter_freq.png")
		figures["julie_43_scatter_freq"] = fig

	# --- 4.4 Scatter âge vs panier moyen ---
	if is_wanted("julie_44_scatter_panier"):
		fig, ax = plt.subplots(figsize=(8, 5))
		ax.scatter(df_panier["age"], df_panier["panier_moyen"], alpha=0.5, color="darkorange", edgecolors="none")
		m, b = np.polyfit(df_panier["age"], df_panier["panier_moyen"], 1)
		x_line = np.linspace(df_panier["age"].min(), df_panier["age"].max(), 100)
		ax.plot(x_line, m * x_line + b, color="tomato", linewidth=2, label="Tendance linéaire")
		ax.set_xlabel("Âge")
		ax.set_ylabel("Panier moyen (€)")
		ax.set_title("Âge vs Panier moyen par client")
		ax.legend()
		plt.tight_layout()
		_save_if_needed(fig, out_dir / "julie_44_scatter_panier.png")
		figures["julie_44_scatter_panier"] = fig

	# --- 4.5 Boxplot âge par catégorie ---
	if is_wanted("julie_45_boxplot_categ"):
		categories = sorted(df["categ"].dropna().unique())
		data_by_cat = [df[df["categ"] == c]["age"].dropna().values for c in categories]
		fig, ax = plt.subplots(figsize=(10, 5))
		bp = ax.boxplot(data_by_cat, labels=[str(c) for c in categories], patch_artist=True)
		colors = list(plt.cm.Set2.colors)
		for patch, color in zip(bp["boxes"], colors):
			patch.set_facecolor(color)
			patch.set_alpha(0.7)
		ax.set_xlabel("Catégorie")
		ax.set_ylabel("Âge")
		ax.set_title("Distribution de l'âge par catégorie de produit")
		ax.grid(True, axis="y", alpha=0.3)
		plt.tight_layout()
		_save_if_needed(fig, out_dir / "julie_45_boxplot_categ.png")
		figures["julie_45_boxplot_categ"] = fig

	return figures
