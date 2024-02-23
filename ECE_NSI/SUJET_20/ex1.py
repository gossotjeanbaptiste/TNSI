'''
Écrire une fonction ajoute_dictionnaires qui prend en paramètres deux
dictionnaires d1 et d2 dont les clés sont des nombres et renvoie le dictionnaire d défini de
la façon suivante :
- Les clés de d sont celles de d1 et celles de d2 réunies.
- Si une clé est présente dans les deux dictionnaires d1 et d2, sa valeur associée
dans le dictionnaire d est la somme de ses valeurs dans les dictionnaires d1 et d2.
- Si une clé n’est présente que dans un des deux dictionnaires, sa valeur associée
dans le dictionnaire d est la même que sa valeur dans le dictionnaire où elle est
présente.
'''


def ajoute_dictionnaires(d1, d2):
    """
    Ajoute les valeurs des clés communes des dictionnaires d1 et d2.
    Si une clé est présente uniquement dans l'un des dictionnaires, elle est ajoutée au résultat.

    Args:
        d1 (dict): Premier dictionnaire.
        d2 (dict): Deuxième dictionnaire.

    Returns:
        dict: Dictionnaire contenant la somme des valeurs des clés communes et les clés uniques des deux dictionnaires.
    """
    d = {}
    for k in d1:
        if k in d2:
            d[k] = d1[k] + d2[k]
        else:
            d[k] = d1[k]
    for k in d2:
        if k not in d1:
            d[k] = d2[k]
    return d


assert ajoute_dictionnaires({1: 5, 2: 7}, {2: 9, 3: 11}) == {
    1: 5, 2: 16, 3: 11}, 'erreur'
print(ajoute_dictionnaires({1: 5, 2: 7}, {2: 9, 3: 11}))
