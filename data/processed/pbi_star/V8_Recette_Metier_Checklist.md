# Recette Metier - V8 MVP (30-45 min)

## 1) Préparation
- Ouvrir Dashboard_eau_v8.pbix
- Vérifier le filtre Année = 2016 (page principale)
- Carte: Emplacement = iso3, pas nom pays
- Carte: Légende région retirée

## 2) Mesures à mettre à jour
- Coller les mesures du fichier V8_MVP_Corrections_DAX.txt
- Remplacer les anciennes mesures utilisées par:
  - Couleur accès eau mixte DWFA
  - Badge alerte mortalité - texte
  - Badge alerte mortalité - couleur
  - Afficher_Pays_Eligibles_v8 (si filtre booléen utilisé)

## 3) Contrôles ciblés
- Chine (CHN) visible sur la carte
- Groenland: ND ou gris si donnée manquante (pas faux 0)
- Niger: mortalité élevée => badge défavorable (rouge)
- Italie: mortalité faible => badge favorable (bleu)

## 4) Contrôle cohérence visuelle
- Seuils alerte conservés (rouge/orange)
- Zone favorable en palette bleue DWFA
- Info-bulle contient: accès eau %, mortalité/100k, décès, stabilité

## 5) KPI de couverture (option rapide)
- Afficher mention: "ND = donnée non disponible (non assimilée à 0)"
- Vérifier absence de COALESCE(...,0) sur les mesures critiques d'affichage

## 6) Go/No-Go livraison
- Go si:
  - carte stable par pays
  - badges cohérents avec les valeurs
  - 3 cas tests validés (CHN, GRL, NER)
