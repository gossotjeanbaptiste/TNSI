from random import randint
from icecream import ic

dico = {"ordinateur": 2, "alliance": 1, "oui": 4}


def next_word(dico):
    # return un mot au hasard en respectant les probabilités données
    total = sum(dico.values())  # On calcule le total des valeurs du dico
    r = randint(1, total)
    ic(r)
    cpt = 0
    for mot, coef in dico.items():
        cpt += coef
        if r <= cpt:
            ic(mot)
            return mot


for _ in range(50):
    print(next_word(dico))
    print("-----")
