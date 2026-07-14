# Questions pieges - Soutenance P10

## Comment utiliser cette fiche

Cette fiche prepare des reponses courtes, defensables et coherentes avec la presentation. L'objectif n'est pas de reciter un texte, mais de garder une ligne claire : distinguer ce qui est etabli par les donnees, ce qui releve des choix methodologiques, et ce qui reste un arbitrage metier.

## 1. Questions pieges sur le cadrage du projet

### Pourquoi ne pas avoir utilise un seul indicateur pour prioriser les pays ?

Un seul indicateur aurait donne une lecture reductrice du besoin. La priorisation croise ici l'acces a l'eau, la vulnerabilite sanitaire WASH, la structure rurale ou urbaine et la stabilite politique pour approcher des situations reellement actionnables.

### Quel est le vrai probleme que ce projet cherche a resoudre ?

Le projet cherche a transformer une masse de donnees heterogenes en aide a la decision. L'enjeu n'est pas seulement de visualiser des indicateurs, mais d'aider a choisir dans quel pays agir et selon quel type d'intervention.

### Pourquoi avoir structure la lecture en mondial, continental puis national ?

Parce que la decision ne se prend pas au meme niveau d'analyse. Le mondial sert a cadrer les disparites, le continental a comparer les profils regionaux, et le national a produire une recommandation pays argumentee.

## 2. Questions pieges sur DWFA

### La DWFA existe-t-elle reellement ?

Dans le cadre du projet, la DWFA est l'organisation de reference qui structure le cas metier. Mon travail portait sur la logique d'aide a la decision et sur la fiabilisation des donnees, pas sur une enquete institutionnelle sur l'organisation elle-meme.

### Quelle est la date de creation de la DWFA ?

Je n'ai pas retenu de date de creation verifiable par source officielle fiable. Ce point n'etait pas le coeur du projet, qui portait sur la construction d'un outil de priorisation fonde sur les donnees.

### Qui gouverne la DWFA en 2026 ?

Je ne peux pas avancer de gouvernance nominative sans source officielle. Dans le projet, la gouvernance apparait surtout comme un niveau metier qui arbitre la decision finale a partir des signaux produits par le dashboard.

### Quels sont les faits d'armes de la DWFA ?

Je ne presenterais pas de realisations historiques non verifiees. En revanche, dans le projet, la DWFA est definie par trois champs d'action complementaires : creer des services, moderniser les services existants et accompagner la gouvernance publique de l'eau.

## 3. Questions pieges sur les donnees

### Pourquoi avoir choisi ces sources de donnees ?

Parce qu'elles couvrent les dimensions essentielles du probleme avec des sources institutionnelles reconnues : acces a l'eau, mortalite WASH, population, stabilite politique et referentiel pays ou regions. Le choix des sources suit la logique metier du projet.

### Les donnees sont-elles vraiment comparables entre pays ?

Elles le deviennent apres harmonisation des noms, des cles, des types, des granularites et des unites. La comparabilite n'est pas parfaite par nature, mais elle a ete renforcee par le nettoyage et les regles explicites de preparation.

### Pourquoi la mortalite WASH n'est-elle disponible qu'en 2016 ?

Parce que c'est la couverture exploitable du jeu de donnees retenu dans le projet. Elle est donc utilisee comme un snapshot de reference pour enrichir la priorisation, et non comme une serie temporelle continue.

### Est-ce que l'indicateur WASH mesure l'eau potable uniquement ?

Non. C'est un proxy sanitaire plus large, lie a l'eau, a l'assainissement et a l'hygiene. Il enrichit la lecture de vulnerabilite, mais ne doit pas etre interprete comme une mesure pure de l'eau potable.

### Pourquoi certains nombres de deces ou taux sont-ils decimaux ?

Parce qu'il s'agit d'estimations statistiques ou de taux standardises, pas de comptages administratifs bruts. Une valeur decimale est donc normale dans ce type de source sanitaire.

## 4. Questions pieges sur la methode

### En quoi votre projet est-il vraiment data-driven ?

Il l'est parce que la logique de priorisation part des donnees, suit un pipeline reproductible de controle, d'exploration, de transformation et d'export, puis formalise les regles de lecture dans le dashboard.

