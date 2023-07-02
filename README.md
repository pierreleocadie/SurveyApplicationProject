# SAÉ Semestre 4 - Rapport

**ÉQUIPE** :
Jordan BAUMARD
Charles HURST
Pierre LEOCADIE

**Groupe 209**

![Untitled](SAE%CC%81%20Semestre%204%20-%20Rapport%2056dfdd2e0b1b4447b1f65bc65e7c1563/Untitled.png)

# Partie 1

## Cahier des charges de l’application

L’application sondage doit permettre :

- À l’utilisateur de répondre au sondage via une interface intuitive et ergonomique
    - Saisie des informations personnelles :
        - Nom
        - Prénom
        - Naissance
        - Adresse
        - Code postal
        - Ville
        - Tel
    - Choisir les 10 aliments qu’il consomme le plus parmi la liste des aliments disponibles
        - L’utilisateur pourra filtrer les aliments en utilisant les groupes, sous groupes et sous sous groupes d’aliments → éviter d’envoyer toute la table aliments côté client
- Avoir une interface de restitution des résultats
    - Accessible via une interface de connexion avec un compte super admin ou admin
    - Qui permettra également de gérer (création/suppression) des comptes admins
    - Gestion des clés API (création, modification, suppression)
- Interface de connexion pour les super admins ou admins

<aside>
ℹ️ Les points en bleus sont ceux que nous avons décidé d'ajouter en plus des fonctionnalités de base de l’application.

</aside>

## Base de données

![Diagramme base de données de l’application sondage](SAE%CC%81%20Semestre%204%20-%20Rapport%2056dfdd2e0b1b4447b1f65bc65e7c1563/Diagramme_base_donnees.drawio.png)

Diagramme base de données de l’application sondage

Dans notre projet, nous avons opté pour l'utilisation de MySQL comme base de données. Afin d'organiser efficacement les données initiales provenant des fichiers Excel "Aliments.xlsx" et "Sondage.xlsx", nous les avons divisées en plusieurs tables SQL. Nous avons également renommé les champs de données en anglais pour une meilleure cohérence avec le code de l'application. Ces tables sont interconnectées à l'aide de clés étrangères.

Voici un aperçu des différentes tables que nous avons créées :

1. La table "constituents" contient les informations des administrés, telles que leur identifiant, nom, prénom, date de naissance, adresse, code postal, ville, téléphone, et la date d'insertion dans la table.
2. La table "survey" stocke les réponses des administrés au sondage, avec l'identifiant de l'administré et les codes des aliments auxquels ils font référence.
3. La table "foods" contient les données relatives aux aliments, comme leur code, nom en français, nom scientifique, code de groupe alimentaire et code de sous-groupe alimentaire.
4. La table "food_nutrients" rassemble toutes les informations nutritionnelles des aliments.
5. La table "food_groups" contient les données sur les différents groupes d'aliments, avec leur code et leur nom en français.
6. La table "food_subgroups" regroupe les informations sur les sous-groupes d'aliments, comprenant leur code, le code du groupe auquel ils appartiennent, et leur nom en français.
7. La table "food_sub_subgroups" contient les données des sous-sous-groupes d'aliments, avec leur code, le code du sous-groupe auquel ils sont rattachés, et leur nom en français.

En plus des tables créées à partir des données initiales, nous avons également ajouté deux nouvelles tables : "admin" et "api_keys". La table "admin" stocke les informations des comptes administrateurs, tandis que la table "api_keys" stocke les clés API qui sont créées.

## Générer un jeu de données aléatoires

Pour alimenter notre base de données, nous avons utilisé l'API de **[https://randomuser.me/](https://randomuser.me/)** pour générer un ensemble de données aléatoires. Nous avons créé des profils fictifs de personnes en utilisant cette API, et nous avons également généré des réponses aléatoires au sondage pour ces profils fictifs. Pour accomplir ces tâches, nous avons utilisé le même script Python que nous avons créé lors de la première SAÉ. Cependant, nous l'avons adapté pour inclure la gestion de l'insertion des données dans la base de données.

Au total, nous avons créé 30 000 profils fictifs, chacun avec ses réponses au sondage correspondantes. Cela a abouti à une base de données contenant plus de 66 000 lignes de données, pesant environ 15 Mo.

## Le back-end de l’application

