import time
from random import randint
from matplotlib import pyplot as plt

def nbr_occurences(chaine):
    resultat = {}
    for lettre in chaine:
        # si la lettre est rencontrée pour la première fois
        if lettre in resultat.keys():
            resultat[lettre] += 1
        # si la lettre a déjà été rencontrée
        else:
            resultat[lettre] = 1
    return resultat

#print(nbr_occurences("Hello World !"))



def fusion(lst1, lst2):
    n1 = len(lst1)
    n2 = len(lst2)
    lst12 = [0] * (n1 + n2)
    i1 = 0
    i2 = 0
    i = 0
    while i1 < n1 and i2 < n2 :
        if lst1[i1] < lst2[i2]:
            lst12[i] = lst1[i1]
            i1 += 1
        else:
            lst12[i] = lst2[i2]
            i2 += 1
        i += 1
    while i1 < n1:
        lst12[i] = lst1[i1]
        i1 = i1 + 1
        i += 1
    while i2 < n2:
        lst12[i] = lst2[i2]
        i2 = i2 + 1
        i += 1
    return lst12


#print(fusion([1, 6, 10], [0, 7, 8, 9]))


def tri_fusion(tab):
    if len(tab) <= 1:
        return tab
    else:
        n = len(tab)//2
        return fusion(tri_fusion(tab[:n]), tri_fusion(tab[n:]))
    
#print(tri_fusion([9, 4, 5, 7, 1, 3, 2, 8]))


def tri_selection(tab):
    """ docstring """
    n = len(tab)
    for i in range(n-1):
        indice_min = i

        for j in range(i+1, n):
            if tab[j] < tab[indice_min]:
                indice_min = j

        if indice_min != i:
            tab[i], tab[indice_min] = tab[indice_min], tab[i]
    return tab

'''
exemple = [randint(0, 100000) for _ in range(10000)]
start = time.time()
tri_fusion(exemple)
#exemple.sort()
print(f"Temps d'exécution : (Tri fusion) {(time.time() - start) * 1000:3F} ms")


start = time.time()
tri_selection(exemple)
print(f'Temps d\'exécution : (Tri par sélection) {(time.time() - start) * 1000:3F} ms')

'''

Y_fusion = []
X = [10, 100, 250, 500, 750, 1000, 2500, 5000, 7500, 10000]
for number in X:
    exemple = [randint(0, 1000) for _ in range(number)]
    start = time.time()
    tri_fusion(exemple)
    Y_fusion.append((time.time() - start) * 1000)
    
print(f'Tri fusion : {Y_fusion}')



Y_selection = []
X = [10, 100, 250, 500, 750, 1000, 2500, 5000, 7500, 10000]
for number in X:
    exemple = [randint(0, 1000) for _ in range(number)]
    start = time.time()
    tri_selection(exemple)
    Y_selection.append((time.time() - start) * 1000)
print(f'Tri selection : {Y_selection}')


plt.plot(X, Y_fusion, 'r-' ,label='Tri fusion')
plt.plot(X, Y_selection, 'b-' ,label='Tri selection')
plt.xlabel('Taille du tableau')
plt.ylabel('Temps d\'exécution (ms)')
plt.legend()
plt.show()

