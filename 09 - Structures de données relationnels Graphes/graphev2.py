michel = {"1" : ["2", "5", "8"],
          "2" : ["3"],
          "3" : ["1", "4"],
          "4" : ["8"],
          "5" : ["6"],
          "6" : [],
          "7" : ["6"],
          "8" : ["7"]
}

# Répresentation d'un graphe sous forme de liste d'adjancence


def est_dans(G, v):
    return v in G.keys()


def voisins(G, v):
    if est_dans(G, v):
        return [sommet for sommet in G[v]]
    else:
        return []


def ajouter_sommet(G, v):
    if not est_dans(G, v):
        G[v] = []


def supprimer_sommet(G, v):
    if est_dans(G, v):
        del G[v]
        for sommet in G.keys():
                G[sommet].remove((v))


def ajouter_arc(G, v1, v2):
    if est_dans(G, v1) and est_dans(G, v2):
        G[v1].append(v2)
        G[v2].append(v1)


def supprimer_arc(G, v1, v2):
    if est_dans(G, v1) and est_dans(G, v2):
        G[v1].remove(v2)