### Pourquoi une API ?

Pour le développement de la partie serveur (back-end) de notre application, nous avons décidé d'adopter une approche basée sur l'utilisation d'une API (Interface de Programmation Applicative). Ce choix a été motivé par plusieurs raisons importantes.

Tout d'abord, l'utilisation d'une API offre une architecture plus flexible et modulaire. Elle permet de séparer clairement la logique métier de l'interface utilisateur, facilitant ainsi la maintenance et l'évolution de l'application.

De plus, en utilisant une API, nous pouvons fournir des fonctionnalités et des données aux clients de manière cohérente, indépendamment de la plateforme ou du type de client (web, mobile, etc.). Cela permet d'assurer une expérience utilisateur homogène et de faciliter l'extension de l'application à l'avenir.

Un autre avantage important de l'utilisation d'une API est la possibilité de contrôler l'accès aux requêtes spécifiques. Nous pouvons mettre en place des mécanismes de sécurité pour protéger les données sensibles, telles que les informations des administrés ou les statistiques, en contrôlant les autorisations d'accès aux différentes parties de l'API.

Dans notre cas, nous avons choisi d’appeler notre API en utilisant ReactJS pour le front-end. ReactJS est un framework JavaScript populaire qui facilite la création d'interfaces utilisateur interactives et réactives. Son approche basée sur des composants modulaires est bien adaptée à la création d'API flexibles et évolutives.

En résumé, l'utilisation d'une API pour notre application back-end nous offre une architecture modulaire, des services réutilisables, une expérience utilisateur cohérente et une évolutivité facilitée. Cette approche est complétée par l'utilisation de ReactJS pour notre front-end, nous permettant de créer une interface utilisateur réactive et conviviale. De plus, l'API nous permet de contrôler l'accès aux données sensibles et d'assurer la sécurité de notre application.

### Développement de l’API

Pour le développement de notre API, nous avons choisi d'utiliser le langage Python. Cette décision a été motivée par plusieurs raisons importantes.

Tout d'abord, Python bénéficie d'une syntaxe simple, claire et lisible, ce qui facilite le développement et la compréhension du code. Cette caractéristique est particulièrement avantageuse pour le développement d'une API, car elle permet de créer un code propre et facilement maintenable.

Ensuite, Python dispose d'un vaste écosystème de bibliothèques et de frameworks qui facilitent le développement d'API. Dans notre cas, nous avons choisi d'utiliser le framework FastAPI. FastAPI est un framework Python moderne et performant, conçu pour faciliter la création d'API REST rapides et évolutives. Il offre des fonctionnalités avancées telles que la validation des données et la génération automatique de documentation pour notre API.

De plus, l'utilisation de pydantic en combinaison avec FastAPI facilite la validation et la transformation des données. Pydantic permet de définir des modèles de données avec des validations intégrées, ce qui garantit la cohérence et la conformité des données reçues et renvoyées par l'API. Cela simplifie la gestion des erreurs et contribue à la fiabilité de notre application.

Une autre raison importante pour laquelle nous avons choisi Python est sa grande communauté de développeurs. Python est largement utilisé et bénéficie d'un support actif de la part de la communauté. Cela signifie que nous avons facilement accès à une multitude de ressources, de tutoriels et de documentation pour nous aider dans le développement de notre API.

Enfin, Python est un langage multiplateforme, ce qui signifie que notre API développée en Python peut être exécutée sur différentes plateformes et systèmes d'exploitation. Cela offre une flexibilité dans le déploiement de notre API, en fonction des besoins de notre projet.

En résumé, notre choix d'utiliser Python pour le développement de notre API est motivé par sa syntaxe simple et lisible, son vaste écosystème de bibliothèques et de frameworks, son support actif de la communauté, sa compatibilité multiplateforme et notre choix spécifique du framework FastAPI. Ensemble, ces facteurs nous permettent de développer une API performante, robuste et facile à maintenir pour notre projet.

## Le front-end de l’application

### Page de sondage

