def analyseur(phrase):
    dico = {}
    phrase_splite = phrase.split(' ')
    n = len(phrase_splite)
    for indice in range(n-1):
        mot = phrase_splite[indice].lower().strip('.,')
        mot_suivant = phrase_splite[indice + 1].lower().strip('.,')
        if mot not in dico.keys():
            dico[mot] = {mot_suivant: 1}
        else:
            if mot_suivant in dico[mot].keys():
                dico[mot][mot_suivant] += 1
            else:
                dico[mot][mot_suivant] = 1
    return dico

test = "Il y a des jours et il y a la journée, NSI SNT. Il convient de se préparer pour cette journée pleine d’échanges."

fichier = open("henri.txt", "r", encoding="utf-8")
lines = fichier.readlines()
dico = analyseur(test)

for line in lines:
    analyseur(line.strip('\n'))

print(dico)
