def recherche_min(tab):
    '''Renvoie l'indice du minimum de tab'''
    min = tab[0]
    indice = 0
    for i in range(1, len(tab)):
        if tab[i] < min:
            min = tab[i]
            indice = i
    return indice


def separe(tab):
    '''Separe les 0 et les 1 dans le tableau tab'''
    gauche = 0
    droite = len(tab) - 1 
    while gauche < droite:
        if tab[gauche] == 0 :
            gauche = gauche + 1 
        else :
            tab[gauche] =  0
            tab[droite] = 1 
            droite = droite - 1 
    return tab


print(separe([1, 0, 1, 0, 1, 0, 1, 0]))
