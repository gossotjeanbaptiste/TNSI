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


#print(cesar("BONJOUR", 5))  # GTSOTZW


def dechiffre_cesar(chaine: str, decompte: int) -> str:
    # Appliquer un décalage négatif pour décrypter
    return cesar(chaine, -decompte)


#print(dechiffre_cesar("GTSOTZW", 5))  # BONJOUR


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


def inv_modulaire_bf(a: int) -> int:
    # ! Principe Inverse Modulaire
    # ! On cherche l'inverse modulaire de a modulo 26
    for i in range(1, 26):
        if (a * i) % 26 == 1:
            return i
    return -1


def dechiffre_affine(chaine: str, a: int, b: int) -> str:
    resultat = ""
    for lettre in chaine:
        if 97 <= ord(lettre) <= 122:
            resultat += chr(inv_modulaire_bf(a) *
                            ((ord(lettre) - 97) - b) % 26 + 97)
        elif 65 <= ord(lettre) <= 90:
            resultat += chr(inv_modulaire_bf(a) *
                            ((ord(lettre) - 65) - b) % 26 + 65)
        else:
            resultat += lettre
    return resultat
    # return affine(chaine, 1 // a, -b // a)


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


#print(vigenere("TERMINALE", "NSI"))


def de_viginere(chaine: str, cle: str) -> str:
    # ! Principe Vigenère
    # ! On applique un déchiffrement de Vigenère à chaque caractère de la chaîne de caractères
    resultat = ""
    cle_index = 0
    for lettre in chaine:
        if 97 <= ord(lettre) <= 122:
            decalage = ord(cle[cle_index % len(cle)]) - 97
            resultat += chr((ord(lettre) - 97 - decalage) % 26 + 97)
            cle_index += 1
        elif 65 <= ord(lettre) <= 90:
            decalage = ord(cle[cle_index % len(cle)]) - 65
            resultat += chr((ord(lettre) - 65 - decalage) % 26 + 65)
            cle_index += 1
        else:
            resultat += lettre
    return resultat


def xor_encrypt_decrypt(message:str, key:str)->str:
    encrypted = ""
    for i in range(len(message)):
        encrypted += chr(ord(message[i]) ^ ord(key[i % len(key)]))
    return encrypted


# Exemple d'utilisation
message = "Bonjour"
key = "secret"

# Chiffrement
encrypted_message = xor_encrypt_decrypt(message, key)
print("Message chiffré:", encrypted_message)

# Déchiffrement
decrypted_message = xor_encrypt_decrypt(encrypted_message, key)
print("Message déchiffré:", decrypted_message)

