# Presentation P10 - DWFA (version document)

## 1. Objet de la presentation
Cette presentation explique la demarche data-driven mise en place pour aider DWFA a prioriser ses interventions sur l'acces a l'eau potable. Elle couvre le contexte, le pretraitement des donnees, le blueprint du dashboard et la justification de l'outil de visualisation retenu.

## 2. Elements de contexte
DWFA intervient sur trois domaines d'action complementaires:
- creation de services d'eau potable,
- modernisation des services existants,
- consulting en gouvernance publique de l'eau.

Le besoin metier est de transformer une demande de financement en decision ciblee: quel pays prioriser, et pour quel type d'action.

Le projet P10 repose sur une logique multi-echelles:
- vue mondiale pour cadrer les disparites,
- vue continentale pour comparer les profils regionaux,
- vue nationale pour produire une recommandation pays argumentee.

La priorisation ne repose pas sur un indicateur unique. Elle croise:
- acces a l'eau,
- mortalite WASH,
- stabilite politique,
- structure demographique (rural/urbain),
- faisabilite institutionnelle.

## 3. Pretraitement des donnees
### 3.1 Sources mobilisees
Les donnees sont issues de cinq jeux principaux:
- acces a l'eau (basic et safely managed),
- mortalite attribuee au WASH,
- population,
- stabilite politique,
- referentiel pays/regions.

### 3.2 Controles qualite
Les controles realises avant modelisation:
- verification des schemas et des types,
- harmonisation des noms de pays et des codes,
- controle des doublons,
- controle des valeurs manquantes,
- verification de la granularite pays-annee,
- verification des unites (notamment population).

### 3.3 Transformations metier
Les transformations principales:
- normalisation des dimensions (pays, annee, region),
- enrichissement geographique (continent, sous-region),
- construction d'indicateurs derives (ecarts de service, part rurale),
- calcul de trois scores metier:
  - score creation,
  - score modernisation,
  - score gouvernance,
- attribution d'une action prioritaire selon le score dominant.

### 3.4 Structuration pour la BI
Le modele final est structure en etoile pour Power BI:
- une table de faits analytique,
- des dimensions dediees (pays, annee, date, action, region),
- exports FR/EN pour faciliter analyse et communication.

### 3.5 Arbitrages et limites documentees
- mortalite WASH exploitee en snapshot 2016,
- filtre population pour eviter les biais des micro-etats,
- regles explicites sur exclusions/qualite de couverture,
- tracabilite des champs sources vs champs calcules.

## 4. Captures d'ecran du blueprint

Tu peux utiliser ce bloc tel quel dans une slide ou un document, puis faire une capture ecran.

| Besoin utilisateur | Mesures mobilisees | Visualisation retenue | Niveau de lecture |
|---|---|---|---|
| Situer les disparites globales eau/sante | acces_eau_potable_pct, mortalite_wash_pour_100k, deces_wash | carte mondiale + KPI | mondial |
| Comparer les continents | moyenne stabilite, moyenne acces eau, deces WASH estimes | barplot regional + line plot stabilite | continental |
| Identifier les pays actionnables | score_creation, score_modernisation, score_gouvernance, score_final | tableau de priorisation | continental/national |
| Expliquer la recommandation pays | domaine dominant, score final, contexte rural/urbain, stabilite | fiche nationale + texte d'explication | national |
| Piloter la decision financeur | nb pays eligibles, nb recommandables, score final moyen | KPI cards + tableau filtre | continental |

Regle de lecture du blueprint:
- mondial pour cadrer,
- continental pour prioriser,
- national pour decider.

Logique decisionnelle:
- un pays peut etre pre-selectionne techniquement,
- la recommandation finale reste un arbitrage metier explicite,
- l'outil aide la decision, il ne remplace pas la decision.

### Capture 1 - Vue mondiale (Page 1)
Legende proposee:
"La vue mondiale fournit une lecture macro des disparites eau-sante-gouvernance. Les KPI de tete de page cadrent l'etat global et la carte choroplethe localise les zones de fragilite."

