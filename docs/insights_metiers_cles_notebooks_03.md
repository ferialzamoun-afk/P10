# Insights metiers cles pour la presentation

## 1. Message executif
La priorisation des pays ne repose pas sur un indicateur unique mais sur trois logiques metier complementaires:
- creation ou extension des services d eau,
- modernisation de la qualite de service,
- gouvernance et contexte politico-sanitaire.

L apport principal de l analyse est de transformer des donnees heterogenes en decisions differenciees selon le type d effort a engager.

## 2. Insights transverses

### 2.1 Un pays prioritaire ne l est pas pour la meme raison
Deux pays avec un niveau d acces similaire peuvent relever d actions opposees:
- manque d infrastructure a creer,
- besoin de modernisation qualitative,
- contexte de gouvernance a accompagner.

Insight actionnable:
- eviter les plans d intervention uniformes,
- aligner le type de projet avec le score dominant.

### 2.2 La region sert au cadrage, le pays reste l unite d action
Les tendances regionales facilitent la lecture macro, mais la priorisation effective se joue au niveau pays.

Insight actionnable:
- utiliser la region pour filtrer et contextualiser,
- conserver des decisions et plans au niveau pays.

### 2.3 Les controles de qualite doivent etre visibles
Les lignes non classees ou partiellement renseignees ne sont pas des erreurs de visualisation: ce sont des limites de couverture a rendre explicites.

Insight actionnable:
- integrer une page de controle qualite dans la restitution BI,
- separer lecture metier et diagnostic de couverture.

## 3. Domaine 1 - Creation de services

### 3.1 Lecture metier
Le croisement acces eau potable de base et structure urbaine/rurale montre des besoins d infrastructure differents:
- pays a faible acces avec forte urbanisation: tension sur capacite urbaine,
- pays a faible acces avec forte ruralite: enjeu de desserte diffuse.

### 3.2 Insight cle
Le meme deficit d acces ne suppose pas le meme modele de deploiement.

### 3.3 Decision recommandee
Segmenter les programmes de creation de services selon la morphologie demographique:
- logique reseau dense en contexte urbain,
- logique couverture territoriale en contexte rural.

## 4. Domaine 2 - Modernisation des services

### 4.1 Lecture metier
L ecart entre service de base et service gere en toute securite met en evidence des pays ou l infrastructure existe mais ne garantit pas encore un niveau de securite satisfaisant.

### 4.2 Insight cle
Le besoin prioritaire n est pas toujours de construire plus, mais d ameliorer la qualite et la fiabilite de l existant.

### 4.3 Decision recommandee
Orienter les investissements vers:
- securisation sanitaire,
- qualite de traitement et de distribution,
- reduction du gap de service plutot qu extension brute.

## 5. Domaine 3 - Gouvernance et consulting

### 5.1 Lecture metier
Le nuage stabilite politique x effectivite gouvernementale (proxy base sur acces eau + mortalite WASH normalisee) permet d identifier des contextes differencies:
- zones favorables a un accompagnement de performance,
- zones plus fragiles demandant un appui institutionnel progressif.

### 5.2 Insight cle
La priorisation gouvernance ne se limite ni a la politique ni a la sante: elle nait de leur combinaison.

### 5.3 Decision recommandee
Adapter les interventions de consulting selon les quadrants:
- haute stabilite et haute effectivite: optimisation et acceleration,
- basse stabilite et/ou basse effectivite: renforcement institutionnel et gestion du risque.

## 6. Point methodologique a expliciter en soutenance
La mortalite WASH est une contrainte forte de lecture (disponibilite 2016):
- elle est robuste pour un snapshot de priorisation,
- elle ne doit pas etre surinterpretee en dynamique temporelle longue.

Message a porter:
- l analyse assume cette limite, la documente et la transforme en regle d usage.

## 7. Traduction directe pour Power BI

### 7.1 Ce qui fonctionne bien
- Une page Domaines metiers avec slicers communs (annee, region, action prioritaire).
- Top N par score pour conserver la lisibilite.
- Visuels differencies par domaine (nuage creation, barres modernisation, nuage gouvernance).

### 7.2 Ce qui securise la lecture
- Une page de controle qualite dediee.
- Affichage explicite des lignes Non classe.
- Rappel des limites de couverture et des hypotheses de score.

## 8. Storyline conseilee pour l oral
1. Expliquer le passage de la donnee brute a la decision (pipeline en 3 notebooks).
2. Montrer que la priorisation est multi-logiques, pas monolithique.
3. Presenter un exemple concret par domaine.
4. Conclure sur la valeur operationnelle: quoi faire, ou, et pourquoi.
