from random import randint, choices
from primePy import primes
# Description: Implémentation de l'algorithme RSA


def pgcd(a, b):
    if a < b:
        return pgcd(b, a)
    elif b == 0:
        # cas de base
        return a
    else:
        # pas de recursion
        return pgcd(b, a % b)


def lame_lucas(a, n):
    """renvoie l'inverse de a modulo n """
    mat = [[n, 1, 0],
           [a, 0, 1]]
    i = 2
    while mat[i-1][0] > 0:
        # qotient
        q = mat[i-2][0] // mat[i-1][0]
        # reste
        r = mat[i-2][0] % mat[i-1][0]
        # relation de récurrence au sens mathématiques du terme
        x = mat[i-2][1] - q * mat[i-1][1]
        y = mat[i-2][2] - q * mat[i-1][2]
        mat.append([r, mat[i-2][1] - q * mat[i-1][1],
                   mat[i-2][2] - q * mat[i-1][2]])
        i += 1
    return mat[-2][2]


def generate_e(n):
    """
    Génère un entier aléatoire e entre 2 et n-1 (inclus) tel que pgcd(e, n) = 1.

    Paramètres:
    n (int): La limite supérieure pour générer e.
    """
    e = randint(2, n-1)
    while pgcd(e, n) != 1:
        e = randint(2, n-1)
    return e


def get_cle_publique_prive(len_cle=3):
    liste_premiers = primes.between(10**(len_cle-1), 10**(len_cle) - 1)
    p, q = choices(liste_premiers, k=2)
    n = p * q
    phi_n = (p-1)*(q-1)
    e = generate_e(phi_n)
    d = lame_lucas(e, phi_n)
    d = d if d > 0 else d + phi_n
    return {"cle_publique": (n, e), "cle_prive": d}