La création d'une page de sondage moderne et intuitive était au cœur de notre démarche pour ce projet. Nous avons cherché à développer une interface conviviale et facile à naviguer pour maximiser l'engagement des utilisateurs. Les éléments visuels ont été soigneusement choisis pour être agréables à l'œil et pour faciliter la compréhension du processus de sondage. De plus, chaque étape du sondage a été conçue pour être simple et directe, minimisant la confusion et le temps nécessaire pour compléter chaque section. Pour améliorer davantage l'expérience utilisateur, nous avons veillé à ce que la page se charge rapidement, tout en restant réactive à toutes les interactions. En combinant tous ces éléments, nous croyons avoir créé une page de sondage qui encourage activement la participation tout en respectant les meilleures pratiques en matière d'expérience utilisateur et de design web moderne.

![Screenshot 2023-06-26 at 22.52.39.png](SAE%CC%81%20Semestre%204%20-%20Rapport%2056dfdd2e0b1b4447b1f65bc65e7c1563/Screenshot_2023-06-26_at_22.52.39.png)

La première page de notre sondage est dédiée à la collecte des informations de l'utilisateur. Afin d'assurer une progression linéaire et logique, l'utilisateur ne peut pas passer à la page suivante tant qu'il n'a pas correctement rempli toutes les informations requises. Cela garantit l'intégrité et la complétude des données recueillies. Le formulaire d'information est conçu pour être simple et direct, demandant à l'utilisateur de fournir des informations essentielles sans être trop intrusif. De plus, afin d'éviter toute confusion ou frustration, des messages d'erreur clairs sont affichés en cas d'informations manquantes ou incorrectes. L'objectif est de faire en sorte que les utilisateurs se sentent en confiance lorsqu'ils fournissent leurs informations, tout en garantissant qu'ils comprennent clairement ce qui est requis à chaque étape du processus.

![Screenshot 2023-06-26 at 22.53.06.png](SAE%CC%81%20Semestre%204%20-%20Rapport%2056dfdd2e0b1b4447b1f65bc65e7c1563/Screenshot_2023-06-26_at_22.53.06.png)

Le respect du Règlement Général sur la Protection des Données (RGPD) est une priorité pour nous. Par conséquent, nous demandons à l'utilisateur d'accepter que ses informations soient stockées et utilisées dans le but d'établir un score santé. L'utilisateur ne peut pas continuer le sondage sans accepter cette condition, garantissant ainsi que nous respectons les normes de consentement du RGPD. Nous stockons ces informations de manière sécurisée dans le localStorage. C'est un élément clé pour améliorer l'expérience utilisateur, car cela permet à l'utilisateur de quitter le sondage et d'y revenir plusieurs jours après sans avoir à ressaisir ses informations. C'est une fonctionnalité particulièrement utile pour les sondages plus longs ou pour les utilisateurs qui pourraient être interrompus pendant le processus.

![Screenshot 2023-06-26 at 22.53.12.png](SAE%CC%81%20Semestre%204%20-%20Rapport%2056dfdd2e0b1b4447b1f65bc65e7c1563/Screenshot_2023-06-26_at_22.53.12.png)

La section de notre sondage demandant à l'utilisateur de sélectionner ses dix aliments préférés a été soigneusement conçue pour être à la fois intuitive et facile à utiliser. Nous avons structuré les choix d'aliments en différents groupes, sous-groupes et sous-sous-groupes pour faciliter la navigation. Chaque catégorie affiche le nombre d'aliments que l'utilisateur a déjà sélectionnés, ce qui lui permet de suivre facilement ses choix et de les modifier si nécessaire. Le formulaire ne peut pas être validé tant que l'utilisateur n'a pas sélectionné dix aliments, ce qui garantit que nous recueillons les informations complètes nécessaires pour notre analyse. Pour faciliter encore plus la tâche, nous avons ajouté une fonction permettant à l'utilisateur d'effacer tous ses choix en une seule fois grâce à un bouton situé en bas de la page. Cette attention aux détails facilite le processus de sélection des aliments et rend l'expérience globale du sondage plus agréable.

![Screenshot 2023-06-26 at 22.53.30.png](SAE%CC%81%20Semestre%204%20-%20Rapport%2056dfdd2e0b1b4447b1f65bc65e7c1563/Screenshot_2023-06-26_at_22.53.30.png)

