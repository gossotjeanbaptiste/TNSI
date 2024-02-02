from liste import *

# 1) création de la liste
L2 = creer_liste()

L2 = ajouter_en_tete('a', ajouter_en_tete('e', ajouter_en_tete(
    'i', ajouter_en_tete('o', ajouter_en_tete('u', ajouter_en_tete('y', L2))))))

# 2) acceder a 'i'
c = tete(queue(queue(L2)))
