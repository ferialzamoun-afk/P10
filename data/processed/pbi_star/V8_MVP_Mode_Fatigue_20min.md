# Mode fatigue (20 min) - Livraison ce soir

## Objectif
- Ne rien casser
- Garder la base stable V6
- Corriger uniquement les points soutenance

## Fichier de travail
- Ouvrir Dashboard_eau_v8_mvp_depuis_v6.pbix

## Etape 1 (5 min) - Coller seulement 4 mesures
Copier/coller depuis V8_MVP_Corrections_DAX.txt uniquement:
- Accès eau potable % moyen
- Couleur accès eau mixte DWFA
- Badge alerte mortalité - texte
- Badge alerte mortalité - couleur

## Etape 2 (5 min) - Brancher les visuels
- Carte monde: couleur de remplissage = Couleur accès eau mixte DWFA
- Info-bulle: afficher Taux mortalité WASH moyen + Badge alerte mortalité - texte
- Couleur du badge (ou carte KPI): Badge alerte mortalité - couleur

## Etape 3 (5 min) - 3 tests obligatoires
- Niger: doit sortir en défavorable (rouge)
- Italie: doit sortir favorable (bleu)
- Chine: visible sur carte (si non visible: utiliser iso3 en emplacement)

## Etape 4 (5 min) - Verrouillage soutenance
- Année fixée à 2016
- Mention affichée: ND = donnée non disponible (non assimilée à 0)
- Enregistrer

## STOP - ne plus toucher
Si ces 3 tests passent, on livre ce soir sans ajouter d'autres évolutions.
