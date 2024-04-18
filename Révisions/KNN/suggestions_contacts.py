import csv


# Politique,Sport,Lecture,Art,Cuisine,Voyage,Jeux_Video,Musique,Animaux,Username

with open('reseaux_sociaux.csv', newline='\n') as csvfile:
    data = csv.reader(csvfile, delimiter=',')
    titre = next(data)
    donnees = []
    for row in data:
        donnees.append([int(row[i]) for i in range(9)]
                        + [row[9]])


'''Votre travail demandez à un utilisateur ses goûts une note entre 
    0 et 10 pour chacune des catégories Politique,Sport,Lecture,Art,
    Cuisine,Voyage,Jeux,Video,Musique,Animaux
    Puis lui proposer trois suggestions d'éventuels amis qui auraient 
    les goûts les plus proches.
    Vous testerez votre scripts avec 
    M_Kbida = [8, 5, 3,1,7,9,2,5,3]
 '''


