--SGBD : Système de Gestion de Base de Données--

--Logiciel intermédiaire entre l'utilisateur et la base de données-- 

--Gère les accès simultanées permet la cohérence et la sécurité des données-- 

--Ex : MySQL, Oracle, SQL Server, PostgreSQL, SQLite, Access, etc...--

--SQL : Structured Query Language--

--Langage de requête structurée--

--Le SGBD permet d'éviter de faire n'importe quoi--

--Inserer un enregistrement avec une clé primaire déjà existante (le sgbd permet d'éviter ceci)--

------------------------------------------------------------------------------------------------------------------------------

--Modèle relationnel :--

--Utilisation de principes mathématiques(Théorie des ensembles) Etgar Codd--

--Savoir faire Relation/Entité/Attribut/Clé Primaire/Clé étrangère/Schéma Relationnel--

--Relation : Table--

--Entité : Table--

--Attribut : Colonne--

--Clé Primaire : Identifiant unique d'un enregistrement--

--Clé étrangère : Identifiant d'un enregistrement d'une autre table--

--Schéma Relationnel : Ensemble de tables--


------------------------------------------------------------------------------------------------------------------------------

--DDL : Data Definition Language (pas au programme)--

--Tout ce qui permet de créer, modifier et supprimer--

--CREATE, ALTER, DROP--

------------------------------------------------------------------------------------------------------------------------------

--DML : Data Manipulation Language (à savoir)--

--Tout ce qui permet de manipuler les données--

--Inserer, selectionner, modifier, supprimer--

--INSERT, SELECT, UPDATE, DELETE--

--Exemple--

INSERT INTO `cinema` (`
idCinema`,`nom
`, `ville`, `nombreDeSalles`) 
VALUES
(1, 'UGC Ciné cité', 'Ludres', 14);

UPDATE cinema
SET ville = 'Maxéville'
WHERE nom = "L'Impérial";
--Exemple repris du fichier 'cinema_utf8.sql' sur le chemin relatif 'BDD et POO'--

DELETE 
FROM nom_table
where id_truc = 8;
--Exemple quelconque et généraliste--

UPDATE espece
SET classe = "mammifères"
WHERE nom_espece = "ornithorynque";
--Exemple de la correction du BAC Sujet 2 NSI 2023 Métropole--

--Requête de base--

SELECT Liste-Attributs
FROM Liste
-Tables
WHERE condition
ORDER BY Liste-Attributs;
--Exemple quelconque et généraliste de la requête de base--

SELECT nom
FROM cinema
WHERE ville = 'Nancy'
ORDER BY nb_salles; 
--Exemple repris du fichier 'cinema_utf8.sql' sur le chemin relatif 'BDD et POO' --

------------------------------------------------------------------------------------------------------------------------------