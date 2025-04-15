-- Section pour la création des tables

--Table Produits
CREATE TABLE IF NOT EXISTS Produits (
    id_produit TEXT PRIMARY KEY,
    nom TEXT,
    prix REAL,
    stock INT
)

--Table Magasins
CREATE TABLE IF NOT EXISTS Magasins (
    id_magasin TEXT PRIMARY KEY,
    ville TEXT,
    Nb_salarie INT
)

--Table Ventes
CREATE TABLE IF NOT EXISTS Ventes (
    id_vente INTEGER PRIMARY KEY AUTOINCREMENT,
    id_produit TEXT,
    id_magasin TEXT,
    date_vente TEXT,
    quantite INTEGER,
    FOREIGN KEY(id_produit) REFERENCES Produit(id_produit),
    FOREIGN KEY(id_magasin) REFERENCES Magasins(id_magasin)
    --,    UNIQUE(id_produit, id_magasin, date_vente)
)

--Table Analyse (Pour enregistrer les anlyser à partir des requêtes du script "analyse.py")
CREATE TABLE IF NOT EXISTS Analyse (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date_analyse TEXT,
    type_analyse TEXT,
    resultat TEXT
)


-- Section pour les analyses

--Calcul du chiffre d'affaire total (Prix X Qté)
SELECT SUM(V.quantite * P.prix) AS chiffre_affaires_total
FROM Ventes V
JOIN Produits P ON V.id_produit = P.id_produit


--Ventes par produit
SELECT V.id_produit, COUNT (quantite) as Nombre_vendu
FROM Ventes V
JOIN Produits P ON V.id_produit = P.id_produit
GROUP BY V.id_produit
ORDER BY Nombre_vendu DESC

--Ventes par région