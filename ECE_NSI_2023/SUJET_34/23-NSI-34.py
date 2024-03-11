def moyenne(tab):
    somme = 0
    if not tab:
        return None
    for i in range(len(tab)):
        somme = somme + tab[i]
    return somme / len(tab)

print(moyenne([]))
print(moyenne([5, 3, 8]))
print(moyenne([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


def tri(tab):
    # i est le premier indice de la zone non triee,
    # j est le dernier indice de cette zone non triée.
    # Au debut, la zone non triee est le tableau complet.
    i = 0
    j = len(tab)-1
    while i != j:
        if tab[i] == 0:
            i = i + 1
        else:
            valeur = tab[j]
            tab[j] = tab[i]
            tab[i] = valeur
            j = j - 1
    return tab


print(tri([0, 1, 0, 1, 0, 1, 0, 1, 0]))
