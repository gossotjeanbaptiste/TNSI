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


print(cesar("BONJOUR", 5))  # GTSOTZW


def dechiffre_cesar(chaine: str, decompte: int) -> str:
    # Appliquer un décalage négatif pour décrypter
    return cesar(chaine, -decompte)


print(dechiffre_cesar("GTSOTZW", 5))  # BONJOUR


def affine(chaine: str, a: int, b: int) -> str:
    # ! Principe Affine
    # ! On applique une transformation affine à chaque caractère de la chaîne de caractères
    resultat = ""
    for lettre in chaine:
        if 97 <= ord(lettre) <= 122:
            resultat += chr((a * (ord(lettre) - 97) + b) % 26 + 97)
        elif 65 <= ord(lettre) <= 90:
            resultat += chr((a * (ord(lettre) - 65) + b) % 26 + 65)
        else:
            resultat += lettre
    return resultat


def vigenere(chaine: str, cle: str) -> str:
    # ! Principe Vigenère
    # ! On applique un chiffrement de Vigenère à chaque caractère de la chaîne de caractères
    resultat = ""
    cle_index = 0
    for lettre in chaine:
        if 97 <= ord(lettre) <= 122:
            decalage = ord(cle[cle_index % len(cle)]) - 97
            resultat += chr((ord(lettre) - 97 + decalage) % 26 + 97)
            cle_index += 1
        elif 65 <= ord(lettre) <= 90:
            decalage = ord(cle[cle_index % len(cle)]) - 65
            resultat += chr((ord(lettre) - 65 + decalage) % 26 + 65)
            cle_index += 1
        else:
            resultat += lettre
    return resultat
