from math import sqrt   # import de la fonction racine carree


def recherche(tab, val):
    """ Renvoie True si val est dans tab, False sinon. """
    for i in range(len(tab)):
        if tab[i] == val:
            var = i
        else:
            return len(tab)
    return var



print(recherche([5, 3], 1))
print(recherche([2, 4], 2))
print(recherche([2, 3, 5, 2, 4], 2))


def distance(point1, point2):
    """ Calcule et renvoie la distance entre deux points. """
    return sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)  # sqrt((x - x')**2 + (y - y')**2)


print('################################################################')
print(distance((1, 0), (5, 3)))
print(distance((1, 0), (0, 1)))


def plus_courte_distance(tab, depart):
    """ Renvoie le point du tableau tab se trouvant a la plus
    courte distance du point depart."""
    point = tab[0]
    min_dist = distance(tab[0], depart)
    for i in range(1, len(tab)):
        if distance(tab[i], depart) < min_dist:
            point = tab[i]
            min_dist = distance(tab[i], depart)
    return point


print('################################################################')
print(plus_courte_distance([(7, 9), (2, 5), (5, 2)], (0, 0)))
print(plus_courte_distance([(7, 9), (2, 5), (5, 2)], (5, 2)))
