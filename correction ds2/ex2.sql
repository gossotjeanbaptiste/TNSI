--1) 
--a) une clé étrangère est un attribut d'une relation qui fait référence à 
--une clé primaire d'une autre relation
--b) rendu pour etre un booléen et par défaut a False 

--2)
--a) Si l'id servant de clé primaire existe déjà ou déjà dans la base, 
--il sera impossible d'inserer le nouvelle enregistrement
--b) 
INSERT INTO EMPRUNT(nom, prénom, classe, dateDebutEmprunt, dateRetourMax, rendu, idOuvrage)
VALUES(0, "MICHEL", "Tom", "T10", 2023-11-20, 2023-12-04, False, "DRE-101-A")

--3)
--a) * --> tout les attributs de la table 
SELECT * 
FROM OUVRAGE
WHERE disponible = 'True' --ou disponible = 1 

--b)

DELETE
FROM OUVRAGE
WHERE idOuvrage = "FTR-452-TT"

--c) 

SELECT (prenom, nom, classe)
FROM EMPRUNT
JOIN OUVRAGE ON EMPRUNT.idOuvrage = OUVRAGE.idOuvrage
WHERE dateRetourMax > 2022-12-31 AND dateRetourMax < 2024-01-01 AND titre = "Le vieil homme et la mer"

