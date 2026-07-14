# Slide - Methodologie et demarche data-driven (P10)

## Message cle (a afficher)
Une demarche pilotee par les donnees, de la collecte multi-sources jusqu'a la livraison de tables fiabilisees pour Power BI.

## 1) Collecte et cadrage des donnees
- Sources mobilisees : acces a l'eau (JMP), mortalite WASH, population (UN), stabilite politique (WGI), referentiel pays/regions.
- Import des fichiers bruts dans data/raw puis normalisation des noms de variables, des types et des cles pays.
- Verification initiale : couverture temporelle, granularite (pays-annee), valeurs manquantes, doublons, coherence des unites.

## 2) EDA (analyse exploratoire)
- Inspection des distributions, outliers, ruptures temporelles et comparabilite inter-pays.
- Controle des relations metier : acces basic vs safely managed, lien WASH-vulnerabilite, poids demographique.
- Validation d'hypotheses pour orienter la priorisation et eviter les interpretations trompeuses.

## 3) Analyse preparatoire et transformation
- Harmonisation des dimensions : pays, annee, indicateur, zones geographiques enrichies (continent, sous-region ONU, region OMS).
- Construction des indicateurs utiles au pilotage : ecarts de service, niveaux de vulnerabilite, snapshots de priorite (2016 pour WASH).
- Traitement des limites de donnees : serie partielle WASH, choix de regles explicites de filtrage/aggregation.

## 4) Industrialisation des tables analytiques
- Generation des tables intermediaires et enrichies dans data/processed.
- Production de jeux bilingues FR/EN pour usage analyse et communication.
- Structuration en modele analytique pour BI (dimensions + table de faits).

## 5) Export final pour Power BI
- Exports cibles dans data/processed/pbi_star :
  - dim_action_star_fr.csv
  - dim_annee_star_fr.csv
  - dim_date_star_fr.csv
  - dim_pays_star_fr.csv
  - fact_dashboard_star_fr.csv
- Benefice : modele lisible, performant et directement exploitable dans Power BI.

## Gouvernance qualite (a mentionner en oral)
- Tracabilite : chaque indicateur garde sa source, son unite et sa definition.
- Reproductibilite : pipeline notebook/script de l'inspection a l'export.
- Transparence : distinction claire entre donnees sources et champs calcules.

---

## Version ultra-courte (si tu veux une slide tres compacte)
Collecter -> Controler -> Explorer (EDA) -> Transformer -> Structurer en etoile -> Exporter vers Power BI.

Le projet P10 applique une logique pilotee par les donnees pour prioriser l'action (creation, modernisation, gouvernance) sur une base comparable pays-annee et documentee.
