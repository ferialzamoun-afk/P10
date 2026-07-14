# Resume methodologique du pipeline de donnees (Notebooks 01, 02, 03)

## 1. Finalite globale du pipeline
Le pipeline met en place une chaine reproductible qui va de l inspection des sources brutes jusqu a la restitution analytique orientee decision.

La logique generale est la suivante:
- Notebook 01: qualifier et fiabiliser les donnees sources, construire les indicateurs, produire les scores de priorisation et publier les exports.
- Notebook 02: formaliser le pipeline en couches (staging, intermediate, marts), auditer les contrats de publication et garantir la reproductibilite.
- Notebook 03: exploiter les marts publies pour produire une analyse metier par domaine, avec visualisations et messages de soutenance.

## 2. Notebook 01 - Inspection, normalisation et construction analytique

### 2.1 Chargement et cadrage des sources
Le notebook charge les 5 fichiers bruts principaux:
- Population.csv
- RegionCountry.csv
- PoliticalStability.csv
- MortalityRateAttributedToWater.csv
- BasicAndSafelyManagedDrinkingWaterServices.csv

Ces tables sont ensuite passees dans un schema canonique francais via src/schema_fr.py afin de:
- harmoniser les noms de colonnes,
- standardiser les formats,
- etablir une base commune pour les etapes aval.

### 2.2 Inspection de qualite
Le notebook realise un controle structurel et metier:
- apercu des tables,
- fonctions d inspection des types et des valeurs manquantes,
- verification des granularites,
- controle des correspondances pays entre jeux de donnees,
- audit de qualite cible.

Points de vigilance rendus explicites:
- heterogeneite des noms de pays,
- contraintes d unite (notamment population),
- disponibilite limitee de la mortalite WASH (signal 2016 a traiter avec prudence en temporel).

### 2.3 Preparation analytique
La preparation construit un socle analytique harmonise:
- standardisation des noms de pays,
- rattachement pays-region via un referentiel de correspondance,
- mise en forme longue des indicateurs,
- fusion des indicateurs sur les cles pays-annee,
- normalisations necessaires au calcul de scores.

### 2.4 Construction des scores de priorisation
Le notebook construit trois scores metier:
- score_creation_services,
- score_modernisation_services,
- score_gouvernance.

Pour la gouvernance, la logique retenue repose sur:
- inversion d un score de mortalite WASH normalise,
- combinaison avec le score d acces a l eau,
- projection finale sur une echelle 0-100 pour la priorisation.

Puis un champ action_prioritaire est assigne en fonction du score dominant:
- Creer ou etendre les services d eau,
- Moderniser les services d eau,
- Renforcer la gouvernance politique.

### 2.5 Publication des sorties
Le notebook publie des sorties reutilisables:
- marts analytiques EN et FR (csv_enrichis/en et csv_enrichis/fr),
- snapshots de priorisation (dont focus),
- tables pour modele etoile Power BI (pbi_star), avec table de faits et dimensions.

Cette etape fixe le contrat de donnees pour la BI et les analyses.

## 3. Notebook 02 - Formalisation en couches et gouvernance de publication

### 3.1 Couche staging
Role:
- atterrissage controle des donnees raw,
- verification de schema et de coherence minimale,
- detection precoce des anomalies de format et de couverture.

### 3.2 Couche intermediate
Role:
- centraliser les transformations metier et qualite,
- produire un socle harmonise independant des outils de restitution,
- conserver les regles critiques (standardisation pays, unites, normalisation indicateurs).

Sorties intermediaires controlees:
- country_region_reference (EN/FR),
- water_indicators_long (EN/FR).

### 3.3 Couche marts
Role:
- publier des tables orientees usage,
- dissocier logique de calcul et logique de consommation,
- servir les usages analytiques et dashboard.

Le notebook audite la publication sur plusieurs dimensions:
- existence des fichiers,
- nombre de lignes,
- nombre de colonnes,
- alignement EN/FR en volume et structure,
- granularite et cles metier,
- contrat semantique de traduction des colonnes.

Point de gouvernance central:
- EN et FR sont deux publications soeurs issues du meme socle intermediate,
- pbi_star reste un contrat technique distinct pour Power BI.

### 3.4 Reproductibilite GitHub
Le notebook explicite les conditions de reproductibilite:
- organisation claire raw/processed/notebooks,
- transformations versionnees,
- sorties deterministes,
- absence de manipulations manuelles cachees,
- contrats de donnees explicites par couche.

## 4. Notebook 03 - Exploitation analytique et restitution metier

### 4.1 Mise en place de la base d analyse
Le notebook consomme principalement:
- dashboard_water_country_year.csv,
- priority_snapshot_focus_2016.csv,
- country_region_reference.csv.

Il reconstruit une base d analyse avec:
- securisation de la region via referentiel,
- variables derivees (population en millions, part urbaine, ecart de qualite de service),
- recalcul de score d effectivite gouvernementale si absent,
- controles de coherence d unite population.

### 4.2 Parametrage analytique
Filtres explicites pour la lecture:
- fenetre temporelle,
- perimetre regional,
- actions prioritaires,
- seuil minimal de population,
- annee de snapshot pour la priorisation.

### 4.3 Analyse par domaines
Trois blocs metier sont analyses avec des visuels dedies:
- Domaine 1 - Creation de services: acces eau vs structure urbaine/rurale, priorisation des pays.
- Domaine 2 - Modernisation: comparaison service de base vs service gere en toute securite.
- Domaine 3 - Gouvernance: croisement stabilite politique et effectivite gouvernementale, plus lecture geographique.

### 4.4 Traduction operationnelle BI
Le notebook documente la transposition en Power BI:
- proposition de visuels par domaine,
- recommandations de slicers,
- mesures DAX (version standard et version exact de reproduction du score gouvernance),
- principes de mise en page et de lisibilite.

## 5. Enchainement methodologique de bout en bout
Le pipeline suit une logique DataOps analytique coherente:
1. Inspecter et qualifier les sources (Notebook 01).
2. Harmoniser et structurer les donnees (Notebook 01 puis formalisation Notebook 02).
3. Calculer les indicateurs et scores de priorisation (Notebook 01).
4. Publier des contrats de donnees stables EN/FR + Power BI (Notebook 01 et audits Notebook 02).
5. Exploiter ces contrats pour une restitution metier actionnable (Notebook 03).

## 6. Points de robustesse a mettre en avant a l oral
- Separation claire des couches staging, intermediate, marts.
- Contrats de publication explicites et audites.
- Publication bilingue EN/FR sans divergence de fond.
- Contrat pbi_star dedie a la compatibilite Power BI.
- Traite explicite des limites de donnees (notamment mortalite WASH).
- Pipeline reproductible, versionnable et oriente decision.
