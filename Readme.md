
🎯 Objectif du projet

    Description:
        -Ce projet a pour but d’automatiser le traitement de fichiers CSV contenant des informations
        liées aux ventes, aux clients, aux produits et aux collaborateurs d’une PME. Le script Python
        fourni permet de nettoyer, structurer et stocker les données dans une base SQLite (pme.db), 
        tout en respectant l’intégrité des données (relations, clés primaires/étrangères, etc.)


🧭 Architecture du Projet

Voici un visuel de l’architecture Dockerdu projet :
    ![Architecture Docker](docker-architecture.png)



🚀 Comment lancer avec Docker

    Commencez par installer Docker :
        - Télécharger [Docker Desktop](https://www.docker.com/products/docker-desktop)
        - Dans le terminal, se mettre dans le dossier de travail
        - Lancer l’application avec la commande :
            ```bash
            docker compose up --build
        - Pour tester le containeur dans le terminal : docker start -ai sqlite_base
        - Pour arrêter le conteneur (à la fin de l'utilisation):
            ```bash
            docker compose down
            


⚙️ Fonctionnalités du script Python

    Description des étapes dans le script :
        - Nettoie et renomme les colonnes des CSV
        - Crée les tables dans pme.db si elles n’existent pas
        - Insère les données en base
        - Respect des clés primaires/étrangères et l’auto-incrément de id_vente



Exemple de requêtes
