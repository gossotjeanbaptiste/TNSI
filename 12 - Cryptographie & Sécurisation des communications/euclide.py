def pgcd(n1, n2):  # plus grand diviseur commun algo d'euclide
    # ! Vu en maths expertes
    reste = n1 % n2
    if reste == 0:
        return n2
    else:
        return pgcd(n2, reste)

def euclide_etendu(a, b):
    r, u, v, r1, u1, v1 = a, 1, 0, b, 0, 1
    while r1 != 0:
        q = r // r1
        r, u, v, r1, u1, v1 = r1, u1, v1, r - q * r1, u - q * u1, v - q * v1
    return r, u, v