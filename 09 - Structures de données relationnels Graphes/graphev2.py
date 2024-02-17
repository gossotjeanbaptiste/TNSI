from collections import deque
# deque est une structure de données qui permet d'ajouter et de supprimer des éléments en temps constant

michel = {"1": ["2", "5", "8"],
          "2": ["3"],
          "3": ["1", "4"],
          "4": ["8"],
          "5": ["6"],
          "6": [],
          "7": ["6"],
          "8": ["7"]
          }  # graphe orienté ex1

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


def parcours_largeur(graph, depart):
    """
    Effectue un parcours en largeur sur un graphe à partir d'un nœud de départ.
    Args:
        graph (list): Le graphe représenté sous forme de liste d'adjacence.
        depart (int): Le nœud de départ du parcours.
    Returns:
        list: Une liste contenant les nœuds visités dans l'ordre du parcours en largeur.
    """
    resultat = []  # Liste pour stocker les nœuds visités
    deja_visites = [False] * len(graph)  # Liste pour marquer les nœuds déjà visités
    a_traiter = []  # File pour stocker les nœuds à traiter
    a_traiter.append(depart)  # Ajoute le nœud de départ à la file
    deja_visites[depart] = True  # Marque le nœud de départ comme visité
    while a_traiter:
        # Retire le premier nœud de la file
        noeud_courant = a_traiter.pop(0)
        resultat.append(noeud_courant)  # Ajoute le nœud courant à la liste des nœuds visités
        # Parcourt les voisins du nœud courant
        for voisin in graph[noeud_courant]:
            if not deja_visites[voisin]:
                a_traiter.append(voisin)  # Ajoute le voisin à la file
                deja_visites[voisin] = True  # Marque le voisin comme visité

    return resultat

def parcours_largeur2(G, v):
    visites = deque(v)
    a_visiter = deque(voisins(G, v))
    while a_visiter:
        # pour une file utiliser popleft() pour retirer le premier élément
        sommet = a_visiter.popleft()
        if sommet not in visites:
            visites.append(sommet)
            for voisin in voisins(G, sommet):
                if voisin not in visites:
                    a_visiter.append(voisin)
    return visites

# Exemple d'utilisation
# Supposons que le graphe soit représenté par une liste d'adjacence
# graph = {0: [1, 2], 1: [3, 4], 2: [5], 3: [], 4: [6], 5: [], 6: []}
# On appelle la fonction parcours_largeur avec le graphe et le nœud de départ, par exemple, 0
# resultat = parcours_largeur(graph, 0)
# print(resultat)
# Sortie: [0, 1, 2, 3, 4, 5, 6]


# graph = {0: [1, 2], 1: [3, 4], 2: [5], 3: [], 4: [6], 5: [], 6: []}
# print(parcours_largeur(graph, 0))


def parcours_profondeur(G, v):
    visites = deque(v)
    a_visiter = deque(voisins(G, v))
    while a_visiter:
        sommet = a_visiter.pop()
        if sommet not in visites:
            visites.append(sommet)
            for voisin in voisins(G, sommet):
                if voisin not in visites:
                    a_visiter.append(voisin)
    return visites


print(parcours_profondeur(michel, "1"))  # psartek michel <3
print(parcours_largeur2(michel, "1"))
