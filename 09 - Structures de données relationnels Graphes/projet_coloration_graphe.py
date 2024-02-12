import networkx as nx
from matplotlib import pyplot as plt

G = nx.Graph()
G.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8])
G.add_edges_from([(1, 2), (1, 3), (1, 5), (1, 8), (2, 3),
                  (3, 4), (4, 8), (5, 6), (6, 7), (8, 7)])

def coloriage_glouton(graphe):
    couleur = {}
    for s in graphe.nodes():
        for v in graphe.neighbors(s):
            #couleur_voisins = [col for col in couleur[v]]
            couleur_voisins = [couleur[voisin] for voisin in graphe.neighbors(s) if voisin in couleur]
            if couleur_voisins:
                numero = max(couleur_voisins) + 1
                new_color = numero
                for i in range(numero):
                    if i not in couleur_voisins and i < new_color:
                        new_color = i 
            else:
                couleur[s] = 0
    return couleur
        

carte_couleur = [0, 1, 2, 1, 2, 0, 1, 2]
#nx.draw(G, node_color=carte_couleur, with_labels=True, font_weight='bold')
#plt.show()

#fait par IA


def coloriage_glouton_ia(graphe):
    """
    Colorie un graphe en utilisant l'algorithme de coloration gloutonne.

    :param graphe: Un graphe représenté sous forme de dictionnaire, où les clés sont les sommets
                  et les valeurs sont les listes des voisins de chaque sommet.
    :return: Un dictionnaire représentant la coloration du graphe, où les clés sont les sommets
             et les valeurs sont les couleurs attribuées à chaque sommet.
    """
    sommets = list(graphe.keys())
    couleurs = {}  # Dictionnaire pour stocker les couleurs attribuées à chaque sommet

    # Trie les sommets par degré décroissant (nombre de voisins)
    sommets_triés = sorted(sommets, key=lambda sommet: len(
        graphe[sommet]), reverse=True)

    # Parcourt les sommets triés et attribue une couleur à chaque sommet
    for sommet in sommets_triés:
        # Couleurs possibles pour ce sommet
        couleurs_possibles = set(range(1, len(sommets) + 1))

        # Parcourt les voisins du sommet et retire leurs couleurs de l'ensemble des couleurs possibles
        for voisin in graphe[sommet]:
            if voisin in couleurs:
                couleurs_possibles.discard(couleurs[voisin])

        # Attribue la couleur disponible la plus basse au sommet
        couleurs[sommet] = min(couleurs_possibles)

    return couleurs


# Exemple d'utilisation
graphe_exemple = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

resultat_coloriage = coloriage_glouton(graphe_exemple)
print("Coloration gloutonne du graphe:", resultat_coloriage)
