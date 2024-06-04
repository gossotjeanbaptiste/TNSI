# ! a revoir

def indice_maxi(tab):
    '''renvoie maxi le plus grand element du tab
    et indices une liste des indices de maxi dans tab'''
    maxi = tab[0]
    indices = [0]
    for i in range(len(tab)):
        if tab[i] > maxi:
            maxi = tab[i]
            if maxi == tab[i]:
                indices.append(i)
    return maxi, indices

print(indice_maxi([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]))
print(indice_maxi([7]))

def renverse(pile):
    pass
    '''renvoie une pile contenant les mêmes éléments que pile,
    mais dans l'ordre inverse.
    Cette fonction détruit pile.
    pile_inverse = ... 
    while pile != []:
        ... .append(...) 
    return ...''' 


def positifs(pile):
    pass
    '''renvoie une pile contenant les éléments positifs de pile,
    dans le même ordre. Cette fonction détruit pile.
    pile_positifs = ... 
    while pile != []:
        ... = pile.pop() 
        if ... >= 0: 
            ...
    return ...'''


