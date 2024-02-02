def recherche_min(tab):
    min = tab[0]
    indice = 0
    for i in range(1, len(tab)):
        if tab[i] < min:
            min = tab[i]
            indice = i
    return indice, min

print(recherche_min([1, 8, 5, 6, 0, 4, 9, -2]))

assert recherche_min([1, 8, 5, 6, 0, 4, 9, -2]) == 7, 'Il y a un problème au test 1'
print('Test 1 concluant')

assert recherche_min([2, 4, 1]) == 2, 'Il y a un problème au test 2'
print('Test 2 concluant')

