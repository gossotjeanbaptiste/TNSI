stock = {"bananes" : [20, 3.5], "pommes" : [8, 3.5], "marrons" : [12, 9.90]}
"""méthode .keys() donne la liste des clés
méthode .values() donne la liste des valeurs
méthode .items() donne la liste des couples (clé, valeur)
1) stock.keys
2) stock['orange'] = [35, 2]
#les dictionnaires ne sont pas ordonnées donc on ne peut pas faire de slicing (pas sequentiel)"""


def max_quantite():
    quantite_max = 0
    fruit_max = ""
    for fruit, info in stock.items(): 
        #fruit est une chaine de caractère et info est une liste[qte, prix]
        if info[0] > quantite_max:
            quantite_max = info[0]
            fruit_max = fruit
    return (fruit_max, quantite_max)

#3 La fonction mystère modifie le prix au kg de l'article a le passant à b€

def mystere(a, b):
    stock[a][1] = b
    
#4
def prix_panier(tableau):
    total = 0
    for produit, qte in tableau:
        total += stock[produit][1]*qte
    return total