Afin de préserver l'intégrité de notre sondage et d'éviter les doublons, nous avons mis en place une mesure pour empêcher un utilisateur de répondre plus d'une fois au sondage. Une fois qu'un utilisateur a soumis ses réponses, il lui est indiqué clairement que sa participation a été enregistrée et il ne peut plus modifier ses réponses ou refaire le sondage. Cela garantit également que chaque utilisateur a une influence équitable sur les résultats du sondage. Cette restriction est rendue possible grâce à notre méthode de stockage des informations utilisateur, ce qui nous permet de vérifier si un utilisateur a déjà participé au sondage. Par conséquent, nous sommes en mesure de maintenir des données précises et fiables tout en respectant l'équité de la participation au sondage.

![Screenshot 2023-06-26 at 22.53.51.png](SAE%CC%81%20Semestre%204%20-%20Rapport%2056dfdd2e0b1b4447b1f65bc65e7c1563/Screenshot_2023-06-26_at_22.53.51.png)

L'accès au tableau de bord est strictement contrôlé et réservé aux utilisateurs ayant un compte superAdmin ou admin. Cette mesure de sécurité garantit que seuls les utilisateurs autorisés peuvent visualiser les résultats du sondage. Lorsqu'un utilisateur se connecte, ses informations d'identification sont enregistrées de manière sécurisée dans le localStorage. Les données sont chiffrées pour garantir leur sécurité, et ce système permet à l'utilisateur de rester connecté et de ne pas avoir à saisir à nouveau ses informations à chaque visite. Cela contribue à faciliter l'accès pour les utilisateurs autorisés tout en maintenant un haut niveau de sécurité. Cette fonctionnalité est particulièrement utile pour les utilisateurs qui ont besoin d'accéder régulièrement au tableau de bord, car elle réduit le temps nécessaire pour se connecter et permet un accès plus fluide aux informations.

### Page de connexion

![Screenshot 2023-06-26 at 22.45.21.png](SAE%CC%81%20Semestre%204%20-%20Rapport%2056dfdd2e0b1b4447b1f65bc65e7c1563/Screenshot_2023-06-26_at_22.45.21.png)

### Dashboard

Nous avons créé un tableau de bord robuste et intuitif pour visualiser les résultats du sondage. Sur cette page, trois diagrammes en barres représentent respectivement les groupes d'aliments les plus consommés, les sous-groupes d'aliments les plus consommés et les sous-sous-groupes d'aliments les plus consommés. Ces visualisations offrent un aperçu rapide et facile à comprendre des tendances de consommation des utilisateurs. Bien qu'actuellement non implémentée, nous envisageons une évolution future qui permettrait d'afficher d'autres statistiques, telles que le nombre total de réponses au sondage, le nombre de visiteurs et des indicateurs de score santé comme la moyenne, le minimum et le maximum. Cela permettrait une analyse plus détaillée et plus complète des données collectées, offrant aux administrateurs une meilleure compréhension des habitudes alimentaires des utilisateurs.

![Screenshot 2023-06-26 at 22.44.40.png](SAE%CC%81%20Semestre%204%20-%20Rapport%2056dfdd2e0b1b4447b1f65bc65e7c1563/Screenshot_2023-06-26_at_22.44.40.png)

![Screenshot 2023-06-26 at 22.44.45.png](SAE%CC%81%20Semestre%204%20-%20Rapport%2056dfdd2e0b1b4447b1f65bc65e7c1563/Screenshot_2023-06-26_at_22.44.45.png)

Sur la seconde page du tableau de bord, nous avons intégré une fonctionnalité permettant de visualiser les groupes d'aliments, les sous-groupes d'aliments et les sous-sous-groupes d'aliments les plus consommés, segmentés par tranche d'âge. Cela offre une perspective plus précise et nuancée de la consommation alimentaire en fonction de l'âge, permettant une analyse plus détaillée des habitudes alimentaires. Ce niveau de granularité peut fournir des informations précieuses pour comprendre comment les préférences alimentaires varient avec l'âge, et peut aider à identifier des tendances ou des modèles spécifiques. Cela constitue un outil puissant pour analyser les données du sondage, et nous pensons que cela ajoutera une valeur significative à notre plateforme.

![Screenshot 2023-06-26 at 22.44.55.png](SAE%CC%81%20Semestre%204%20-%20Rapport%2056dfdd2e0b1b4447b1f65bc65e7c1563/Screenshot_2023-06-26_at_22.44.55.png)

