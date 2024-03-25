def cesar(chaine: str, decompte: int) -> str:
    # ! Principe Décalage de caractères
    # ! On décale chaque caractère de la chaîne de caractères de la valeur de décompte
    resultat = ""
    decompte %= 26
    for lettre in chaine:
        if 97 <= ord(lettre) <= 122:
            resultat += chr((ord(lettre) - 97 + decompte) % 26 + 97)
        elif 65 <= ord(lettre) <= 90:
            resultat += chr((ord(lettre) - 65 + decompte) % 26 + 65)
        else:
            resultat += lettre
    return resultat


print(cesar("BONJOUR", 54))  # CPOKVPS


def dechiffre_cesar(chaine: str, decompte: int) -> str:
    # Appliquer un décalage négatif pour décrypter
    return cesar(chaine, -decompte)


print(dechiffre_cesar("CPOKVPS", 54))  # BONJOUR


def affine(chaine: str, a: int, b: int) -> str:
    pass


def vigenere(chaine: str, cle: str) -> str:
    pass