A inserer:
- screenshot page mondiale avec KPI + carte + courbe stabilite.

### Capture 2 - Vue continentale (Page 1 filtre region actif)
Legende proposee:
"La meme page devient une vue continentale via le filtre region. Cette approche conserve la continuite de lecture entre mondial et continental sans rupture de navigation."

A inserer:
- screenshot avec region filtree et visuels compares par continent.

### Capture 3 - Vue nationale (Drillthrough pays)
Legende proposee:
"La fiche nationale transforme l'analyse globale en diagnostic pays actionnable, avec indicateurs cle, tendance temporelle et recommandation metier."

A inserer:
- screenshot de la page nationale pour un pays exemple.

### Capture 4 - Page Domaines metier
Legende proposee:
"Les visualisations metier distinguent trois logiques d'action: creer, moderniser, gouverner. Le croisement des variables rend explicite le type d'intervention prioritaire."

A inserer:
- screenshot de la page domaines avec scatter + barres groupees.


## 4.ter Mesures de la page continentale (a commenter en presentation)
### Mesure 1 - Nb de pays eligibles
Definition:
- nombre de pays qui respectent les criteres de base (perimetre, donnees disponibles, regles de filtrage actives).

Lecture metier:
- c'est le vivier de decision.
- si ce nombre baisse fortement apres un filtre, on explique l'impact du filtre plutot que de conclure trop vite.

### Mesure 2 - Nb de pays recommandables
Definition:
- nombre de pays eligibles dont le score final depasse le seuil retenu par la gouvernance du projet.

Lecture metier:
- c'est le sous-ensemble actionnable a court terme.
- ce nombre n'est pas fixe: il evolue avec les seuils, les filtres et les nouvelles donnees.

### Mesure 3 - Nb de pays affiches (tableau)
Definition:
- nombre de lignes effectivement visibles dans le tableau de priorisation apres interactions (slicers, clic carte, filtres visuels).

Lecture metier:
- c'est un indicateur de controle de contexte.
- il permet d'eviter les erreurs d'interpretation quand la table est filtree sans que l'utilisateur s'en rende compte.

### Mesure 4 - Score final moyen eligibles
Definition:
- moyenne du score final sur les pays eligibles dans le contexte de filtre courant.

Lecture metier:
- sert a mesurer la pression moyenne de priorite du portefeuille visible.
- utile pour comparer les regions entre elles a perimetre equivalent.

### Mesure 5 - Domaine metier maximum recommande
Definition:
- domaine dominant (creation, modernisation, gouvernance) selon le score maximal agrege dans le contexte actif.

Lecture metier:
- donne l'orientation principale de l'action a financer.
- ne doit pas masquer les cas particuliers pays qui peuvent relever d'un autre domaine.
### Capture 5 - Tableau de priorisation
Legende proposee:
"Le tableau de priorisation consolide les scores et permet une decision transparente, comparable et defendable face aux parties prenantes."

A inserer:
- screenshot du tableau final de pre-selection/selection.

## 6. Choix metier et amelioration continue du score final
Point cle a dire explicitement:
- la recommandation du dashboard est une aide a la decision,
- le choix final demeure un choix metier assume par l'equipe DWFA.

Pourquoi ce point est important:
- les scores sont sensibles a la qualite des donnees,
- certains indicateurs sont des proxies,
- un pays peut etre strategique meme avec un score intermediaire.

Demarche d'amelioration continue proposee:
1. Recalculer les mesures a chaque refresh de donnees.
2. Suivre les ecarts entre pre-selection technique et selection finale metier.
3. Analyser les cas de desaccord (ex: pays peu prioritaire selon score mais retenu pour faisabilite/partenariat).
4. Ajuster de facon tracee les seuils et ponderations du score final.
5. Documenter chaque arbitrage dans un motif de decision lisible dans le tableau final.

Formulation prete a l'oral:
"Le score final structure une priorisation objective et reactive, mais la decision finale reste metier. Nous l'ameliorons en continu a partir des nouvelles donnees, des retours terrain et des arbitrages documentes."