La troisième page du tableau de bord est consacrée à la gestion des clés API. Ces clés jouent un rôle crucial dans la sécurisation des appels à l'API, une mesure de sécurité que nous avons décidé d'implémenter pour protéger les données sensibles. Cette page n'est visible que par les superAdmins, garantissant ainsi un contrôle strict de l'accès aux clés API. Les superAdmins ont la possibilité de créer une nouvelle clé API pour un admin, de mettre à jour une clé API (l'activer ou la désactiver), de supprimer une clé API et de consulter les clés API qui ont été créées. Cette gestion centralisée des clés API assure une meilleure organisation, un suivi plus efficace et une sécurité renforcée de notre système.

![Screenshot 2023-06-26 at 22.45.00.png](SAE%CC%81%20Semestre%204%20-%20Rapport%2056dfdd2e0b1b4447b1f65bc65e7c1563/Screenshot_2023-06-26_at_22.45.00.png)

Sur une autre page dédiée, nous avons donné la possibilité aux superAdmins de créer de nouveaux comptes admin. Cela facilite la gestion des utilisateurs et permet une expansion organisée de l'équipe administrative si nécessaire. En donnant ce pouvoir aux superAdmins, nous assurons que seules les personnes de confiance et autorisées ont la capacité de donner des accès administratifs. Cela renforce non seulement la sécurité du système, mais maintient également un contrôle rigoureux sur les personnes ayant accès aux données sensibles du sondage. C'est une fonctionnalité essentielle pour assurer le bon fonctionnement et la croissance contrôlée de la plateforme.

![Screenshot 2023-06-26 at 22.45.04.png](SAE%CC%81%20Semestre%204%20-%20Rapport%2056dfdd2e0b1b4447b1f65bc65e7c1563/Screenshot_2023-06-26_at_22.45.04.png)

### Responsive

L'accessibilité et l'adaptabilité ont été des considérations majeures lors du développement de notre application. Nous avons veillé à ce que l'application soit entièrement responsive et parfaitement fonctionnelle sur une variété de dispositifs, notamment les téléphones, les tablettes et les PC. Quelle que soit la taille de l'écran ou le type d'appareil utilisé, les utilisateurs bénéficient d'une expérience optimale grâce à un design qui s'adapte automatiquement à leurs conditions d'utilisation. Cette flexibilité permet à plus d'utilisateurs d'accéder facilement à notre sondage et à notre tableau de bord, quelle que soit leur situation, maximisant ainsi la portée et l'efficacité de notre application.

![Screenshot 2023-06-26 at 22.49.54.png](SAE%CC%81%20Semestre%204%20-%20Rapport%2056dfdd2e0b1b4447b1f65bc65e7c1563/Screenshot_2023-06-26_at_22.49.54.png)

# Partie 2

Le deuxième rapport est séparé en raison de sa taille.

# Conclusion globale du projet

Ce projet nous a offert une opportunité d'explorer et de développer nos compétences dans de nouvelles technologies. Dans la première partie du projet, nous avons découvert le module Python FastAPI pour la conception d'API et avons appliqué des méthodes de conception logicielles apprises en cours. Nous avons effectué un refactoring de l'API pour améliorer sa qualité et sa maintenabilité. De plus, nous avons créé une interface utilisateur attrayante, intuitive et fluide en utilisant ReactJS, qui s'est avéré être un excellent choix pour interagir avec l’API. Cette combinaison de technologies nous a permis de créer un système performant et convivial.

Dans la seconde partie du projet, nous avons abordé l'aspect réseau en déployant une infrastructure AWS. Nous avons utilisé des outils tels que Docker, AWS, Terraform et Ansible pour configurer et gérer notre infrastructure réseau. Cela nous a permis de mettre en place un environnement sécurisé et évolutif pour nos applications. Nous avons déployé des services tels que NGINX Proxy Manager, WireGuard-UI, Pihole et GoAccess, qui ont tous contribué à améliorer la sécurité, la gestion des accès et la visibilité de notre infrastructure. Ce volet du projet nous a permis d'acquérir une compréhension approfondie du fonctionnement des réseaux et des technologies utilisées dans le cloud computing.

En conclusion, ce projet nous a offert une expérience enrichissante pour explorer différentes facettes du développement logiciel et de l'infrastructure réseau. Nous sommes heureux d'avoir pu mettre en pratique nos connaissances théoriques. Ce projet a renforcé notre compréhension des technologies émergentes.