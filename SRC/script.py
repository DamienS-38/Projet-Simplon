# Imports
import pandas as pd
import sqlite3
import os

# Connexion à la base SQLite
conn = sqlite3.connect("pme.db")
cursor = conn.cursor()

# Création des tables si elles n'existent pas
cursor.execute('''
CREATE TABLE IF NOT EXISTS Produit (
    id_produit TEXT PRIMARY KEY,
    nom TEXT,
    prix REAL,
    stock INT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Magasins (
    id_magasin TEXT PRIMARY KEY,
    ville TEXT,
    Nb_salarie INT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Ventes (
    id_vente INTEGER PRIMARY KEY AUTOINCREMENT,
    id_produit TEXT,
    id_magasin TEXT,
    date_vente TEXT,
    quantite INTEGER,
    FOREIGN KEY(id_produit) REFERENCES Produit(id_produit),
    FOREIGN KEY(id_magasin) REFERENCES Magasins(id_magasin),
    UNIQUE(id_produit, id_magasin, date_vente)
)
''')

# Chargement des CSV
df_produits = pd.read_csv('DATA/produits.csv', delimiter=',')
df_magasins = pd.read_csv('DATA/magasins.csv', delimiter=',')
df_ventes = pd.read_csv('DATA/ventes.csv', delimiter=',')

# Renommage des colonnes
df_produits = df_produits.rename(columns={
    'ID Référence produit': 'id_produit',
    'Nom': 'nom',
    'Prix': 'prix',
    'Stock': 'stock'
})
ordre_colonnes_produits = ['id_produit', 'nom', 'prix', 'stock']
df_produits = df_produits[ordre_colonnes_produits]

df_magasins = df_magasins.rename(columns={
    'ID Magasin': 'id_magasin',
    'Ville': 'ville',
    'Nombre de salariés': 'nb_salarie'
})

df_ventes = df_ventes.rename(columns={
    'ID Magasin': 'id_magasin',
    'ID Référence produit': 'id_produit',
    'Date': 'date_vente',
    'Quantité': 'quantite'
})
ordre_colonnes_ventes = ['id_produit', 'id_magasin', 'date_vente', 'quantite']
df_ventes = df_ventes[ordre_colonnes_ventes]

# Éviter les doublons sur Produits
id_produit_existant = pd.read_sql("SELECT id_produit FROM Produit", conn)['id_produit'].tolist()
df_produits = df_produits[~df_produits['id_produit'].isin(id_produit_existant)]

# Éviter les doublons sur Magasins
id_magasin_existant = pd.read_sql("SELECT id_magasin FROM Magasins", conn)['id_magasin'].tolist()
df_magasins = df_magasins[~df_magasins['id_magasin'].isin(id_magasin_existant)]

# Éviter les doublons sur Ventes (via clé composite)
df_ventes['vente_key'] = df_ventes['id_produit'] + "_" + df_ventes['id_magasin'] + "_" + df_ventes['date_vente']
ventes_existantes = pd.read_sql("SELECT id_produit, id_magasin, date_vente FROM Ventes", conn)

ventes_existantes['vente_key'] = ventes_existantes['id_produit'] + "_" + ventes_existantes['id_magasin'] + "_" + ventes_existantes['date_vente']
df_ventes = df_ventes[~df_ventes['vente_key'].isin(ventes_existantes['vente_key'])]
df_ventes = df_ventes.drop(columns=['vente_key'])

# Insertion des données
df_produits.to_sql('Produit', conn, if_exists='replace', index=False)
df_magasins.to_sql('Magasins', conn, if_exists='replace', index=False)
df_ventes.to_sql('Ventes', conn, if_exists='append', index=False)

# Finalisation
conn.commit()
conn.close()
