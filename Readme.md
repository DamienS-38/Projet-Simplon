
Le but du projet:







🚀 Comment lancer avec Docker

    Commencez par installer Docker :
        - Télacharger Docker Desktop: https://www.docker.com/products/docker-desktop
        - Dans le terminal, se mettre dans le dossier de travail
        - Docker Compose (intégré à Docker Desktop) — utilisez `docker compose` et non `docker-compose`.
        - Dans le terminal "bash" tapper: docker compose up --build


⚙️ Fonctionnalités du script Python

    Description des étapes dans le script :
        - Nettoie et renomme les colonnes des CSV
        - Crée les tables dans pme.db si elles n’existent pas
        - Insère les données en base
        - Respecte les clés primaires/étrangères et l’auto-incrément de id_vente



Exemple de requêtes
