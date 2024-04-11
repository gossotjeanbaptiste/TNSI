def inverse_modulaire(a:int, m:int)->int:
    """
    Calcule l'inverse modulaire de a modulo m.
    Retourne l'inverse modulaire si il existe, sinon retourne None.
    """
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None