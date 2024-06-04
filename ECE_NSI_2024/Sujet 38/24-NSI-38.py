# ! a revoir

def indices_maxi(tab):
    # Initialisation du maximum avec le premier élément
    maxi = tab[0]
    indices = []
    # Première boucle pour trouver le maximum
    for value in tab:
        if value > maxi:
            maxi = value
    # Deuxième boucle pour trouver les indices du maximum
    for i in range(len(tab)):
        if tab[i] == maxi:
            indices.append(i)
    return (maxi, indices)


# Exemples d'utilisation
print(indices_maxi([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]))  # (9, [3, 8])
print(indices_maxi([7]))  # (7, [0])


def renverse(pile):
    '''renvoie une pile contenant les mêmes éléments que pile,
    mais dans l'ordre inverse.
    Cette fonction détruit pile.'''
    pile_inverse = [] 
    while pile != []:
        pile_inverse.append(pile.pop()) 
    return pile_inverse


def positifs(pile):
    '''renvoie une pile contenant les éléments positifs de pile,
    dans le même ordre. Cette fonction détruit pile.'''
    pile_positifs = []
    while pile != []:
        element = pile.pop() 
        if element >= 0: 
            pile_positifs.append(element)
    return pile_positifs


print(renverse([1, 2, 3, 4, 5]))
print(positifs([-1, 0, 5, -3, 4, -6, 10, 9, -8]))
print(positifs([-2]))