## 5. Justification de la pertinence de l'outil de visualisation retenu (Power BI)
Power BI est pertinent pour ce projet pour cinq raisons principales.

### 5.1 Modele de donnees robuste
Le modele en etoile (faits + dimensions) garantit:
- des calculs coherents,
- une bonne performance d'affichage,
- une maintenance plus simple du schema analytique.

### 5.2 Interactivite orientee decision
Les slicers (annee, region, stabilite, efficience, action) permettent:
- une exploration autonome par des profils non techniques,
- une lecture multi-niveaux (mondial, continental, national),
- des arbitrages rapides en reunion.

### 5.3 Capacite de narration analytique
Power BI facilite un storytelling progressif:
- cadrage global,
- comparaison regionale,
- zoom pays,
- justification de la recommandation finale.

### 5.4 DAX et regles metier explicites
Les mesures DAX permettent de formaliser:
- les seuils d'alerte,
- les scores de priorisation,
- les badges de statut,
- les regles de selection finale.

La logique decisionnelle devient auditable et mise a jour automatiquement a chaque refresh.

### 5.5 Integrabilite avec le pipeline existant
Le projet dispose deja d'un pipeline notebooks/scripts qui publie des CSV propres vers la couche pbi_star. Power BI s'integre donc sans rupture:
- flux reproductible,
- mises a jour rapides,
- industrialisation possible.

## 6. Conclusion
Le dashboard P10 ne se limite pas a visualiser des indicateurs: il structure une decision d'allocation d'effort publique.

La combinaison contexte + pretraitement robuste + blueprint coherent + interactivite Power BI produit un outil pertinent pour prioriser l'action DWFA avec transparence, reactivite et rigueur methodologique.

## 7. Version slide-ready (1 page)
### 7.1 Contexte
- DWFA doit prioriser un pays et un domaine d'intervention pour l'acces a l'eau potable.
- Trois domaines: creation de services, modernisation, gouvernance.
- Objectif: passer d'une lecture globale a une decision pays argumentee.

### 7.2 Pretraitement des donnees
- Collecte multi-sources: eau, WASH, population, stabilite politique, referentiel pays.
- Controles qualite: types, doublons, valeurs manquantes, granularite pays-annee, unites.
- Transformations: harmonisation pays/regions, variables derivees, scores metier, action prioritaire.
- Structuration BI: modele en etoile (faits + dimensions) pour performance et coherence des calculs.

### 7.3 Blueprint (lecture macro -> micro)
| Niveau | Question | Visuels cles | Resultat attendu |
|---|---|---|---|
| Mondial | Ou sont les fragilites globales ? | KPI + carte choroplethe + tendances | Cadrage strategique |
| Continental | Quels profils regionaux prioriser ? | comparatifs regionaux + tableau filtre | Priorisation portefeuille |
| National | Que recommander pour un pays ? | fiche pays + scores + explication | Decision actionnable |

### 7.4 Mesures continentales a presenter
- Nb de pays eligibles: vivier de decision apres filtres et regles de qualite.
- Nb de pays recommandables: pays au-dessus du seuil de score final.
- Nb de pays affiches (table): controle du contexte reel de lecture.
- Score final moyen eligibles: niveau moyen de priorite du portefeuille visible.
- Domaine metier maximum recommande: orientation dominante (creer/moderniser/gouverner).

### 7.5 Message metier cle
- Le score final rend la priorisation plus objective et reactive.
- La recommandation du dashboard est une aide a la decision.
- Le choix final reste un choix metier, documente et assume.

### 7.6 Amelioration continue du score final
1. Recalcul a chaque actualisation des donnees.
2. Suivi des ecarts entre pre-selection technique et selection finale metier.
3. Analyse des cas atypiques et arbitrages documentes.
4. Ajustement trace des seuils et ponderations.
5. Stabilisation progressive du modele de priorisation.

Formule de conclusion prete a presenter:
"Le score final guide la priorisation en temps reel, mais la decision demeure metier. Notre demarche d'amelioration continue garantit une priorisation robuste, explicable et adaptable aux nouvelles donnees."
