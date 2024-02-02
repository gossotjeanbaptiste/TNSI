def verifie(tableau):
    resultat = None
    valeur = tableau[0]
    for i in range(len(tableau)):
        if valeur <= tableau[i]:
            valeur = tableau[i]
            resultat = True
        else:
            resultat = False
            return resultat
    return resultat
