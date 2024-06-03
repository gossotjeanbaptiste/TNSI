def couples_consecutifs(tab):
    list = []
    for i in range(len(tab)-1):
        if tab[i+1] - tab[i] == 1:
            list.append((tab[i], tab[i+1]))
    return list

print(couples_consecutifs([1, 4, 3, 5]))
print(couples_consecutifs([1, 4, 5, 3]))
print(couples_consecutifs([1, 1, 2, 4]))
print(couples_consecutifs([7, 1, 2, 5, 3, 4]))
print(couples_consecutifs([5, 1, 2, 3, 8, -5, -4, 7]))

def colore_comp1(M, i, j, val):
    if M[i][j] != 1:
        return

    M[i][j] = val

    if i-1 >= 0: # propage à gauche
        colore_comp1(M, i-1, j, val)
    if i+1 < len(M): #propage à droite 
        colore_comp1(M, i+1, j, val) 
    if j-1 >= 0: # propage en haut
        colore_comp1(M, i, j-1, val) 
    if j+1 < len(M[0]):
        colore_comp1(M, i, j+1, val)


M = [[0, 0, 1, 0], [0, 1, 0, 1], [1, 1, 1, 0], [0, 1, 1, 0]]
colore_comp1(M, 2, 1, 3)

print(M)
