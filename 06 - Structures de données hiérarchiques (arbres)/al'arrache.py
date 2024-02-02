#première tentative d'implémentation d'une structure d'arbre
# 
abr1 = ['Attaquer', [], []]
abr2 = ['Défendre', [], []]
comb = ['Combattre', abr1, abr2]
fuir = ['Fuir', [], []]


arbre_jdr = ["Action", comb, fuir]

def parcours(arbre):
    #parcours recursive d'un arbre pcqu'il s'appelle lui même
    sommet, gauche, droite = arbre
    print(f'{sommet}, ', end=" ")
    if gauche:
        parcours(gauche)
    else:
        print('∅', end=" ")
    if droite:
        parcours(droite)
    else:
        print('∅', end=" ")
