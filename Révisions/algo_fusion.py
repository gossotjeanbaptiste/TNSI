# * algo fusion -> on a deux listes triées il faut renvoyer la liste des deux listes triés

def algo_fusion(liste1:list, liste2:list) -> list:
    resultat = []
    n = len(liste1)
    m = len(liste2)
    i = 0
    j = 0
    while i < n and j < m:
        if liste1[i] < liste2[j]:
            resultat.append(liste1[i])
            i += 1
        else:
            resultat.append(liste2[j])
            j += 1
    return resultat + liste1[i:] + liste2[j:]

A = [4, 6, 9, 11]
B = [1, 3, 5, 7]

print(algo_fusion(A, B))