def fonction1(tab, i):
    nb_elem = len(tab)
    cpt = 0
    for j in range(i+1, nb_elem):
        if tab[j] < tab[i]:
            cpt +=1
    return cpt


print(f'Cas 1 : {fonction1([1, 5, 3, 7], 0)}')

print(f'Cas 2 : {fonction1([1, 5, 3, 7], 1)}')

print(f'Cas 3 : {fonction1([1, 5, 2, 6, 4], 1)}')
