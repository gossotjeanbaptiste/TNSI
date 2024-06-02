def multiplication(n1, n2):
    # Si l'un des nombres est zéro, le produit est zéro
    if n1 == 0 or n2 == 0:
        return 0
    # Déterminer le signe du résultat
    signe = 1
    if (n1 < 0 and n2 > 0) or (n1 > 0 and n2 < 0):
        signe = -1
    # Travail avec des valeurs absolues pour faciliter l'addition répétée
    n1 = abs(n1)
    n2 = abs(n2)
    # Ajouter n1 à lui-même n2 fois
    produit = 0
    for _ in range(n2):
        produit += n1
    # Appliquer le signe au résultat final
    if signe == -1:
        produit = -produit
    return produit


print(multiplication(3, 5))
print(multiplication(-4, -8))
print(multiplication(-2, 6))
print(multiplication(-2, 0))


def chercher(tab, x, i, j):
    '''Renvoie l'indice de x dans tab, si x est dans tab, 
    None sinon.
    On suppose que tab est trié dans l'ordre croissant.'''
    if i > j:
        return None
    m = (i + j) // 2
    if tab[m] < x:
        return chercher(tab, x, m + 1, j)
    elif tab[m] > x:
        return chercher(tab, x, i, m - 1)
    else:
        return m


print(chercher([1, 5, 6, 6, 9, 12], 7, 0, 10))
print(chercher([1, 5, 6, 6, 9, 12], 7, 0, 5))
print(chercher([1, 5, 6, 6, 9, 12], 9, 0, 5))
print(chercher([1, 5, 6, 6, 9, 12], 6, 0, 5))