### Pourquoi avoir fait une EDA si vous aviez deja le besoin metier ?

Parce qu'un besoin metier ne suffit pas a garantir que les donnees racontent bien ce qu'on croit. L'EDA sert a verifier les distributions, les valeurs manquantes, les outliers et les relations attendues avant de construire un score ou une visualisation.

### Qu'est-ce qui garantit la reproductibilite ?

La reproductibilite repose sur un pipeline notebook ou script, sur des jeux de donnees versionnes dans le projet, et sur une separation claire entre donnees sources, transformations et exports analytiques.

### Pourquoi avoir enrichi la geographie sans toucher aux mesures ?

Parce que l'objectif etait d'ameliorer la lecture analytique sans denaturer les chiffres sources. Les valeurs restent celles des sources officielles ; seul le referentiel descriptif des pays a ete enrichi pour mieux comparer les territoires.

## 5. Questions pieges sur les scores

### Comment justifier l'existence de trois scores differents ?

Parce que les besoins d'action ne sont pas de meme nature. Un pays peut relever d'un deficit d'infrastructure, d'un deficit de qualite de service, ou d'un enjeu institutionnel ; il est donc plus rigoureux de distinguer creation, modernisation et gouvernance.

### Les ponderations des scores ne sont-elles pas arbitraires ?

Elles comportent une part de choix methodologique, oui, mais ce choix est explicite et discutable. L'interet du projet est justement de rendre ces regles visibles, ajustables et auditables plutot que de laisser une priorisation implicite.

### Peut-on dire qu'un score prouve qu'il faut agir dans un pays ?

Non. Le score signale une priorite potentielle dans un cadre donne ; il n'equivaut pas a une preuve causale ni a une decision automatique. Il structure une discussion metier.

### Pourquoi un score final si vous avez deja trois scores metier ?

Le score final permet une vue synthetique pour classer ou filtrer rapidement un portefeuille de pays. Les trois scores metier restent indispensables pour comprendre la nature precise de la recommandation.

### Que faites-vous si le score dit une chose mais le terrain une autre ?

Le terrain prime dans la decision finale. Le dashboard sert a objectiver la preselection, puis les equipes metier peuvent documenter un arbitrage different si la faisabilite, le contexte local ou les partenariats l'exigent.

## 6. Questions pieges sur Power BI

### Pourquoi Power BI et pas un autre outil ?

Power BI est adapte ici parce qu'il articule bien modele de donnees, mesures DAX, filtrage interactif et narration multi-niveaux. Il s'integre aussi directement avec les tables preparees par le pipeline.

### Pourquoi avoir choisi un modele en etoile ?

Parce qu'il ameliore la lisibilite du schema, la coherence des calculs et la performance des requetes. C'est une structure classique et robuste pour la BI.

### Le dashboard n'est-il pas trop complexe pour un decideur non technique ?

Justement, toute la conception cherche a reduire cette complexite. La lecture va du global au detail, les slicers cadrent le contexte, et les indicateurs sont regroupes par usage metier plutot que par logique purement technique.

### Pourquoi garder seulement trois pages ?

Parce qu'au-dela, le risque est de disperser la lecture. Trois pages suffisent ici pour couvrir les trois niveaux de decision sans perdre la coherence du parcours utilisateur.

## 7. Questions pieges sur les limites

### Quelle est la principale limite du projet ?

La principale limite est l'usage de la mortalite WASH en snapshot 2016, qui enrichit fortement la priorisation mais ne permet pas une lecture historique complete de cette dimension sanitaire.

### Peut-on vraiment parler de causalite avec ce dashboard ?

Non. Le dashboard met en evidence des signaux, des rapprochements et des profils de priorite ; il ne demontre pas a lui seul des relations causales.

### Qu'est-ce qui pourrait biaiser la priorisation ?

Les biais peuvent venir de la couverture incomplete de certaines sources, des proxies utilises, des ponderations retenues et de la perte d'information inevitable quand on resume une situation pays par un score.

### Votre recommandation finale est-elle objective ?

Elle est plus objective qu'une lecture intuitive, parce qu'elle repose sur des regles explicites et des donnees tracees. Mais elle ne devient pas neutre ou automatique pour autant ; elle reste un appui a un arbitrage metier.

