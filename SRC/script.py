#Imports
import pandas as pd
import sqlite3

# Connexion à la base de données SQLite "pme"
conn = sqlite3.connect("pme.db")
cursor = conn.cursor()


#csv to df
magasins=pd.read_csv('Data/magasins.csv', delimiter=',', index_col=0)
produits=pd.read_csv('Data/produits.csv', delimiter=',', index_col=1)
ventes=pd.read_csv('Data/ventes.csv', delimiter=',')
