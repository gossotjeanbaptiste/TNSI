# Cours de NSI de Terminal

## Année scolaire 2023-2024

Cours écrit par [@akbida](https://github.com/akbida) et certains par [@gossotjeanbaptiste](https://github.com/gossotjeanbaptiste)

Elève qui met en repo github : [GOSSOT Jean-Baptiste](https://github.com/gossotjeanbaptiste) en T05

Etape à suivre :

1) Télécharger et installer Python via [ce lien](https://www.python.org/downloads/) et ne pas oublier de cliquer sur ADD TO PATH à la fin de l'installation
2) Si vous ne disposez pas de Winget allez le télécharger sur [ce lien](https://aka.ms/getwinget) puis installer le.
3) Lancer le fichier "prérequis_librairie_python.bat"
4) Lancer le fichier "prérequis_logiciel_installer.bat"

Si durant l'installation de Python vous avez oubliez de l'ajoutez au PATH suivez cette méthode : 
1) Chercher `Modifier les variables d'environnement système`
2) Cliquer sur `Variables d'environnement...`
3) Double cliquer sur `Path` dans `Variables utilisateur pour <votre utilisateur>` 
4) Cliquez sur `Nouveau` et ajoutez `C:\Users\<votre utilisateur>\AppData\Local\Programs\Python\Python<Version>\Scripts\`
5) De même refaite la même chose comme ceci `C:\Users\<votre utilisateur>\AppData\Local\Programs\Python\Python<Version>\`
6) Refaites les trois étapes précédentes dans le `Path` du `Variables système`
7) ATTENTION NE SUPPRIMEZ AUCUNE VARIABLES OU LIGNE INTEGRER AU RISQUE DE CASSER QQCHOSE MISE A PART SI VOUS SAVEZ CE QUE VOUS FAITES !
8) Cliquez sur `OK` pour tout refermer
9) Rédemarrer votre PC
10) Vérifié que Python est bien détecté depuis n'importe où, ouvrez une ligne de commande et faite la commande `py -v` si c'est le cas cela devrait vous affichez quelque chose dans ce style `Python v<version> (tags/v<version>:<qqchose de quelconque>, <Date> , <heure>) [MSC v.1937 64 bit (AMD64)] on win32` avec ceci `>>>`, si ce n'est pas le cas il devrait afficher ceci `'py' n’est pas reconnu en tant que commande interne ou externe, un programme exécutable ou un fichier de commandes.`, si c'est le cas revoyez toutes vos étapes  

©JustWirelessInc 2021 - 2025

Librairie installé :

* MàJ de `pip`
* `networkx`
* `matplotlib`
* `jupyter`
* `Flask`
* `colorama`
* `icecream`
* `gTTS`
* `TKinter`
* `Custom TKinter`
* `pygame`

Logiciel installé :

* VS Code
* Visual Studio Community 2022
* Twinkle Tray
* Spotify
* Git
* PowerToys
* NodeJS
* Windows Subsystem for Linux
* Windows Terminal
* MySQL
* Wintoys

## 01 - Structure de données

Introduction au Pile et File (la stack), retour sur les listes et les dictionnaires

## 02 - Programmation Orienté Objet (POO)

Introduction à la POO, qu'est qu'un attribut, une classe etc...

## 03 - Base de données (BDD)

Introduction au language SQL et au base données, vu un peu de JSON également, retour sur la POO

## 04 - Réseaux et Algorithmes de routages

Utilisation de Filius, vu de la notation CIDR, notion d'IP, de masque de sous réseau, protocole de routage etc...

## 05 - Récursivité

Introduction à la notion de fonction qui s'appelle elle-même.

## 06 - Structures de données hiérarchiques (arbres)

Introduction au structure de données sous formes d'arbre, arbre binaire de recherche, retour sur la POO + Sujet 25 ECE 2023

## 07 - Système d'exploitation

Apprentisage des commandes essentiels du shell, gérer des processus (ordonnancement, état, priorité), Deadlock

## 08 - Diviser pour régner

Vu du slicing et du découpage de tableau pour formuler l'algorithme de tri le plus rapide : le tri fusion, ou faire de manière plus rapide le calcul d'une puissance d'un chiffre

## 09 - Structures de données relationnels Graphes

Introduction à la notion de graphe et de matrice pour utiliser des graphes matricielles, introduction des graphes pondérés, continuité informatique du cours de Maths Experts

## 10 - Recherche textuelle

Création de l'algorithme reprennant le principe du Ctrl+F

## 11 - Programmation dynamique

Technique qui permet de ne pas refaire des calculs

## 12 - Cryptographie & Sécurisation des communications

Introduction à la cryptographie, les clés, les algorithmes de chiffrement, les attaques, les protocoles de sécurisation des communications

Principe :

1) Doit etre mathématiquement indéchiffrable
2) Méthode de chiffrement doit être connu de l'expéditeur et du destinataire
3) La clé doit être connu que de l'expéditeur et du destinataire (clé simple à retenir)

## 13 - Calculabilité

Calculer sur les programmes
Utilisation du language Assembleur (celui le plus proche de la machine)

## 14 SoC (System on Chip) 

Introduction au notion de RAM, CPU, Carte Mère etc...
