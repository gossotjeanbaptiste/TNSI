import networkx as nx
from matplotlib import pyplot as plt
import csv
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

reader = csv.DictReader(
    open('t1_7.csv', 'r', encoding='utf-8'), delimiter=',')
data = [row for row in reader]


couple_spe = {}
for dico in data:
    if dico['Spe1'] < dico['Spe2']:
        temp = (dico['Spe1'], dico['Spe2'])
    else:
        temp = (dico['Spe2'], dico['Spe1'])

    if temp not in couple_spe.keys():
        couple_spe[temp] = 1
    else:
        couple_spe[temp] += 1

print(couple_spe)


def coloriage_glouton(graphe):
    couleur = {}
    for s in graphe.nodes():
        # couleur_des_voisins = [col for col in couleur.get]
        couleur_des_voisins = [couleur[voisin]
                               for voisin in graphe.neighbors(s) if voisin in couleur]
        if couleur_des_voisins:
            numero = max(couleur_des_voisins) + 1
            new_color = numero
            for i in range(numero):
                if i not in couleur_des_voisins and i < new_color:
                    new_color = i
            couleur[s] = new_color
        else:
            couleur[s] = 0
    return couleur


G = nx.Graph()


carte_couleur = [i for i in coloriage_glouton(G).values()]

"""('SES', 'SVT'): 8  ---> ('SES', 'SVT', 8) """
link = [(cle[0], cle[1], valeur) for cle, valeur in couple_spe.items()]

G.add_nodes_from(['HGGSP', 'HLP', 'LLCE', 'Maths',
                 'NSI', 'PH-CH', 'SES', 'SVT'])

G.add_weighted_edges_from(link)
resultat = coloriage_glouton(G)
carte_couleur = [resultat[noeud] for noeud in G.nodes()]
# positions for all nodes - seed for reproducibility
pos = nx.spring_layout(G, seed=5)

nx.draw(G, pos, node_color=carte_couleur, with_labels=True, font_weight='bold')
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels)
plt.show()
