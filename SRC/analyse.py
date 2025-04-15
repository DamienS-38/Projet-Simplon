import sqlite3
import pandas as pd
import os

# Connexion à la base de données
conn = sqlite3.connect(os.path.join("DATA", "pme.db"))

# 1. Quantité totale de produits vendus par magasin
query_magasins = """
SELECT 
    M.ville,
    SUM(V.quantite) AS total_produits_vendus
FROM Ventes V
JOIN Magasins M ON V.id_magasin = M.id_magasin
GROUP BY M.ville
ORDER BY total_produits_vendus DESC;
"""
df_magasins = pd.read_sql(query_magasins, conn)
print("\n🛒 Quantité totale de produits vendus par magasin :")
print(df_magasins)

# 2. Produit le plus vendu (en nombre de fois)
query_top_produit = """
SELECT 
    P.nom AS produit,
    SUM(V.quantite) AS total_vendu
FROM Ventes V
JOIN Produit P ON V.id_produit = P.id_produit
GROUP BY V.id_produit
ORDER BY total_vendu DESC
LIMIT 10;
"""
df_top_produit = pd.read_sql(query_top_produit, conn)
print("\n🏆 Les 10 Produits le plus vendus :")
print(df_top_produit)


# 3. Chiffre d'affaire par magasin
query_ca_par_magasin = """
SELECT 
    M.ville,
    SUM(V.quantite * P.prix) AS chiffre_affaires
FROM Ventes V
JOIN Produit P ON V.id_produit = P.id_produit
JOIN Magasins M ON V.id_magasin = M.id_magasin
GROUP BY M.id_magasin
ORDER BY chiffre_affaires DESC;
"""

df_ca = pd.read_sql(query_ca_par_magasin, conn)
print("\n💰 Chiffre d'affaires par magasin en € :")
print(df_ca)

# Fermeture de la connexion
conn.close()