## 8. Questions pieges sur la valeur du projet

### Quelle est la vraie valeur ajoutee de votre travail ?

La valeur ajoutee est d'avoir transforme des sources heterogenes en un cadre decisionnel lisible, documente et reproductible, capable de soutenir une priorisation transparente.

### Qu'est-ce que le jury doit retenir en une phrase ?

Le projet montre qu'on peut passer d'un ensemble de donnees disparates a une aide a la decision claire pour prioriser l'action sur l'eau potable selon trois logiques : creer, moderniser ou gouverner.

### Si vous aviez une amelioration a faire apres la soutenance, laquelle choisiriez-vous ?

J'approfondirais soit la robustesse du score final par tests de sensibilite sur les ponderations, soit l'enrichissement des donnees sanitaires pour reduire la dependance au snapshot WASH 2016.

## 9. Reponses de secours a reutiliser

### Reponse de prudence

Je prefere distinguer ce qui est etabli par les donnees du projet et ce qui demanderait une validation institutionnelle supplementaire.

### Reponse de recentrage

Ce point est interessant, mais dans le cadre de ce projet, l'enjeu principal etait surtout de construire une priorisation fiable et lisible a partir de donnees heterogenes.

### Reponse sur les limites

Je ne presente pas cela comme une verite absolue, mais comme un cadre d'aide a la decision explicite, traçable et ameliorable.

### Reponse sur l'arbitrage metier

Le dashboard n'a pas vocation a remplacer l'expertise terrain ; il sert a la structurer et a la documenter.

## 10. Mini script final si le jury te pousse

Si je devais resumer ma position, je dirais que ce projet ne pretend pas automatiser une decision complexe. Il propose une methode rigoureuse pour croiser des signaux sanitaires, demographiques, techniques et institutionnels afin d'orienter une decision metier plus transparente.

## 11. Simulation de jury - questions agressives et reponses mot pour mot

### Question 1

**Jury**

Franchement, votre dashboard ne fait que mettre des jolies couleurs sur des donnees deja disponibles. Ou est votre valeur ajoutee ?

**Reponse a dire**

Ma valeur ajoutee n'est pas d'afficher des chiffres bruts, mais de transformer des sources heterogenes en un cadre de decision coherent. J'ai fiabilise les donnees, explicite les regles de lecture, structure trois logiques d'action et rendu la priorisation comparable entre pays.

### Question 2

**Jury**

Votre score final, c'est juste une formule arbitraire. Pourquoi devrait-on lui faire confiance ?

**Reponse a dire**

Je ne demande pas qu'on lui fasse confiance aveuglement. Je propose un score explicite, discutable et auditable, ce qui est plus robuste qu'une priorisation implicite. Le score ne remplace pas le jugement metier, il structure la discussion.

### Question 3

**Jury**

Vous parlez d'aide a la decision, mais en realite vous ne prenez aucune decision. A quoi sert vraiment votre travail ?

**Reponse a dire**

Justement, un bon outil d'aide a la decision n'automatise pas une decision complexe. Il reduit l'arbitraire, clarifie les criteres et permet de justifier pourquoi un pays est prioritaire plutot qu'un autre.

### Question 4

**Jury**

Pourquoi avoir choisi la mortalite WASH si elle n'est meme disponible que sur 2016 ? C'est methodologiquement faible.

**Reponse a dire**

Ce serait faible si je la presentais comme une serie historique complete. Ce n'est pas le cas. Je l'utilise comme un snapshot sanitaire de reference, en annoncant clairement sa limite, pour enrichir la priorisation sans surinterpreter la temporalite.

### Question 5

**Jury**

Donc vous utilisez un proxy imparfait, des ponderations discutables et une gouvernance fictive. Pourquoi votre projet serait-il credible ?

**Reponse a dire**

Il est credible parce qu'il rend visibles ses hypotheses et ses limites. Un projet decisionnel est plus solide quand il expose ses conventions que lorsqu'il laisse croire a une objectivite absolue. Mon travail est defendable parce qu'il est transparent.

### Question 6

**Jury**

Pourquoi ne pas avoir fait un modele predictif ou du machine learning ? Votre approche reste tres descriptive.

