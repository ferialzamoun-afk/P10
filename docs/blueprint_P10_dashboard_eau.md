# Blueprint P10 - Dashboard Eau, Population et Gouvernance

## 1. Blueprint complet

| Besoin utilisateurs | Mesures specifiques a utiliser | Visualisation | Page/Onglet/Vue |
|---|---|---|---|
| Voir l'evolution de la population rurale par pays vs la population totale | Population rurale, population totale, part de population rurale (%) | Line plot a 2 series | Page 3 - Vue nationale |
| Comprendre la stabilite politique dans le monde | Stabilite politique par pays, moyenne de stabilite politique par continent | Carte du monde choroplethe | Page 1 - Vue mondiale et continentale |
| Comprendre la stabilite politique par continent | Moyenne de stabilite politique par continent, nombre de pays, minimum et maximum | Bar chart horizontal classe par continent | Page 1 - Vue mondiale et continentale |
| Indicateur : Domaine 1 (creation de services) | Taux d'acces a l'eau potable, taux de population urbaine, population totale, score_creation_services | Scatter plot | Page 2 - Domaines metier |
| Indicateur : Domaine 1 (structure urbaine / rurale) | Part de population urbaine, part de population rurale | Percent stacked barplot | Page 2 - Domaines metier |
| Indicateur : Domaine 2 (modernisation des services) | Service basique, service safely managed, ecart basique - safely managed, score_modernisation_services | Grouped barplot | Page 2 - Domaines metier |
| Indicateur : Domaine 3 (gouvernance) | Stabilite politique, proxy efficacite politique eau, mortalite WASH pour 100k, score_gouvernance | Scatter plot avec quadrants | Page 2 - Domaines metier |
| Le nombre de morts a cause de l'eau insalubre | deces_wash, mortalite_wash_pour_100k | Carte du monde + bar chart Top N pays | Page 1 - Vue mondiale et continentale |
| Localiser les pays les plus exposes a la vulnerabilite sanitaire WASH | mortalite_wash_pour_100k, deces_wash, acces_eau_potable_pct | Carte du monde choroplethe | Page 1 - Vue mondiale et continentale |
| Identifier les pays prioritaires pour l'action publique | score_creation_services, score_modernisation_services, score_gouvernance, action_prioritaire, population totale | Tableau de priorisation avec mise en forme conditionnelle | Page 3 - Vue nationale |
| Explorer un pays dans le detail | Population totale, population rurale, acces a l'eau potable, service safely managed, stabilite politique, action prioritaire | KPI cards + line plot + tableau detaille | Page 3 - Vue nationale |

## 2. Version orientee Power BI

### Logique generale des 3 pages

Le dashboard peut rester limite a 3 pages tout en couvrant les 3 niveaux de lecture demandes :

1. une lecture `mondiale` pour situer les disparites geographiques ;
2. une lecture `continentale` par agregations et filtres regionaux sur cette meme page ;
3. une lecture `nationale` sur une page dediee au pays selectionne.

La cle pour integrer les visualisations de facon transverse est de ne pas creer une page par echelle geographique. Il vaut mieux creer :

- une page 1 qui supporte simultanement la vue mondiale et la comparaison continentale ;
- une page 2 centree sur les 3 domaines metier, avec des filtres region / annee / action ;
- une page 3 dediee au zoom pays, pilotee par un slicer pays ou par drillthrough.

### Page 1 - Vue mondiale et continentale

**Objectif**

Donner une lecture immediate des disparites mondiales sur l'eau, la ruralite, la mortalite WASH et la stabilite politique, puis permettre une lecture continentale sans changer de page.

**Visuels recommandes**

| Visuel | Mesures / champs | Usage |
|---|---|---|
| Carte du monde choroplethe | Stabilite politique par pays ou mortalite_wash_pour_100k par pays | Voir les zones les plus fragiles |
| Cartes KPI | Moyenne acces a l'eau potable, moyenne stabilite politique, population rurale totale, deces_wash | Resumer la situation globale |
| Bar chart par continent | Moyenne stabilite politique, moyenne acces a l'eau potable, moyenne mortalite WASH pour 100k | Comparer les continents |
| Top N pays | deces_wash ou score_gouvernance | Faire le lien entre vue mondiale et priorisation |
| Segmentations | Annee, region, action prioritaire | Filtrer toute la page |

### Page 2 - Domaines metier

**Objectif**

Porter les 3 analyses metier demandees dans le projet : creation de services, modernisation des services, gouvernance.

