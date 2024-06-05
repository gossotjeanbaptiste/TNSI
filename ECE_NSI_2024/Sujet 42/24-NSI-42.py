def moyenne(tab):
    """calcule la moyenne des éléments du tableau tab"""
    n = len(tab)
    somme = 0
    for i in range(n):
        somme = somme + tab[i]
    return somme / n


def dichotomie(tab, x):
    """applique une recherche dichotomique pour déterminer
    si x est dans le tableau trié tab.
    La fonction renvoie True si tab contient x et False sinon"""

    debut = 0
    fin = len(tab) - 1 
    while debut <= fin:
        m = (debut + fin) // 2
        if x == tab[m]:
            return True 
        if x > tab[m]:
            debut = m + 1 
        else:
            fin = m - 1 
    return False


