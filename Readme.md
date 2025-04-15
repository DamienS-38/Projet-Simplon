
🎯 Objectif du projet

- Lire un ou plusieurs fichiers CSV.
- Générer une base SQLite contenant les données.
- Permettre des requêtes SQL interactives sur la base.

🧱 Architecture (Docker)

Deux services sont utilisés (dans docker-compose.yml) :

| Service       | Rôle                                                                     |
|---------------|--------------------------------------------------------------------------|
| `csv-runner`  | Exécute le script Python de transformation CSV ➜ SQLite                 |
| `sqlite_base` | Conteneur persistant pour accéder à la base SQLite et faire des requêtes |


📁 Arborescence du projet

    ├── DATA/
    │   ├── magasins.csv              # Fichier CSV magasins source
    │   ├── produits.csv              # Fichier CSV produits source
    │   ├── ventes.csv                # Fichier CSV ventes source
    │   └── pme.db                    # Base SQLite générée
    │
    ├── SRC/
    │   └── script.py                 # Script Python de conversion CSV ➜ SQLite
    │
    ├── docker_architecture.png       # Schéma de l'architecture
    ├── requirements.txt              # Dépendances Python
    ├── Dockerfile                    # Image Docker avec Python + sqlite3
    ├── docker-compose.yml            # Orchestration des conteneurs
    └── README.md                     # Documentation du projet

🚀 Comment lancer avec Docker

    Commencez par installer Docker :
        - Télécharger [Docker Desktop](https://www.docker.com/products/docker-desktop)
        - Dans le terminal, se mettre dans le dossier de travail
        - Lancer l’application avec la commande :
            ```bash
            docker compose up --build
        - Pour tester le containeur dans le terminal : docker ps
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


📬 Contact

    Damien S.
    📧 [Linkedin](https://www.linkedin.com/in/damien-schaeffer-45a59821b/)