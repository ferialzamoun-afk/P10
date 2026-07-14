# P10 - Dashboard Eau, Population et Gouvernance

## Vue d'ensemble

**P10** est un projet d'analyse décisionnelle qui met en place un pipeline complet de données en vue de la création d'un **dashboard Power BI interactif** sur les enjeux mondiaux d'accès à l'eau potable, de gouvernance politique et de mortalité liée à l'eau (WASH).

Le projet couvre trois niveaux de lecture :
1. **Mondiale** : disparités géographiques et comparaisons continentales
2. **Métier** : trois domaines d'action (création, modernisation, gouvernance)
3. **Nationale** : analyse détaillée par pays avec trajectoires temporelles

---

## Objectifs métier

Le dashboard P10 répond à quatre besoins utilisateurs prioritaires :

| Besoin | Indicateurs clés | Visualisation |
|--------|-----------------|---------------|
| Comprendre la stabilité politique mondiale | Stabilité politique par pays et continent | Carte choropléthe + bar chart |
| Localiser les zones critiques WASH | Mortalité WASH, accès à l'eau potable | Carte du monde + ranking top N |
| Identifier les priorités d'action publique | Scores métier (création, modernisation, gouvernance) | Matrice de priorisation |
| Explorer les trajectoires nationales | Population rurale, accès eau, services safely managed | KPI + courbes temporelles + tableaux |

---

## Structure du projet

```
P10/
├── notebooks/                              # Pipeline analytique
│   ├── 01 - Inspection des données.ipynb  # Qualification et normalisation
│   ├── 02 - Préparation et nettoyage...   # Formalisation en couches
│   └── 03 - Analyses des groupements...   # EDA et analyses métier
│
├── data/
│   ├── raw/                                # Données sources brutes
│   │   ├── Population.csv
│   │   ├── RegionCountry.csv
│   │   ├── PoliticalStability.csv
│   │   ├── MortalityRateAttributedToWater.csv
│   │   └── BasicAndSafelyManagedDrinkingWaterServices.csv
│   │
│   └── processed/                          # Données transformées
│       ├── pbi_star/                       # Tables étoile Power BI
│       │   ├── Dashboard_eau_v6.pbit
│       │   ├── fact_dashboard_star_fr.csv
│       │   ├── dim_pays_star_fr.csv
│       │   └── [dimensions détaillées]
│       │
│       ├── csv_enrichis/                   # Marts analytiques
│       │   ├── en/ (anglais)
│       │   └── fr/ (français)
│       │
│       └── [dimensions et références]
│
├── src/                                    # Modules réutilisables
│   ├── data_manager.py                     # Gestion des données
│   ├── schema_fr.py                        # Schéma français canonique
│   ├── figures_export.py                   # Export des visualisations
│   ├── kpi_export.py                       # Calcul des KPI
│   └── rebuild_geography_exports.py        # Reconstruction géographique
│
├── requirements.txt                        # Dépendances Python
└── [documentation métier et dashboards]
```

---

## Pipeline de données

### Notebook 01 - Inspection, normalisation et construction analytique

**Objectif** : Qualifier les données sources, les harmoniser et construire les indicateurs de base.

