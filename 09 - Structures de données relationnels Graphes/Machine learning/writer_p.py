from random import randint
# from icecream import ic
import json

with open('resultats.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)
#print(data)

dico = {"ordinateur": 2, "alliance": 1, "oui": 4}


def joker():
    # version temporaire à améliorer
    # return un mot au hasard
    return "joker"


def next_word(dico):
    # return un mot au hasard en respectant les probabilités données
    if dico == {}:
        return joker()
    else:
        total = sum(dico.values())  # On calcule le total des valeurs du dico
        r = randint(1, total)
        # ic(r)
        cpt = 0
        for mot, coef in dico.items():
            cpt += coef
            if r <= cpt:
                # ic(mot)
                return mot


phrase = ''
depart = 'je'
for i in range(5):
    phrase += depart + ' '
    if depart in data.keys():
        depart = next_word(data[depart])
    else:
        depart = joker()
    
print(phrase)

'''
for _ in range(50):
    print(next_word(dico))
    print("-----")
'''
