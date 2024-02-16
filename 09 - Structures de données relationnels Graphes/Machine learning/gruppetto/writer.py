#from re import split, sub
import json
from random import randint

# Ouverture  du fichier
with open('corpus_maupassant.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

#testez que charge bien
def next_word(dico):
    total = 0
    for nombre in dico.values():
        total += nombre
    return total
