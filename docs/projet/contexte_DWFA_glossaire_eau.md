# Contexte DWFA et Glossaire des Donnees Eau

## 1. Proposition pour le projet

Pour ton projet, je te recommande d'ajouter avant la phase Power BI un bloc documentaire court mais solide, construit en deux niveaux :

1. un contexte metier DWFA pour expliquer pourquoi les indicateurs eau, population, mortalite WASH et stabilite politique sont mobilises ensemble ;
2. un glossaire de definitions pour expliciter chaque donnee manipulee, sa source, son unite, sa couverture et son interpretation.

L'objectif n'est pas seulement documentaire. Ce bloc sert a :

- justifier le choix des indicateurs ;
- montrer que les donnees n'ont pas toutes le meme sens ni la meme couverture temporelle ;
- expliquer les champs calcules et les scores derives dans le pipeline ;
- faciliter la lecture du dashboard par un jury non technique.

## 2. Cadre de lecture DWFA pour ce projet

Dans une lecture DWFA orientee vulnerabilite, resilience et capacite d'action publique, l'eau n'est pas seulement un service technique. C'est un sujet croisant :

- l'exposition des populations a un risque sanitaire ;
- la capacite des infrastructures a fournir un service de base ;
- la qualite reelle de ce service ;
- la structure territoriale des besoins, notamment urbains et ruraux ;
- la capacite institutionnelle et politique a conduire des politiques publiques stables.

Autrement dit, le projet ne cherche pas seulement a mesurer l'eau potable. Il cherche a identifier :

- ou il faut creer des services ;
- ou il faut moderniser des services deja existants ;
- ou il faut accompagner la gouvernance publique pour rendre les politiques de l'eau plus efficaces.

## 3. Point de vigilance methodologique

L'indicateur WASH ne mesure pas l'eau potable seule. Il combine une vulnerabilite associee a l'eau, a l'assainissement et a l'hygiene. Il doit donc etre interprete comme un proxy sanitaire.

Deux consequences directes pour le projet :

- la mortalite WASH sert a enrichir la priorisation mais ne prouve pas a elle seule l'effet de l'eau potable ;
- la table de mortalite n'etant disponible que pour 2016, elle doit etre utilisee comme un snapshot de reference et non comme une serie temporelle.
- le taux de mortalite WASH pour 100000 habitants peut etre decimal, car il s'agit d'un taux standardise et non d'un comptage de personnes ;
- le nombre de deces WASH peut lui aussi etre decimal, car la source sanitaire fournit une estimation statistique modelisee de la charge de mortalite et non un decompte administratif exhaustif.

## 3.bis Enrichissement geographique analytique

Les mesures du projet restent conservees telles quelles a partir des sources officielles. En revanche, la dimension geographique peut etre enrichie pour ameliorer la lecture du dashboard sans modifier les valeurs sources.

Cela signifie que les indicateurs eau, population, stabilite politique et WASH ne sont pas recalcules. Ce qui est enrichi, c'est uniquement le referentiel descriptif des pays :

- code `ISO3` pour fiabiliser les jointures ;
- libelle pays en anglais et en francais ;
- macro-region OMS (`region_oms`) conservee comme niveau source ;
- continent ;
- sous-region ONU (`sous_region_onu`) pour une lecture plus fine de type Afrique de l'Ouest, Afrique de l'Est, Amerique du Nord ou Amerique du Sud.

Cette distinction est importante : on ne corrige pas les chiffres sources, mais on ameliore l'axe geographique de lecture. Les aggregations par continent ou sous-region restent donc des regroupements analytiques construits a partir de mesures pays officielles.

Formulation courte possible : nous avons conserve les territoires disposant de donnees et enrichi uniquement leur classification geographique pour ne pas perdre d'information analytique.

## 4. Logique de lecture des domaines metier

### Domaine 1 - Creation de services

Le besoin principal est d'identifier les pays ou l'acces a l'eau potable est faible et ou la structure spatiale de la population rend le deploiement plus ou moins complexe. La part urbaine et la part rurale changent fortement la nature de l'effort d'infrastructure.

### Domaine 2 - Modernisation des services

Le besoin principal est d'identifier les pays qui disposent deja d'un service basique, mais dont la qualite reste insuffisante. L'ecart entre "basic" et "safely managed" devient alors un indicateur utile de modernisation.

### Domaine 3 - Consulting et gouvernance

Le besoin principal est d'identifier les pays ou la performance observable en matiere d'acces a l'eau reste faible alors que la stabilite politique conditionne fortement la possibilite d'agir avec les institutions publiques.

## 5. Structure recommandee du glossaire

Je te recommande d'utiliser la structure suivante dans ton memoire, ton notebook ou un onglet de documentation :

| Champ | Usage |
|---|---|
| Titre | Nom lisible de l'indicateur |
| Variable projet | Nom technique dans le pipeline ou le dataset |
| Unite de mesure | %, habitants, indice, deces, etc. |
| Donnees sources | Fichier ou table utilisee dans le projet |
| Source originale | Institution productrice de la donnee |
| Concepts et definitions statistiques | Ce que mesure exactement l'indicateur |
| Pertinence projet | Pourquoi on l'utilise dans le dashboard |
| Couverture temporelle | Periode disponible |
| Couverture geographique | Pays / regions couverts |
| Relation a la vulnerabilite | Signe + si l'indicateur augmente la vulnerabilite, signe - s'il la reduit |
| Limites | Principale precaution d'interpretation |

## 6. Sources recommandees pour citer les donnees

### Stabilite politique

- Banque mondiale, Worldwide Governance Indicators
- URL de reference : http://info.worldbank.org/governance/wgi/Home/FAQ
- Definition utile : la stabilite politique et l'absence de violence mesurent la probabilite percue que le gouvernement soit destabilise ou renverse par des moyens anticonstitutionnels ou violents.

### Services d'eau potable

- WHO / UNICEF Joint Monitoring Programme for Water Supply, Sanitation and Hygiene
- URL de reference : https://washdata.org/monitoring/drinking-water
- Definitions utiles :
  - basic drinking-water service = source amelioree avec un temps de collecte inferieur ou egal a 30 minutes aller-retour ;
  - safely managed drinking-water service = source amelioree accessible sur place, disponible au besoin et exempte de contamination.

### Population

- United Nations, Department of Economic and Social Affairs, Population Division
- URL de reference : https://population.un.org/wpp/
- Definition utile : estimations et projections officielles de population par pays, fondees sur recensements, registres et enquetes nationales.

### Mortalite attribuee aux services WASH non surs

- Source institutionnelle a citer prudemment comme source sanitaire internationale de type WHO / GHO selon le jeu de donnees utilise
- Interpretation projet : indicateur de vulnerabilite sanitaire associee a des conditions WASH non sures
- Precaution : dans ce projet, la couverture exploitable est limitee a 2016
- Precision sur les decimales : `mortalite_wash_pour_100k` est un taux par 100000 habitants, donc une valeur decimale est normale ; `deces_wash` correspond a un nombre de deces estime, qui peut lui aussi rester decimal sans contradiction methodologique
