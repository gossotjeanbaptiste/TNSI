from re import split, sub
import pprint
import json

# Ouverture  du fichier
text = open("maupassant.txt", 'r', encoding='utf-8')
lines = text.readlines()

def sanitize(word):
    return sub('[!?(,;.:«»)\n]', '', word).lower()



def create_dict():
    mon_dico = {}
    for line in lines:
        words = split(" ", line)
        for indice,word in enumerate(words):
            word_clean = sanitize(word)
            if word_clean in mon_dico.keys():
                if indice < len(words)-1 :
                    next_word = sanitize(words[indice +1])
                    if next_word in mon_dico[word_clean].keys():
                        mon_dico[word_clean][next_word] = mon_dico[word_clean][next_word] + 1
                    else:
                        mon_dico[word_clean].update({next_word: 1})
                else:
                    mon_dico[word_clean] = {}
            else:
                #attention au  dernier mot de la phrase
                if indice < len(words) - 1 :
                    mon_dico[word_clean] = {sanitize(words[indice +1]): 1}
                else:
                    mon_dico[word_clean] = {}
    return mon_dico


parsed_text_dict = create_dict()
#pp = pprint.PrettyPrinter(indent=2)
#pp.pprint(parsed_text_dict)
# sauvegarde du dictionnaire
with open('corpus_maupassant.json', 'w+') as json_file: json.dump(parsed_text_dict, json_file)
