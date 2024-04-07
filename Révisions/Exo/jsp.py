"""
for indice in range(97, 123):
    if indice % 7 == 5:
        print(chr(indice))
    else:
        print(chr(indice), ' ', end="")
print()
"""


def factorielle(n):
    fact = 1
    for nb in range(1, n+1):
        fact *= nb # ! fact = fact * nb 
    return fact


"""taux = 0.04
capital = 1253
for mois in range(1, 13):
    coef = 1 + taux
    capital = capital + capital * taux
"""


def RechercheMinMax(tableau):
    if tableau == []:
        return {'min': None, 'max': None}
    else:
        min = tableau[0]
        max = tableau[0]
        for indice in range(1, len(tableau)):
            if tableau[indice] < min:
                min = tableau[indice]
            if tableau[indice] > max:
                max = tableau[indice]
        return {'min': min, 'max': max}
