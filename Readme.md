
Le but du projet:







🚀 Comment lancer avec Docker

    Commencez par installer Docker :
        - [Docker](https://www.docker.com/products/docker-desktop)
        - Dans le terminal, se mettre dans le dossier de travail
        - Docker Compose (intégré à Docker Desktop) — utilisez `docker compose` et non `docker-compose`.
        - Dans le terminal "bash" tapper: docker compose up --build


Le script Python :
    Nettoie et renomme les colonnes des CSV
    Crée les tables dans pme.db si elles n’existent pas
    Insère les données en évitant les doublons
    Respecte les clés primaires/étrangères et l’auto-incrément de id_vente



Exemple de requêtes
