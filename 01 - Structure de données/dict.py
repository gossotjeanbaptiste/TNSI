#déclaration et création de dictionnaire vide

le_larousse = {  }

#déclaration et création de dictionnaire non vide

le_petit_robert = { "table" : 79.9 , 'four' : 50, 'set_couvert_argent' : 150}

#methodes items() keys() values() pour parcourir un dico

for prix in le_petit_robert.values():
    print(prix)
print('*******************')

for objet in le_petit_robert.keys():
    print(objet)
print('*******************')

for objet, prix in le_petit_robert.items():
    print(f'{objet} : {prix} €')
print('*******************')

# values() retourne une liste de valeurs
# keys() retourne une liste de clés
# items() retourne une liste de tuples (clé, valeur)

#mise a jour et suppression d'éléments

le_petit_robert['four'] = 199.99
del(le_petit_robert['table'])

#del() supprime un élément du dictionnaire ou une variable