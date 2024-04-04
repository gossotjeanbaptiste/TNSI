def cesar(chaine:str, decalage:int)->str:
    """Chiffre de Cesar"""
    decalage = decalage % 26
    response = ""
    for lettre in chaine:
        if 97 <= ord(lettre) <= 122:
            response += chr((ord(lettre) - 97 + decalage) % 26 + 97)
        elif 65 <= ord(lettre) <= 90:
            response += chr((ord(lettre) - 65 + decalage) % 26 + 65)
        else:
            response += lettre
    return response


def de_cesar(chaine:str, decalage:int)->str:
    """Dechifrement de Cesar"""
    return cesar(chaine, -decalage)


def affine(chaine:str, a:int, b:int)->str:
    """Chiffrement affine (ax + b)"""
    resultat = ""
    for lettre in chaine:
        if 97 <= ord(lettre) <= 122:
            resultat += chr((a * (ord(lettre) - 97)+ b)%26 + 97)
        elif 65 <= ord(lettre) <= 90:
            resultat += chr((a * (ord(lettre) - 65) + b) % 26 + 65)
        else:
            resultat += lettre
    return resultat


def inverse_modulaire_bf(nombre:int)->int:
    """Fonction qui trouve l'inverse modulaire de nombre
    modulo 26
    """
    for i in range(26):
        if nombre * i % 26 == 1:
            return i


def de_affine(chaine:str, a:int, b:int)->str:
    """Dechiffrement du codage affine"""   
    resultat = ""
    for lettre in chaine:
        if 97 <= ord(lettre) <= 122:
            resultat += chr(inverse_modulaire_bf(a) * ((ord(lettre) - 97) - b) % 26 + 65)
        elif 65 <= ord(lettre) <= 90:
            resultat += chr(inverse_modulaire_bf(a) * ((ord(lettre) - 65) - b) % 26 + 65)
        else:
            resultat += lettre
    return resultat


def vigenere(chaine: str, cle: str)->str:
    """Chiffre un texte selon le chiffrement de Vigenère"""
    response = ""
    indice_cle = 0
    for lettre in chaine:
        if 97 <= ord(lettre) <= 122:
            indice_lettre = ord(lettre) - 97
            cle_lettre = ord(cle[indice_cle % len(cle)]) - 97
            indice_chiffre = (indice_lettre + cle_lettre) % 26
            caractere_chiffre = chr(indice_chiffre + 97)
            indice_cle += 1
        elif 65 <= ord(lettre) <= 90:
            indice_lettre = ord(lettre) - 65
            cle_lettre = ord(cle[indice_cle % len(cle)]) - 65
            indice_chiffre = (indice_lettre + cle_lettre) % 26
            caractere_chiffre = chr(indice_chiffre + 65)
            indice_cle += 1
        else:
            caractere_chiffre = lettre
        response += caractere_chiffre
    return response


def de_vigenere(chaine: str, cle: str) -> str:
    """Déchiffre un texte selon le chiffrement de Vigenère"""
    response = ""
    indice_cle = 0
    for lettre in chaine:
        if 97 <= ord(lettre) <= 122:
            indice_lettre = ord(lettre) - 97
            cle_lettre = ord(cle[indice_cle % len(cle)]) - 97
            indice_dechiffre = (indice_lettre - cle_lettre) % 26
            caractere_dechiffre = chr(indice_dechiffre + 97)
            indice_cle += 1
        elif 65 <= ord(lettre) <= 90:
            indice_lettre = ord(lettre) - 65
            cle_lettre = ord(cle[indice_cle % len(cle)]) - 65
            indice_dechiffre = (indice_lettre - cle_lettre) % 26
            caractere_dechiffre = chr(indice_dechiffre + 65)
            indice_cle += 1
        else:
            caractere_dechiffre = lettre
        response += caractere_dechiffre
    return response


def xor(chaine: str, cle: str)->str:
    """Chiffre un texte selon le chiffrement xor"""
    response = ""
    indice_cle = 0
    for lettre in chaine:
        lettre_chiffree = chr(ord(lettre) ^ ord(cle[indice_cle % len(cle)]))
        response += lettre_chiffree
        indice_cle += 1
    return response