**Étapes principales** :
1. **Chargement** des 5 fichiers source (population, régions, stabilité politique, mortalité WASH, services eau)
2. **Cadrage** via schéma canonique français (`src/schema_fr.py`)
3. **Inspection de qualité** : types, valeurs manquantes, granularités, cohérence pays
4. **Préparation analytique** : standardisation des noms de pays, rattachement pays-région
5. **Construction des scores** :
   - `score_creation_services` (accès à l'eau potable + urbanisation)
   - `score_modernisation_services` (service basique vs safely managed)
   - `score_gouvernance` (stabilité politique, mortalité WASH, efficacité)
6. **Publication** : marts analytiques (EN/FR) et tables étoile Power BI

### Notebook 02 - Formalisation en couches et gouvernance

**Objectif** : Structurer le pipeline en couches reproductibles et auditer les contrats de publication.

**Couches** :
- **Staging** : atterrissage contrôlé des données brutes
- **Intermediate** : transformations métier centralisées (harmonisation, enrichissement)
- **Marts** : tables orientées consommation (Power BI, analyses)

**Sorties** :
- Dimensions: `country_region_reference`, `water_indicators_long`
- Faits: `fact_dashboard_star_fr.csv`

### Notebook 03 - Analyses métier et EDA

**Objectif** : Exploiter les marts pour produire des analyses métier par domaine et des visualisations pour la soutenance.

**Domaines analysés** :
1. **Création de services** : scatter plot population urbaine vs accès eau
2. **Modernisation de services** : évolution basique → safely managed
3. **Gouvernance** : stabilité politique vs proxy d'efficacité

---

## Configuration et exécution

### Prérequis

- Python 3.12+
- pip ou conda
- Jupyter Lab/Notebook

### Installation

1. **Cloner ou accéder au projet** :
   ```bash
   cd c:\Users\feria\Documents\P10
   ```

2. **Créer et activer l'environnement virtuel** (si nécessaire) :
   ```bash
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

3. **Installer les dépendances** :
   ```bash
   pip install -r requirements.txt
   ```

### Exécution des notebooks

Les notebooks doivent être exécutés dans l'ordre :

```bash
# Lance Jupyter Lab
jupyter lab

# Puis exécute dans l'ordre:
# 1. 01 - Inspection des données.ipynb
# 2. 02 - Préparation et nettoyage des données.ipynb
# 3. 03 - Analyses des groupements de pays - EDA...ipynb
```

---

## Dépendances principales

| Package | Rôle |
|---------|------|
| `pandas >= 2.2` | Manipulation et agrégation de données |
| `numpy >= 1.26` | Calculs numériques et matrices |
| `matplotlib >= 3.9` | Visualisations statiques |
| `seaborn >= 0.13` | Visualisations statistiques |
| `plotly >= 5.24` | Visualisations interactives |
| `country_converter >= 1.3` | Standardisation des noms de pays |
| `openpyxl >= 3.1` | Export Excel |
| `babel >= 2.17` | Gestion des locales et traductions |

---

## Artefacts clés

### Données exportées

| Fichier | Description | Usage |
|---------|-------------|-------|
| `pbi_star/fact_dashboard_star_fr.csv` | Table de faits (pays × année × indicateurs) | Power BI - visualisations |
| `pbi_star/dim_pays_star_fr.csv` | Dimension pays enrichie (région, indicateurs statiques) | Power BI - contexte |
| `pbi_star/Dashboard_eau_v6.pbit` | Modèle Power BI complet | BI directe |
| `csv_enrichis/fr/` | Marts analytiques français | Analyses complémentaires |
| `csv_enrichis/en/` | Marts analytiques anglais | Analyses complémentaires |

### Dimensions de référence

- `dim_pays.csv` : Référenciel maître des pays
- `dim_region_fr.csv` : Continents et régions (français)
- `dim_annee.csv` : Couverture temporelle des données
- `dim_indicateur.csv` : Catalogue des indicateurs disponibles

---

## Architecture du dashboard Power BI

### Page 1 - Vue mondiale et continentale

**Visuels** :
- Carte choropléthe (stabilité politique ou mortalité WASH)
- Bar chart par continent (comparaison continentale)
- KPI cards (moyennes globales)
- Top N pays (benchmark)

**Filtres** : Année, région, action prioritaire

### Page 2 - Domaines métier

**Visuels** :
- Scatter plot : création de services (accès eau vs urbanisation)
- Grouped bar chart : modernisation (basique vs safely managed)
- Scatter plot avec quadrants : gouvernance (stabilité vs efficacité)
- Carte de support (score gouvernance ou mortalité)

**Filtres** : Année, région, seuil population

### Page 3 - Vue nationale

**Visuels** :
- KPI cards du pays sélectionné
- Line plot : évolution démographique (population rurale vs totale)
- Line plot : trajectoire d'accès eau et services
- Tableau détaillé : années × indicateurs

**Filtres** : Pays, année

---

## Remarques de qualité des données

### Points de vigilance

1. **Mortalité WASH** : données disponibles surtout jusqu'à 2016 ; traiter les valeurs récentes avec prudence en analyses temporelles
2. **Hétérogénéité des noms de pays** : standardisés via `country_converter` ; certains territoires (Hong Kong, Macao, Taiwan, etc.) ont été exclus pour éviter les conflits de classification régionale
3. **Granularité population** : données annuelles ; unités validées (habitants)
4. **Couverture géographique** : 193 pays attendus ; quelques lacunes ciblées par `data_curation`

### Audits effectués

- Validation des correspondances pays × région (2026-06-12)
- Suppression de 5 territoires créant des anomalies de classification
- Vérification des totaux continentaux vs sommes nationales
- Audit de concordance EN ↔ FR

---

## Utilisation programmatique

Les modules `src/` facilitent la réutilisation du pipeline :

```python
from src.data_manager import load_raw_data, publish_marts
from src.schema_fr import apply_schema_fr
from src.kpi_export import compute_scores

# Charger et transformer
data = load_raw_data()
data_fr = apply_schema_fr(data)
scores = compute_scores(data_fr)

# Publier
publish_marts(scores, lang=['fr', 'en'])
```

---

## Maintenance et mises à jour

### Recalcul complet

Pour relancer la totalité du pipeline :

1. Placer les fichiers source dans `data/raw/`
2. Exécuter les 3 notebooks dans l'ordre
3. Les sorties seront publiées dans `data/processed/`

### Enrichissements possibles

- Ajout de nouveaux indicateurs (climat, budget, etc.)
- Extension régionale (sous-régions, bassins fluviaux)
- Intégration de données en temps réel
- Versioning des modèles de score

---

## Auteurs et dates

- **Projet** : P10 - DWFA (Data Work For Africa)
- **Dernière mise à jour** : 2026-06-12
- **Version données** : v6 (modèle Power BI Dashboard_eau_v6.pbit)

---

## Ressources et documentation

- [Blueprint complet](blueprint_P10_dashboard_eau.md) : détail des besoins et visuels
- [Glossaire métier](contexte_DWFA_glossaire_eau.md) : définitions des indicateurs
- [Méthodologie](resume_methodologique_pipeline_notebooks_01_02_03.md) : détails du pipeline
- [Slide de méthodologie](slide_methodologie_demarche_P10.md) : présentation visuelle
- [QCM de soutenance](questions_pieges_soutenance_P10.md) : points critiques

---

## Support et questions

Pour toute question ou améliorations, se référer à la documentation métier ou aux commentaires détaillés dans les notebooks.

**Licence** : Usage interne DWFA / P10