**Reponse a dire**

Le besoin du projet etait d'abord de prioriser de facon lisible et explicable. Un modele predictif aurait ajoute de la complexite sans garantir une meilleure decision metier. J'ai privilegie l'interpretabilite, ce qui est plus pertinent ici.

### Question 7

**Jury**

Vous parlez de data-driven, mais on a surtout l'impression que vous avez adapte les donnees a votre histoire.

**Reponse a dire**

J'ai justement cherche a eviter cela en passant par une phase d'inspection, de controle qualite et de documentation des transformations. La narration vient apres les verifications, pas avant.

### Question 8

**Jury**

Pourquoi Power BI ? Ce n'est pas un choix tres original.

**Reponse a dire**

Je n'ai pas cherche l'originalite de l'outil, j'ai cherche l'adequation au besoin. Power BI est pertinent ici pour son modele en etoile, ses mesures DAX, ses filtres interactifs et son integration directe avec le pipeline de donnees.

### Question 9

**Jury**

Si les donnees sont incompletes ou imparfaites, votre priorisation peut etre fausse. Quelle est alors son utilite ?

**Reponse a dire**

Une priorisation imparfaite mais explicite reste plus utile qu'une decision intuitive non tracee. L'objectif n'est pas de supprimer toute incertitude, mais de mieux la cadrer pour prendre une decision plus defendable.

### Question 10

**Jury**

Votre projet ne prouve rien causalement. Pourquoi lui donner une valeur strategique ?

**Reponse a dire**

Parce qu'un outil strategique n'a pas besoin de prouver une causalite totale pour etre utile. Il doit surtout organiser l'information pertinente, faire ressortir les profils de priorite et soutenir un arbitrage plus coherent.

### Question 11

**Jury**

En quoi votre dashboard ferait mieux qu'un simple tableau Excel bien construit ?

**Reponse a dire**

Il fait mieux sur trois points : l'interactivite, la lecture multi-niveaux et la formalisation des regles metier. Le dashboard permet de passer du mondial au pays, de filtrer dynamiquement et d'expliquer visuellement la recommandation.

### Question 12

**Jury**

Vous dites que la decision finale reste humaine. Donc votre score final ne sert pas a grand-chose.

**Reponse a dire**

Au contraire, c'est parce que la decision reste humaine que le score est utile. Il fournit une base commune, objective et discutable, sur laquelle l'expertise terrain peut ensuite arbitrer.

### Question 13

**Jury**

Pourquoi avoir retenu seulement trois domaines d'action ? La realite est plus complexe que cela.

**Reponse a dire**

Bien sur que la realite est plus complexe. Mais un outil de decision doit simplifier sans trahir. Les trois domaines retenus couvrent les grandes logiques d'intervention tout en restant lisibles pour l'utilisateur final.

### Question 14

**Jury**

Si un pays a un mauvais score de stabilite politique, pourquoi investir quand meme dans l'analyse ?

**Reponse a dire**

Parce qu'un faible niveau de stabilite n'annule pas automatiquement le besoin, il change la nature de l'action envisageable. C'est justement l'interet de distinguer creation, modernisation et gouvernance.

### Question 15

**Jury**

Quel est, selon vous, le point le plus fragile de votre projet ?

**Reponse a dire**

Le point le plus fragile est la dependance au snapshot WASH 2016 pour la dimension sanitaire. Je l'assume clairement, et c'est aussi pour cela que je presente le dashboard comme une aide a la decision perfectible, pas comme un verdict automatique.

## 12. Conseils d'oral pour repondre a une question agressive

### Regle 1

Ne conteste pas le ton du jury. Reponds sur le fond, calmement, en une idee principale.

### Regle 2

Commence souvent par reconnaitre la limite, puis retourne-la en preuve de rigueur. Exemple : oui, cette limite existe, et c'est justement pour cela que je l'ai documentee explicitement.

### Regle 3

Ne defends jamais une certitude que tu n'as pas. Defends plutot la transparence de ta methode.

### Regle 4

Si le jury insiste, reviens toujours a cette phrase : le projet ne remplace pas la decision metier, il la rend plus explicite, plus comparable et plus defendable.