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
```
├── DATA/
│   ├── magasins.csv              # CSV source des magasins
│   ├── produits.csv              # CSV source des produits
│   ├── ventes.csv                # CSV source des ventes
│   └── pme.db                    # Base SQLite générée automatiquement
│
├── SRC/
│   └── script.py                 # Script Python de transformation CSV ➜ SQLite
│
├── docker_architecture.png       # Schéma visuel de l'architecture
├── requirements.txt              # Dépendances Python
├── Dockerfile                    # Image Docker (Python + SQLite)
├── docker-compose.yml            # Définition des services
└── README.md                     # Documentation du projet
```
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
## 🧪 Requêtes SQL dans SQLite

Voici quelques commandes utiles une fois dans le client SQLite :

```sql
.tables                     -- Voir les tables disponibles
.schema nom_de_table       -- Voir la structure d’une table
SELECT * FROM ventes;      -- Voir les ventes
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

👤 Damien Schaeffer  
🔗 [LinkedIn](https://www.linkedin.com/in/damien-schaeffer-45a59821b/)
---