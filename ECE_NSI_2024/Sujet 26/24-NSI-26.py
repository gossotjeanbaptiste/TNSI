# -*- coding: utf-8 -*-

from random import randint


def ajoute_dictionnaires(dico1, dico2):
    '''Ajoute les valeurs des clés communes de deux dictionnaires.'''
    dico = {}
    for cle in dico1:
        if cle in dico2:
            dico[cle] = dico1[cle] + dico2[cle]
        else:
            dico[cle] = dico1[cle]
    for cle in dico2:
        if cle not in dico1:
            dico[cle] = dico2[cle]
    return dico


def version2(d1, d2):
    return {key: d1.get(key, 0) + d2.get(key, 0) for key in set(d1).union(d2)}


print(ajoute_dictionnaires({1: 5, 2: 7}, {2: 9, 3: 11}))
print(ajoute_dictionnaires({}, {2: 9, 3: 11}))
print(ajoute_dictionnaires({1: 5, 2: 7}, {}))

print(version2({1: 5, 2: 7}, {2: 9, 3: 11}))
print(version2({}, {2: 9, 3: 11}))
print(version2({1: 5, 2: 7}, {}))


def nombre_coups():
    '''Simule un jeu de plateau avec 12 cases et renvoie le nombre
    minimal de coups pour visiter toutes les cases.'''
    nombre_cases = 12
    # indique si une case a été vue
    cases_vues = [False] * nombre_cases
    nombre_cases_vues = 1
    cases_vues[0] = True
    case_en_cours = 0
    n = 1
    while nombre_cases_vues < nombre_cases:
        x = randint(1, 6)
        case_en_cours = (case_en_cours + x) % nombre_cases
        if not cases_vues[case_en_cours]:
            cases_vues[case_en_cours] = True
            nombre_cases_vues = nombre_cases_vues + 1
        n = n + 1
    return n
