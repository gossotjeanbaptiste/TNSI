"""Un arbre binaire est soit vide, représenté en Python par la valeur None, soit un nœud
représenté par un triplet(g, x, d) où x est l’étiquette du nœud et g et d sont les sousarbres gauche et droit.
On souhaite écrire une fonction parcours_largeur qui prend en paramètre un arbre
binaire et qui renvoie la liste des étiquettes des nœuds de l’arbre parcourus en largeur."""
# * Ex1:
from collections import deque


def parcours_largeur1(arbre, file=None, resultat=None):
    """
    Perform a breadth-first traversal of a binary tree.

    Args:
        arbre: The binary tree to traverse.
        file: The queue used for traversal. If not provided, a new queue will be created.
        resultat: The list to store the traversal result. If not provided, a new list will be created.

    Returns:
        The list containing the traversal result.

    """
    if file is None:
        file = deque([arbre])
    if resultat is None:
        resultat = []
    if not file:
        return resultat
    noeud = file.popleft()
    resultat.append(noeud[1])
    if noeud[0] is not None:
        file.append(noeud[0])
    if noeud[2] is not None:
        file.append(noeud[2])
    return parcours_largeur1(arbre, file, resultat)


arbre = (((None, 1, None), 2, (None, 3, None)),
         4, ((None, 5, None), 6, (None, 7, None)))

print(parcours_largeur1(arbre))  # * à obtenir [4, 2, 6, 1, 3, 5, 7]


# ! a savoir refaire les algos de parcours d'arbre en infixe/suffixe/préfixe et largeur
def parcours_largeur2(arbre):
    file = [arbre]
    liste_valeurs = []
    while file:
        temp = file.pop(0)
        liste_valeurs.append(temp[1])
        if not (temp[0] == None):
            file.append(temp[0])
        if not (temp[2] == None):
            file.append(temp[2])
    return liste_valeurs


# * Ex2:
def somme_max(tab):
    n = len(tab)
    sommes_max = [0]*n
    sommes_max[0] = tab[0]
    # on calcule la plus grande somme se terminant en i
    for i in range(1, n):
        if sommes_max[i-1] + tab[i] > tab[i]:
            sommes_max[i] = sommes_max[i-1] + tab[i]
        else:
            sommes_max[i] = tab[i]
    # on en déduit la plus grande somme de celles-ci
    maximum = 0
    for i in range(1, n):
        if sommes_max[i] > sommes_max[maximum]:
            maximum = i
    return sommes_max[maximum]


print(somme_max([1, 2, 3, 4, 5]))
print(somme_max([1, 2, -3, 4, 5]))
print(somme_max([1, 2, -2, 4, 5]))
print(somme_max([1, -2, 3, 10, -4, 7, 2, -5]))
