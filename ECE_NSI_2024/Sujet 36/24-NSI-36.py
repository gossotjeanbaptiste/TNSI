# * Ex 1

def occurences(lettre: str, mot: str) -> int:
    conte_lettre = 0
    if len(lettre) == 0 or len(mot) == 0:
        return conte_lettre
    if len(lettre) != 1:
        assert ValueError("La lettre doit être un caractère")
    for l in range(len(mot)):
        if mot[l] == lettre:
            conte_lettre += 1
    return conte_lettre


# * Ex 2
valeurs = [100, 50, 20, 10, 5, 2, 1]


def rendu_glouton(a_rendre: int, rang: int) -> list[int]:
    if a_rendre == 0:
        return []
    v = valeurs[rang]
    if v <= a_rendre:
        return 1 + rendu_glouton(a_rendre - v, rang)
    else:
        return rendu_glouton(a_rendre, rang + 1)
