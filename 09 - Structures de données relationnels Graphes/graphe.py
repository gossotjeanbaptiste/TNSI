transport = {"Paris": [("Strasbourg", 490), ("Brest", 592), ("Lyon", 546)],
             "Brest": [("Paris", 592), ("Nantes", 295)],
             "Nantes": [("Brest", 295)],
             "Lyon": [("Paris", 546)],
             "Strasbourg": [("Paris", 490)],
             }

# Répresentation d'un graphe sous forme de liste d'adjancence


def est_dans(G, v):
    return v in G.keys()


def voisins(G, v):
    if est_dans(G, v):
        return [sommet for sommet, poids in G[v]]
    else:
        return []


def ajouter_sommet(G, v):
    if not est_dans(G, v):
        G[v] = []


def supprimer_sommet(G, v):
    if est_dans(G, v):
        del G[v]
        for sommet in G.keys():
            for v1, poids in G[sommet]:
                if v1 == v:
                    G[sommet].remove((v1, poids))


def ajouter_arc(G, v1, v2, poids):
    if est_dans(G, v1) and est_dans(G, v2):
        G[v1].append((v2, poids))
        G[v2].append((v1, poids))


def supprimer_arc(G, v1, v2):
    if est_dans(G, v1) and est_dans(G, v2):
        for v, poids in G[v1]:
            if v == v2:
                G[v1].remove((v, poids))
        for v, poids in G[v2]:
            if v == v1:
                G[v2].remove((v, poids))


ajouter_sommet(transport, "Nancy")
ajouter_arc(transport, "Nancy", "Lyon", 445)
ajouter_arc(transport, "Nancy", "Strasbourg", 150)
ajouter_arc(transport, "Nancy", "Paris", 380)

print(transport)
