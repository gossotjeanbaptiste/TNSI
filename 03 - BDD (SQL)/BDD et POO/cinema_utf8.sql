/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `CINEMA`
--

-- --------------------------------------------------------

--
-- Structure de la table `cinema`
--

CREATE TABLE `cinema` (
  `idCinema` int NOT NULL,
  `nom` varchar(50) NOT NULL,
  `ville` varchar(50) NOT NULL,
  `nombreDeSalles` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `cinema`
--

INSERT INTO `cinema` (`idCinema`, `nom`, `ville`, `nombreDeSalles`) VALUES
(1, 'UGC Ciné cité', 'Ludres', 14),
(2, 'CinéLun', 'Lunéville', 5),
(3, 'Kinépolis', 'Nancy', 18),
(4, 'L\'Impérial', 'Maxéville', 5),
(5, 'Caméo', 'Nancy', 7);

-- --------------------------------------------------------

--
-- Structure de la table `film`
--

CREATE TABLE `film` (
  `idFilm` int NOT NULL,
  `nom` varchar(50) NOT NULL,
  `dateDeSortie` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `film`
--

INSERT INTO `film` (`idFilm`, `nom`, `dateDeSortie`) VALUES
(1, 'L\'armée des douzes singes', '1995-10-05'),
(2, 'Contagion', '2011-12-06'),
(3, '28 jours plus tard', '2002-02-10'),
(4, 'World War Z', '2013-02-10');

-- --------------------------------------------------------

--
-- Structure de la table `seance`
--

CREATE TABLE `seance` (
  `idseance` int NOT NULL,
  `horaire` time DEFAULT NULL,
  `idFilm` int DEFAULT NULL,
  `idCinema` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `seance`
--

INSERT INTO `seance` (`idSeance`, `horaire`, `idFilm`, `idCinema`) VALUES
(1, '14:00:00', 3, 3),
(2, '10:00:00', 2, 1),
(3, '17:00:00', 2, 2),
(4, '14:00:00', 1, 1),
(5, '11:30:00', 3, 2),
(6, '16:00:00', 1, 5),
(7, '21:00:00', 3, 5),
(8, '14:00:00', 2, 2);

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `cinema`
--
ALTER TABLE `cinema`
  ADD PRIMARY KEY (`idCinema`);

--
-- Index pour la table `film`
--
ALTER TABLE `film`
  ADD PRIMARY KEY (`idFilm`);

--
-- Index pour la table `seance`
--
ALTER TABLE `seance`
  ADD PRIMARY KEY (`idSeance`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