**Visuels recommandes**

| Visuel | Mesures / champs | Usage |
|---|---|---|
| Scatter plot - Domaine 1 | acces_eau_potable_pct vs part_urbaine, taille = population_totale, couleur = region | Identifier les besoins de creation de services |
| Percent stacked barplot - Domaine 1 | part urbaine vs part rurale | Lire la structure des pays prioritaires |
| Grouped barplot - Domaine 2 | service basique vs service safely managed | Identifier les besoins de modernisation |
| Scatter plot - Domaine 3 | stabilite_politique vs proxy efficacite politique eau | Prioriser la gouvernance |
| Carte choroplethe de soutien | score_gouvernance ou mortalite_wash_pour_100k | Replacer les resultats dans l'espace |
| Segmentations | Annee, region, action prioritaire, seuil de population | Filtrer toute la page |

### Page 3 - Vue nationale

**Objectif**

Analyser un pays en detail avec une lecture temporelle et contextuelle, puis relier ce pays a l'une des 3 logiques d'action.

**Visuels recommandes**

| Visuel | Mesures / champs | Usage |
|---|---|---|
| KPI | Population totale, population rurale, part rurale, acces a l'eau potable, stabilite politique, action prioritaire | Lecture rapide du pays selectionne |
| Line plot | Population rurale vs population totale par annee | Voir l'evolution demographique |
| Line plot ou courbe | acces_eau_potable_pct et service_safely_managed_pct par annee | Lire la trajectoire de service |
| Tableau detaille | annee, population, eau, stabilite, scores | Support d'analyse fine |
| Segmentations | Pays, annee | Navigation principale |

### Mise en oeuvre transverse des vues mondiale, continentale et nationale

Pour t'assurer d'avoir une lecture `mondiale`, `continentale` et `nationale` sans disperser les visuels, tu peux utiliser l'architecture suivante :

| Niveau de lecture | Comment l'obtenir dans Power BI | Visuels principalement concernes |
|---|---|---|
| Mondial | Aucun filtre geographique actif, carte au niveau pays, KPI globaux | Carte du monde, KPI globaux, Top N pays |
| Continental | Slicer `region` ou clic sur un continent / groupe dans un bar chart | Bar chart continent, scatter plots filtres, KPI filtres |
| National | Slicer `pays` ou drillthrough depuis la carte / un tableau | Page 3 complete |

Bonnes pratiques de construction :

1. utiliser `region` comme filtre transverse present sur les pages 1 et 2 ;
2. utiliser `pays` seulement sur la page nationale pour ne pas surcharger les pages globales ;
3. activer les interactions entre carte, bar chart continent et tableaux pour passer naturellement du mondial au continental ;
4. utiliser un `drillthrough pays` depuis la carte ou le ranking pour ouvrir la page nationale ;
5. garder les memes couleurs par domaine d'action sur toutes les pages pour renforcer la coherence visuelle.

## 3. Mesures metier conseillees pour Power BI

| Mesure | Definition utile |
|---|---|
| Part population rurale (%) | Population rurale / Population totale |
| Variation annuelle population rurale (%) | (Population rurale annee N - Population rurale annee N-1) / Population rurale annee N-1 |
| Moyenne stabilite politique continent | Moyenne de l'indicateur par continent |
| Taux de mortalite eau insalubre | Deces eau insalubre / Population totale * 100000 |
| Ecart eau vs urbanisation | Taux acces eau potable - Taux population urbaine |
| Score de priorite | Combinaison ponderee : forte mortalite + faible acces a l'eau + faible stabilite politique + forte part rurale |

## 4. Contraintes Techniques A Integrer Dans Power BI

### Types de visuels a respecter

| Exigence | Implementation recommandee dans le dashboard |
|---|---|
| `line plot` | Evolution moyenne regionale de l'acces a l'eau potable et de la stabilite politique dans le temps ; evolution population rurale vs population totale sur la page nationale |
| `scatter plot` | Domaine 1 : acces a l'eau potable vs part de population urbaine ; Domaine 3 : stabilite politique vs proxy d'efficacite politique eau |
| `grouped barplot` | Domaine 2 : comparaison entre services basiques et services safely managed par pays |
| `stacked barplot` ou `percent stacked barplot` | Structure urbaine vs rurale des pays prioritaires pour la creation de services |
| Representation temporelle | Vue 2010-2018 sur les indicateurs eau et stabilite politique |
| Representation geographique | Carte choroplethe mondiale sur le score de gouvernance, la stabilite politique ou la mortalite WASH 2016 |

