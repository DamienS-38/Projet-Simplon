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
JOIN Produits P ON V.id_produit = P.id_produit
"""
df_ca_total = pd.read_sql(query_ca_total, conn)
cursor.execute("INSERT INTO Analyse (date_analyse, type_analyse, resultat) VALUES (?, ?, ?)",
               (today, "ca_total", df_ca_total.to_json(orient="records")))
conn.commit()

print(f"\n Chiffre d'affaires total : {df_ca_total['chiffre_affaires_total'][0]:.2f} €")




# 2. L'article le plus vendu, affiche la quantité
query_ventes_produit = """
SELECT V.id_produit as Ref_produit, SUM(quantite) as Quantite_vendue
FROM Ventes V
JOIN Produits P ON V.id_produit = P.id_produit
GROUP BY V.id_produit
ORDER BY Quantite_vendue DESC
"""
df_ventes_produit=pd.read_sql(query_ventes_produit, conn)
cursor.execute("INSERT INTO Analyse (date_analyse, type_analyse, resultat) VALUES (?, ?, ?)",
               (today, "Quantité_par_produit", df_ventes_produit.to_json(orient="records")))
conn.commit()

print(f"\n La quantité de l'article {df_ventes_produit['Ref_produit'][0]}, le plus vendu est de : {df_ventes_produit['Quantite_vendue'][0]} ")

# 3. Tableau des ventes par produit
query = """
SELECT V.id_produit AS Ref_produit, P.nom AS Nom_produit, SUM(quantite) AS Quantite_vendue
FROM Ventes V
JOIN Produits P ON V.id_produit = P.id_produit
GROUP BY V.id_produit
ORDER BY Quantite_vendue DESC
"""

df_ventes_par_produit = pd.read_sql(query, conn)

print("\n Tableau des ventes par produit :")
print(df_ventes_par_produit.to_string(index=False))
print("\n")

# Fermeture
conn.close()
