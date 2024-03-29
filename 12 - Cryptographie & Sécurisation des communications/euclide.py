def pgcd(n1, n2):  # plus grand diviseur commun algo d'euclide
    # ! Vu en maths expertes
    reste = n1 % n2
    if reste == 0:
        return n2
    else:
        return pgcd(n2, reste)


def euclide_etendu(a, b):
    if b == 0:
        return (1, 0)
    else:
        x, y = euclide_etendu(b, a % b)
        return (y, x - (a // b) * y)


print(euclide_etendu(7, 432))
print(pgcd(7, 432))
