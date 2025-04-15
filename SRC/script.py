#Imports
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
    FOREIGN KEY(id_magasin) REFERENCES Magasins(id_magasin)
)
''')

# Chargement des CSV
df_produits =pd.read_csv('DATA/produits.csv', delimiter=',')
df_magasins = pd.read_csv('DATA/magasins.csv', delimiter=',')
df_ventes=pd.read_csv('DATA/ventes.csv', delimiter=',')


#renommer les colonnes des DataFrame
df_produits = df_produits.rename(columns={
    'ID Référence produit':'id_produit',
    'Nom': 'nom',
    'Prix': 'prix',
    'Stock': 'stock'
})
ordre_colonnes_produits = ['id_produit', 'nom', 'prix', 'stock']
df_produits = df_produits[ordre_colonnes_produits]

df_magasins= df_magasins.rename(columns={
    'ID Magasin': 'id_magasin',
    'Ville' : 'ville',
    'Nombre de salariés': 'nb_salarie'
})

df_ventes=df_ventes.rename(columns={
    'ID Magasin': 'id_magasin',
    'ID Référence produit':'id_produit',
    'Date': 'date_vente',
    'Quantité': 'quantite'
})
ordre_colonnes_ventes = ['id_produit', 'id_magasin', 'date_vente', 'quantite']
df_ventes = df_ventes[ordre_colonnes_ventes]

#Eviter les doublons en base
id_produit_existant = pd.read_sql("SELECT id_produit FROM Produit", conn)['id_produit'].tolist()
df_produits = df_produits[~df_produits['id_produit'].isin(id_produit_existant)]

id_magasin_existant = pd.read_sql("SELECT id_magasin FROM Magasins", conn)['id_magasin'].tolist()
df_magasins = df_magasins[~df_magasins['id_magasin'].isin(id_magasin_existant)]



# Insertion des données en dans la base de données SQlite
df_produits.to_sql('Produit', conn, if_exists='replace', index=False)
df_magasins.to_sql('Magasins', conn, if_exists='replace', index=False)
df_ventes.to_sql('vente', conn, if_exists='append', index=False)




conn.commit()
conn.close()