from random import randint, choices
# from icecream import ic
import json
from gtts import gTTS
import os
from parser_p import *

with open('resultats.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)
# print(data)

dico = {"ordinateur": 2, "alliance": 1, "oui": 4}


def joker():
    # version temporaire à améliorer
    # return un mot au hasard
    return choices(list(data.keys()))[0]


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


text = 'Mathéo va travailler !'
language = 'fr'
obj = gTTS(text=text, lang=language, slow=False)
obj.save("output.mp3")
os.system("start output.mp3")
'''

def  generer_phrase():
    phrase = ''
    depart = 'je'
    for i in range(10):
        phrase += depart + ' '
        if depart in data.keys():
            depart = next_word(data[depart])
        else:
            depart = joker()
    return phrase

#apprentisage par renforcement
for _ in range(10):
    phrase = generer_phrase()
    print(phrase)
    note = int(input("Notez cette phrase de 0 à 5 : "))
    if note > 3:
        #on recalcule les probabilités on parse la phrase et on met à jour le dictionnaire
        analyseur(phrase)
    else:
        #on corrige la phrase	
        phrase = input("Entrez une phrase correcte : ")
        #on parse la phrase et on met à jour le dictionnaire
        # on parse la phrase et on met à jour le dictionnaire
        analyseur(phrase)