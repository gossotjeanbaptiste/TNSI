def max_et_indice(tab):
    '''
    Renvoie le maximum et l'indice du maximum d'un tableau tab
    '''
    max = tab[0]
    indice = 0
    for i in range(1, len(tab)):
        if tab[i] > max:
            max = tab[i]
            indice = i
    return (max, indice)


print(max_et_indice([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]))
print(max_et_indice([-2]))
print(max_et_indice([-1, -1, 3, 3, 3]))
print(max_et_indice([1, 1, 1, 1]))


def est_un_ordre(tab):
    '''
    Renvoie True si tab est de longueur n et contient tous les
    entiers de 1 à n, False sinon
    '''
    n = len(tab)
    # les entiers vus lors du parcours
    vus = []
    for x in tab:
        if x < 1 or x > n:
            return False
        vus.append(x) 
    return True

def nombre_points_rupture(ordre):
    '''
    Renvoie le nombre de points de rupture de ordre qui représente
    un ordre de gènes de chromosome
    '''
    # on vérifie que ordre est un ordre de gènes
    assert est_un_ordre(ordre)
    n = len(ordre)
    nb = 0
    if ordre[0] != 1:  # le premier n'est pas 1
        nb += 1
    i = 0
    while i < (n - 1):
        if (ordre[i + 1] - ordre[i]) not in [-1, 1]:  # l'écart n'est pas 1
            nb += 1
        i += 1
    if ordre[i] != n:  # le dernier élément n'est pas n
        nb += 1
    return nb

# Tests des fonctions
print('---')
print(est_un_ordre([1, 6, 2, 8, 3, 7]))  # False
print(est_un_ordre([5, 4, 3, 6, 7, 2, 1, 8, 9]))  # True
print('---')
print(nombre_points_rupture([5, 4, 3, 6, 7, 2, 1, 8, 9]))  # 4
print(nombre_points_rupture([1, 2, 3, 4, 5]))  # 0
print(nombre_points_rupture([1, 6, 2, 8, 3, 7, 4, 5]))  # 7
print(nombre_points_rupture([2, 1, 3, 4]))  # 2


print('---')
print(est_un_ordre([1, 6, 2, 8, 3, 7]))
print(est_un_ordre([5, 4, 3, 6, 7, 2, 1, 8, 9]))
print('---')
print(nombre_points_rupture([5, 4, 3, 6, 7, 2, 1, 8, 9]))
print(nombre_points_rupture([1, 2, 3, 4, 5]))
print(nombre_points_rupture([1, 6, 2, 8, 3, 7, 4, 5]))
print(nombre_points_rupture([2, 1, 3, 4]))