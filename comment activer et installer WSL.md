# Comment avoir WSL
WSL -> Windows Subsystem for Linux

## ATTENTION VEUILLEZ BIEN AVOIR ACTIVER LA VIRTUALISATION SUR VOTRE ORDINATEUR : Si ce n'est pas le cas il faut l'activer dans le BIOS de l'ordinateur

Comment savoir si la virtualisation est activé sur son ordinateur ? 

1) Ouvrir gestionnaires de tâches (Ctrl + MAJ + Echap)
2) Sur Windows 10 si celui-ci n'a jamais été ouvert cliquer sur "Afficher plus" ou "Plus de détail" (C'est l'un des deux textes)
3) Aller dans l'onglet "Performances"
4) Aller dans l'onglet "Processeur"
5) En dessous du graphique vous allez pouvoir retrouver des informations plus ou moins utiles il faut chercher pour "Virtualisation"
6) Vérifier que "Virtualisation" soit sur "Activé"
7) Si ce n'est pas le cas je vous envoie plus bas vers "Comment activer la virtualisation sur les PC Grand Est"

---

Comment activer la virtualisation sur les PC Grand Est

1) Pour skiper toutes étapes et aller directement à l'étape 8 éxécuté la commande `shutdown.exe /r /fw /t 1` dans un terminal ADMINISTRATEUR (Powershell, CMD, Invite de commande, qu'importe...).
1) Ouvrir les paramètres
2) Allez sur l'onglet "Windows Update"
3) Allez sur "Options avancées"
4) Allez sur "Récupération"
5) Sélectionner "Démarrage avancé"
6) Sélectionner "Dépannage"
7) Changer les paramètres du microprogramme UEFI -> Redémarrer
8) Appuyer sur F10 ou la touche qui dis "Bios SETUP"
9) Allez sur "Configuration"
10) Activer "Virtualization Technology" -> Enable
11) Allez sur "Exit"
12) Sortez du BIOS en faisant "Save changes and exit"

---
1) Rechercher "Fonctionnalités" -> "Activer ou désactiver des fonctionnalités Windows"
2) Dans le panneau chercher le fichier "Sous système Windows pour Linux" en français ou "Windows Subsystme for Linux"
4) Redemarrer votre PC
5) Taper dans une CMD "wsl --install"
6) Créer votre utilisateur et votre mot de passe pour Ubuntu
7) Bien jouer vous avez installé une ligne de commande Linux.
