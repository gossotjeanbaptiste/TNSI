def parser(phrase):
    dico = {}
    for mot in phrase.split(' '):
        mot.lower()
        print(mot)
        if mot in dico:
            dico[mot] += 1
        else:
            dico[mot] = 1
    return dico

test = "Il y a des jours et il y a la journée NSI SNT"

print(parser(test))