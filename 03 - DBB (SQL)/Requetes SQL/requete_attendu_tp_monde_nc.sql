--2a) 
SHOW TABLES;

--2b)

DESCRIBE City;
DESCRIBE Country;
DESCRIBE CountryLanguage;

--2c)--

--l'attribut JOIN permet de joindre les tables entre elles 

--3a)--
SELECT Name
FROM Country
WHERE Continent = 'South America';

--3b)--
SELECT count(*)
FROM Country;

--3c)--

SELECT COUNT(DISTINCT GovernmentForm)
FROM country;

--3d)--

SELECT City.Name
FROM City
    JOIN Country ON City.CountryCode = Country.Code
WHERE Country.Continent = 'Europe' AND City.Population >= 2000000;

--3e)--

SELECT name
FROM City
WHERE name LIKE 'Pa%';

--3f)--

--donnez tous les pays ou l'on parle francais-- 

SELECT Country.Name
FROM Country
    JOIN CountryLanguage on CountryLanguage.CountryCode =Country.Code
WHERE CountryLanguage.Language = 'French';

--3g)--

--donnez les pays d'amérique du sud ayant de plus de 10 000 000 hab et un regime républicain--

SELECT name, GovernmentForm
FROM Country
WHERE Continent = 'South America'
    AND Population >= 10000000
    AND GovernmentForm LIKE '%Republic%';

--3h)--
--donnez la surface de la Polynésie--

SELECT Name, SurfaceArea
FROM Country
WHERE Name = 'French Polynesia';

--3i)--

--donnez la population moyenne dans les pays d'Asie--

SELECT AVG(Population)
FROM Country
WHERE Continent = 'Asia';

--3j)--

--Donnez le nombre de pays en Océanie de plus de 10000km²--

SELECT COUNT(*)
FROM Country
WHERE Continent = 'Oceania'
    AND SurfaceArea >= 10000;

--3k)--

--donnez les pays pour lesquels au moins une ville est repertorier--

SELECT COUNT(DISTINCT Country.Name)
FROM Country
    JOIN City ON City.CountryCode = Country.Code;

--3l)--

--donnez les villes de plus de 100000 habitants de pays nord américain ou l'on parle espagnol--

SELECT City.Name, Country.Code, City.Population
FROM Country
    JOIN City ON City.CountryCode = Country.Code
    JOIN CountryLanguage ON CountryLanguage.CountryCode = Country.Code
WHERE Country.Continent = 'North America'
    AND CountryLanguage.Language = 'Spanish'
    AND City.Population > 100000
ORDER BY Country.Code, City.Population;

--3m)--

--Donnez les pays pour lesquels au moins une ville est répertoriée dans la base--

SELECT COUNT(DISTINCT Country.Name)
FROM Country
    JOIN City ON City.CountryCode = Country.Code;

--3n)--

--Donnez le pays asiatique ayant l’espérance de vie la plus courte--

SELECT Name, LifeExpectancy
FROM Country
WHERE Continent = 'Asia'
ORDER BY LifeExpectancy

--3o)--

-- Donnez les pays pour lesquels plus de 49 villes sont répertoriées dans la base--

SELECT Country.Name, COUNT(City.Name)
FROM Country
    JOIN City ON City.CountryCode = Country.Code
GROUP BY Country.Name
HAVING COUNT(City.Name) > 49;

--3p)--

--Donnez les pays dont toutes les villes répertoriées dans la base ont plus de 100000 habitants--

SELECT Country.Name
FROM Country
    JOIN City ON City.CountryCode = Country.Code
WHERE City.Population > 100000
GROUP BY Country.Name;

--3q)--

-- Donnez les pays pour lesquels la somme du nombre d’habitants de ses villes est supérieure à 10 000 000 habitants.--

SELECT Country.Name, SUM(City.Population)
FROM Country
    JOIN City ON City.CountryCode = Country.Code
GROUP BY Country.Name
HAVING SUM(City.Population) > 10000000
ORDER BY Country.Name;

--3r)--

--Donnez les pays où l'on parle français mais pas anglais-- 

SELECT Country.Name
FROM Country
    JOIN CountryLanguage ON CountryLanguage.CountryCode = Country.Code
WHERE CountryLanguage.Language = 'French'
    AND CountryLanguage.Language != 'English'
    ORDER BY Country.Name;

