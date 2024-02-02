def recherche(val, tab):
    nb_occurences = 0
    for element in tab:
        if element == val:
            nb_occurences += 1
    return nb_occurences


pieces = [1, 2, 5, 10, 20, 50, 100, 200]

def rendu_monnaie(somme_due, somme_versee):
    rendu = []
    a_rendre = somme_versee - somme_due
    i = len(pieces) - 1
    while a_rendre > 0:
        if pieces[i] <= a_rendre :
            rendu.append(pieces[i])
            a_rendre = a_rendre - pieces[i]
        else :
            i -= 1
    return rendu