### Filtres minimum a prevoir

| Type de filtre | Champ recommande |
|---|---|
| Filtre quantitatif | Population totale en millions ou seuil de score |
| Filtre qualitatif | Action prioritaire ou type de domaine |
| Filtre temporel | Annee |
| Filtre geographique | Region |

### Calculs et transformations indispensables

| Contrainte | Implementation recommandee |
|---|---|
| Agregation | Moyennes regionales par annee pour les line plots |
| Champ calcule | Conversion de la population en habitants ou en millions |
| Champ calcule | Part urbaine = `100 - part rurale` |
| Champ calcule | Ecart de qualite de service = `basic - safely managed` |
| Champ calcule | Proxy efficacite politique eau = `acces a l'eau potable - mortalite WASH` |
| Jointure | `dashboard_water_country_year.csv` avec `country_region_reference.csv` si besoin de reconstituer ou securiser la region |

### Limite de donnees a rendre explicite

La mortalite WASH n'est disponible qu'en `2016`. Elle doit donc etre utilisee comme un `snapshot de reference` pour la priorisation, et non comme une vraie serie temporelle. Les courbes temporelles doivent reposer d'abord sur la population, l'acces a l'eau potable et la stabilite politique. En consequence, `deces_wash` et `mortalite_wash_pour_100k` doivent etre portes principalement par des cartes, KPI, bar charts et tableaux de priorisation, pas par des line plots historiques.

### Accessibilite et lisibilite

| Critere | Recommandation |
|---|---|
| Contraste | Utiliser des palettes lisibles et non ambiguës, eviter les couleurs trop proches |
| Libelles | Afficher des titres explicites avec unites (%) / habitants / index |
| Charge visuelle | Limiter les Top N affiches pour garder une lecture soutenable |
| Cadrage | Utiliser des axes bornes de 0 a 100 pour les pourcentages quand c'est pertinent |
| Storytelling | Un visuel principal par message, puis un visuel secondaire de justification |

### Optimisation du modele de donnees

| Objectif | Recommandation |
|---|---|
| Vitesse d'affichage | Charger en priorite les marts prepares plutot que de recalculer dans chaque visuel |
| Simplicite | Utiliser une table large pays-annee pour les analyses principales |
| Reutilisabilite | Garder la table longue normalisee pour les explorations ou extensions futures |
| Robustesse | Centraliser les champs calcules critiques dans Power Query ou dans le modele |
| Clarte | Adapter la complexite des visuels a l'auditoire, sans multiplier les couches d'analyse simultanees |

## 5. Recommandation de lecture pour la soutenance

1. Commencer par la page 1 en vue mondiale pour cadrer les disparites.
2. Utiliser la meme page 1 en lecture continentale via le filtre region.
3. Passer a la page 2 pour montrer les 3 domaines metier et les visuels imposes.
4. Ouvrir enfin la page 3 pour raconter un cas pays en detail.
5. Conclure sur l'action prioritaire et la limite methodologique WASH 2016.

## 6. Version soutenance synthétique

### Message central

Le dashboard doit montrer que les priorites d'action sur l'eau ne se lisent pas avec un seul indicateur. Elles se construisent en croisant exposition sanitaire, capacite de service, structure territoriale de la population et faisabilite institutionnelle.

### Structure de narration recommandee

| Etape | Message a faire passer | Visuel principal | Visuel de soutien |
|---|---|---|---|
| 1 | Le probleme est mondial mais heterogene | Carte du monde | KPI globaux |
| 2 | Les continents n'ont pas le meme niveau de fragilite | Bar chart par continent | Top N pays |
| 3 | Les besoins metier ne sont pas de meme nature | Scatter Domaine 1, Grouped barplot Domaine 2, Scatter Domaine 3 | Carte de soutien |
| 4 | Un pays doit etre lu dans sa trajectoire propre | Page nationale avec KPI + line plots | Tableau detaille |
| 5 | La recommandation finale depend d'une priorisation argumentee | Tableau de priorisation | Action prioritaire dominante |

### Formulation courte pour presenter le dashboard

"Le dashboard s'organise en trois niveaux de lecture. La page 1 cadre les disparites mondiales et continentales. La page 2 compare les trois logiques d'action possibles : creation de services, modernisation des services et conseils de gouvernance. La page 3 zoome sur un pays pour transformer l'analyse globale en recommandation concrete."

### Point methodologique a dire a l'oral

