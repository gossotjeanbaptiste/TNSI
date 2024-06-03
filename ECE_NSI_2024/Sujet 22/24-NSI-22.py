def recherche_indices_classement(elt, tab):
    list1 = []
    list2 = []
    list3 = []
    for i in range(len(tab)):
        if tab[i] < elt:
            list1.append(i)
        elif tab[i] == elt:
            list2.append(i)
        else:
            list3.append(i)
    return (list1, list2, list3)

print(recherche_indices_classement(3, [1, 3, 4, 2, 4, 6, 3, 0]))
print(recherche_indices_classement(3, [1, 4, 2, 4, 6, 0]))
print(recherche_indices_classement(3, [1, 1, 1, 1]))
print(recherche_indices_classement(3, []))


resultats = {
    'Dupont': {
        'DS1': [15.5, 4],
        'DM1': [14.5, 1],
        'DS2': [13, 4],
        'PROJET1': [16, 3],
        'DS3': [14, 4]
    },
    'Durand': {
        'DS1': [6 , 4],
        'DS2': [8, 4],
        'PROJET1': [9, 3],
        'IE1': [7, 2],
        'DS3': [12, 4]
    }
}

def moyenne(nom, resultats):
    '''Renvoie la moyenne de l'élève nom, selon le dictionnaire 
    resultats. Si nom n'est pas dans le dictionnaire, 
    la fonction renvoie None.'''
    if nom in resultats: 
        notes = resultats[nom]
        if notes == []: # pas de notes 
            return 0
        total_points = 0 
        total_coefficients = 0 
        for valeurs in notes.values(): 
            note, coefficient = valeurs
            total_points = total_points + note * coefficient 
            total_coefficients = total_coefficients + coefficient
        return round( total_points / total_coefficients, 1 ) 
    else:
        return None

print(moyenne('Dupont', resultats))
print(moyenne('Durand', resultats))
