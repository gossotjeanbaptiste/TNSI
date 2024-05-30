matrice_adj = [[0, 1, 1, 0, 1, 1, 0, 0],
               [1, 0, 1, 1, 1, 0, 0, 1],
               [1, 1, 0, 1, 1, 1, 1, 0],
               [0, 1, 1, 0, 1, 0, 0, 0],
               [1, 0, 1, 1, 0, 0, 0, 0],
               [1, 0, 1, 1, 0, 0, 1, 0],
               [0, 0, 1, 0, 1, 0, 0, 0],
               [0, 1, 0, 0, 0, 0, 0, 0]]

sommets = ['G', 'J', 'Y', 'E', 'N', 'M', 'A', 'L']

def position(liste, sommet):
    for i in range(len(liste)):
        if liste[i] == sommet:
            return i
    return None

def nb_amis(L, m, s):
    pos_s = position(L, s)
    if pos_s is None:
        return None
    amis = 0
    for i in range(len(m)):
        amis += m[pos_s][i]
    return amis

print(nb_amis(sommets, matrice_adj, 'G'))