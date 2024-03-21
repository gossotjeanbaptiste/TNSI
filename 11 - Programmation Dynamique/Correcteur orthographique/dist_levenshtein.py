def distance_de_levenshtein_ia(chaine1: str, chaine2: str) -> int:
    """Retourne la distance de Levenshtein entre deux chaînes de caractères."""
    if len(chaine1) < len(chaine2):
        return distance_de_levenshtein_ia(chaine2, chaine1)

    if len(chaine2) == 0:
        return len(chaine1)

    ligne_precedente = range(len(chaine2) + 1)
    for i, car1 in enumerate(chaine1):
        ligne_suivante = [i + 1]
        for j, car2 in enumerate(chaine2):
            insertion = ligne_precedente[j + 1] + 1
            suppression = ligne_suivante[j] + 1
            substitution = ligne_precedente[j] + (car1 != car2)
            ligne_suivante.append(min(insertion, suppression, substitution))
        ligne_precedente = ligne_suivante

    return ligne_precedente[-1]


def levenshtein(chaine1: str, chaine2: str) -> int:
    n1 = len(chaine1)
    n2 = len(chaine2)
    N = max(n1, n2)
    # initialisation
    d = [[j for j in range(n2+1)] for i in range(n1+1)]
    for i in range(n1+1):
        d[i][0] = i
    for i in range(1, n1+1):  # Modification ici
        for j in range(1, n2+1):  # Modification ici
            c = 0 if chaine1[i-1] == chaine2[j-1] else 1
            d[i][j] = min(d[i-1][j] + 1, d[i][j-1] + 1, d[i-1][j-1] + c)
    return d[n1][n2]


def distance_de_levenshtein_generated(chaine1: str, chaine2: str) -> int:
    """Retourne la distance de Levenshtein entre deux chaînes de caractères."""
    longueurChaine1 = len(chaine1)
    longueurChaine2 = len(chaine2)
    # D est un tableau de longueurChaine1+1 rangées et longueurChaine2+1 colonnes
    # D est indexé à partir de 0, les chaînes à partir de 1
    D = [[0 for j in range(longueurChaine2+1)]
         for i in range(longueurChaine1+1)]
    # i et j itèrent sur chaine1 et chaine2
    for i in range(longueurChaine1+1):
        D[i][0] = i
    for j in range(longueurChaine2+1):
        D[0][j] = j
    for i in range(1, longueurChaine1+1):
        for j in range(1, longueurChaine2+1):
            if chaine1[i-1] == chaine2[j-1]:
                coûtSubstitution = 0
            else:
                coûtSubstitution = 1
            D[i][j] = min(D[i-1][j] + 1, D[i][j-1] + 1,
                          D[i-1][j-1] + coûtSubstitution)
    return D[longueurChaine1][longueurChaine2]


print(distance_de_levenshtein_ia("SAMEDI", "VENDREDI"))
print(levenshtein("SAMEDI", "VENDREDI"))
print(distance_de_levenshtein_generated("SAMEDI", "VENDREDI"))
