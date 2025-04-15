import sqlite3
import pandas as pd
from datetime import datetime
import os

# Connexion à la base
db_path = os.path.join("DATA", "pme.db")
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Création de la table Analyse si elle n'existe pas
cursor.execute("""
CREATE TABLE IF NOT EXISTS Analyse (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date_analyse TEXT,
    type_analyse TEXT,
    resultat TEXT
)
""")
conn.commit()

today = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# 1. Chiffre d'affaires total
query_ca_total = """
SELECT SUM(V.quantite * P.prix) AS chiffre_affaires_total
FROM Ventes V
JOIN Produit P ON V.id_produit = P.id_produit
"""
df_ca_total = pd.read_sql(query_ca_total, conn)
cursor.execute("INSERT INTO Analyse (date_analyse, type_analyse, resultat) VALUES (?, ?, ?)",
               (today, "ca_total", df_ca_total.to_json(orient="records")))
conn.commit()

print(f"\n💰 Chiffre d'affaires total : {df_ca_total['chiffre_affaires_total'][0]:.2f} €")





# 2. Produits vendus par magasin
query_magasins = """
SELECT M.ville, SUM(V.quantite) AS total_produits_vendus
FROM Ventes V
JOIN Magasins M ON V.id_magasin = M.id_magasin
GROUP BY M.ville
ORDER BY total_produits_vendus DESC
"""
df_magasins = pd.read_sql(query_magasins, conn)
cursor.execute("INSERT INTO Analyse (date_analyse, type_analyse, resultat) VALUES (?, ?, ?)",
               (today, "quantite_par_magasin", df_magasins.to_json(orient="records")))
conn.commit()

# 3. Top 10 produits
query_top = """
SELECT P.nom AS produit, SUM(V.quantite) AS total_vendu
FROM Ventes V
JOIN Produit P ON V.id_produit = P.id_produit
GROUP BY V.id_produit
ORDER BY total_vendu DESC
LIMIT 10
"""
df_top = pd.read_sql(query_top, conn)
cursor.execute("INSERT INTO Analyse (date_analyse, type_analyse, resultat) VALUES (?, ?, ?)",
               (today, "top_10_produits", df_top.to_json(orient="records")))
conn.commit()

# 4. Chiffre d'affaires par magasin
query_ca = """
SELECT M.ville, SUM(V.quantite * P.prix) AS chiffre_affaires
FROM Ventes V
JOIN Produit P ON V.id_produit = P.id_produit
JOIN Magasins M ON V.id_magasin = M.id_magasin
GROUP BY M.ville
ORDER BY chiffre_affaires DESC
"""
df_ca = pd.read_sql(query_ca, conn)
cursor.execute("INSERT INTO Analyse (date_analyse, type_analyse, resultat) VALUES (?, ?, ?)",
               (today, "ca_par_magasin", df_ca.to_json(orient="records")))
conn.commit()




# Fermeture
conn.close()