"La mortalite WASH est utilisee comme signal sanitaire de reference, mais uniquement en snapshot 2016. Elle enrichit la priorisation sans pretendre decrire une evolution temporelle complete ni mesurer l'eau potable seule."

## 7. Contenu exact des 3 pages

### Page 1 - Vue mondiale et continentale

**Objectif de page**

Installer le contexte global, puis permettre une lecture regionale sans changer d'ecran.

**Organisation recommandee**

| Zone | Visuel | Champs / mesures | Role |
|---|---|---|---|
| Bandeau haut | 4 KPI cards | Population totale, Acces eau potable % moyen, Stabilite politique moyenne, Deces WASH estimes | Donner le niveau global |
| Centre gauche | Carte du monde choroplethe | pays + stabilite_politique ou mortalite_wash_pour_100k | Localiser les fragilites |
| Centre droit | Bar chart horizontal par continent | region + moyenne stabilite politique ou moyenne acces eau potable | Passer du mondial au continental |
| Bas gauche | Top N pays | pays + deces_wash ou score_gouvernance | Identifier les pays les plus critiques |
| Bas droit | Tableau de synthese | region, nb pays, moyennes principales | Justifier la lecture regionale |
| Filtres | Slicers | annee, region, action_prioritaire | Rendre la page interactive |

**Lecture attendue**

1. sans filtre, la page raconte la situation mondiale ;
2. avec un filtre `region`, elle devient une vue continentale ;
3. avec clic sur un pays de la carte ou du Top N, elle prepare l'entree vers la page nationale.

### Page 2 - Domaines metier

**Objectif de page**

Comparer clairement les trois types de reponse possibles : creer, moderniser, gouverner.

**Organisation recommandee**

| Bloc | Visuel | Champs / mesures | Role |
|---|---|---|---|
| Bloc 1 | Scatter plot Domaine 1 | part urbaine, acces_eau_potable_pct, population_totale, region | Montrer les besoins de creation de services |
| Bloc 1 bis | Percent stacked barplot | part urbaine, part rurale, pays | Qualifier la structure territoriale |
| Bloc 2 | Grouped barplot Domaine 2 | acces_eau_potable_pct, service_safely_managed_pct, pays | Mesurer le besoin de modernisation |
| Bloc 3 | Scatter plot Domaine 3 | stabilite_politique, proxy efficacite politique eau, mortalite_wash_pour_100k | Lire la priorite gouvernance |
| Bloc transversal | Carte choroplethe de soutien | score_gouvernance ou mortalite_wash_pour_100k | Replacer les signaux dans l'espace |
| Filtres | Slicers | annee, region, action_prioritaire, seuil de population | Filtrer les 3 domaines simultanement |

**Lecture attendue**

1. Domaine 1 repond a la question : ou faut-il etendre ou creer les services ?
2. Domaine 2 repond a la question : ou faut-il surtout ameliorer la qualite d'un service deja present ?
3. Domaine 3 repond a la question : ou l'enjeu principal devient-il institutionnel et politique ?

### Page 3 - Vue nationale

**Objectif de page**

Passer d'une lecture globale a un diagnostic pays exploitable dans la recommandation finale.

**Organisation recommandee**

| Zone | Visuel | Champs / mesures | Role |
|---|---|---|---|
| Bandeau haut | KPI cards | Population totale, Population rurale, Part rurale, Acces eau potable, Stabilite politique, Action prioritaire | Donner la fiche d'identite du pays |
| Centre haut | Line plot | population_rurale et population_totale par annee | Lire la dynamique demographique |
| Centre bas gauche | Line plot | acces_eau_potable_pct et service_safely_managed_pct par annee | Lire la trajectoire de service |
| Centre bas droit | Bar chart ou carte miniature | scores_creation / modernisation / gouvernance | Voir la logique d'action dominante |
| Bas | Tableau detaille | annee, population, eau, stabilite, scores, action_prioritaire | Justifier le diagnostic |
| Filtres | Slicers | pays, annee | Piloter l'analyse du cas national |

**Lecture attendue**

1. selection d'un pays depuis un slicer ou un drillthrough ;
2. lecture du profil de population et de service ;
3. interpretation de l'action prioritaire dominante ;
4. conclusion par recommandation pays.

### Ordre de construction conseille dans Power BI

1. construire la page 1 en premier, car elle fixe les filtres et les interactions globales ;
2. construire ensuite la page 2, car elle porte les visuels imposes du brief ;
3. terminer par la page 3, qui depend du pays selectionne et du drillthrough.