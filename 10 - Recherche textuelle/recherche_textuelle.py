def recherche_textuelle_naif(chaine, motif):
    """Retourne la position du motif dans la chaîne ou -1 si le motif n'est pas trouvé"""
    assert (len(motif) <= len(chaine)), 'chaine trop courte'
    n = len(chaine)
    m = len(motif)
    i = 0
    resultat = []
    while i < n - m:
        j = 0
        while j < m and motif[j] == chaine[i+j]:
            j += 1
        if j == m:
            resultat.append(i)
        i += 1
    return resultat


def affiche_gras(chaine, motif):
    # écrire une fonction affichegras(motif, chaine) qui affiche en gras le motif à chaque fois qu’il est présent dans la chaîne
    resultat = recherche_textuelle_naif(chaine, motif)
    n = len(chaine)
    m = len(motif)
    i = 0
    while i < n:
        if i in resultat:
            print('\033[1m'+chaine[i:i+m]+'\033[0m', end='')
            i += m
        else:
            print(chaine[i], end='')
            i += 1


print(recherche_textuelle_naif(
    "GTAATCAAATCTTGCCAATCAATC", 'AATC'))  # [2, 7, 16]
affiche_gras("GTAATCAAATCTTGCCAATCAATC", 'AATC')


def correspondance(motif, chaine, adroite, p, i):
    # j varie de p-1 à 0 inclus en décroissant
    for j in range(p-1, -1, -1):
        x = motif[i+j]
        if x != motif[j]:
            if x in adroite.keys():
                decalage = max(1, j - adroite[x])
            else:
                decalage = 1
            return (False, decalage)
    return (True, 0)
