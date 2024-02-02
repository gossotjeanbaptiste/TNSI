import csv

#with open('prenom.csv', 'r') as fichier:
#        texte = fichier.readlines()

with open('prenom.csv', 'r', encoding="utf-8") as fichier:
        texte = csv.DictReader(fichier)
        dico_prenom = {}
        for ligne in texte:
                if ligne['Prénom'] in dico_prenom.keys():
                        #incremente de 1
                        dico_prenom[ligne["Prénom"]] += 1
                else:
                        #on initialise à 1
                        dico_prenom[ligne['Prénom']] = 1
                        
        def recherche(prenom):
                if prenom in dico_prenom.keys():
                        return f"{prenom} : {dico_prenom[prenom]}"
                else:
                        return None
 
