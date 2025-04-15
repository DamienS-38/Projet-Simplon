# 📊 Projet SIMPLON (CSV ➜ SQLite avec Docker)

## 🎯 Objectif du projet

- Lire un ou plusieurs fichiers **CSV**.
- Générer une base **SQLite** contenant les données.
- Permettre des **requêtes SQL interactives** sur la base via Docker.

---

## 🧱 Architecture (Docker)

Ce projet utilise **deux services Docker** définis dans `docker-compose.yml` :

| Service       | Rôle                                                                     |
|---------------|--------------------------------------------------------------------------|
| `csv-runner`  | Exécute le script Python de transformation CSV ➜ SQLite                 |
| `sqlite_base` | Conteneur persistant pour accéder à la base SQLite et faire des requêtes |

🖼️ **Schéma de l'architecture** :  
![Architecture Docker](docker_architecture.png)

---

## 📁 Arborescence du projet

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

---

## ⚙️ Fonctionnalités du script Python

    Description des étapes dans le script :
        - Nettoie et renomme les colonnes des CSV
        - Crée les tables dans pme.db si elles n’existent pas
        - Insère les données en base
        - Respect des clés primaires/étrangères et l’auto-incrément de id_vente

---

## 🚀 Comment exécuter l'application avec Docker
1. ⚙️ **Installer Docker** si ce n’est pas déjà fait :  
   👉 [Docker Desktop](https://www.docker.com/products/docker-desktop)

2. 📁 Ouvrir un terminal dans le dossier du projet

3. 🧱 **Construire et démarrer les conteneurs :**
```bash
docker compose up --build
```

4. ✅ **Vérifier que tout tourne :**
```bash
docker ps
```

5. 🔍 **Accéder à SQLite dans le conteneur :**
```bash
docker exec -it sqlite_base bash
sqlite3 /app/DATA/pme.db
```

---



## 🚪 Quitter l’application
- Quitter sqlite :
```bash
.quit
```
- Sortir du container :
```bash
Exit
```
- Pour arrêter le conteneur (à la fin de l'utilisation) :
```bash
docker compose down
```  

---

## 📬 Contact
- Lien Linkedin: 📧 [Linkedin](https://www.linkedin.com/in/damien-schaeffer-45a59821b/)
    