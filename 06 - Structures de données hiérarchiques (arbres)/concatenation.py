def binaire(n):
    if n <= 1:
        return f"{n}"
    else:
        # on concatène toujours par la gauche
        return f"{n % 2 + binaire(n//2)}"
