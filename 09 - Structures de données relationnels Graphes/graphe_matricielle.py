graph_proba = [[0.1, 0.5, 0.4],
               [0, 0.35, 0.65],
               [0.8, 0, 0.2]]

graph_ex2 = [[0, 1, 1, 0, 1, 0, 0, 0],
             [1, 0, 1, 0, 0, 0, 0, 0],
             [1, 1, 0, 1, 0, 0, 0, 0],
             [0, 0, 1, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 1, 0, 1, 0],
             [0, 0, 0, 0, 0, 1, 0, 1],
             [0, 0, 0, 1, 0, 0, 1, 0]]

def est_dans(matrice, v):
    colonne = len(matrice[0])
    return 0 <= v < colonne

def voisins(matrice, n):
    if est_dans(matrice, n):
        reponse = []
        for num, poids in enumerate(matrice[n]):
            if num != 0:
                reponse.append(num)
    return reponse
    
print(voisins(graph_proba, 1))