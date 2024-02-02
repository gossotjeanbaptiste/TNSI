from pile import *

def verif_syntaxe(chaine):
    test = creer_pile()
    # boucle for sur les caractères de la chaine
    for indice, caractere in enumerate(chaine):
        if caractere == '(':
            empiler(test, caractere)
        elif caractere == ')':
            if est_vide(test):
                print(f'erreur à la position {indice}')
                return False
            else:
                depiler(test)
    return est_vide(test)