def recherche_dicho(tab: list, indice: int) -> int:
    if len(tab) == 1:
        return tab[0]
    elif tab == []:
        return None
    else:
        milieu = len(tab)//2
        a = recherche_dicho(tab[:milieu], indice)
        b = recherche_dicho(tab[milieu:], indice)
        if a < b:
            return b
        else:
            return a
        # return max(max_fusion(tab[:milieu]), max_fusion(tab[milieu:]))


def recherche(tab: list, indice: int) -> int:
    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        milieu = (debut + fin) // 2
        if tab[milieu] == indice:
            return milieu
        elif tab[milieu] > indice:
            fin = milieu - 1
        else:
            debut = milieu + 1
    return None


assert recherche([2, 3, 4, 5, 6], 5) == 3, "Pb Test 1"
print("Test 1 OK")
print(recherche([2, 3, 4, 5, 6], 5))
print('-----------------')

assert recherche([2, 3, 4, 6, 7], 5) == None, "Pb Test 2"
print("Test 2 OK")
print(recherche([2, 3, 4, 6, 7], 5))
print('-----------------')

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def position_alphabet(lettre):
    '''Renvoie la position de la lettre dans l'alphabet'''
    return ord(lettre) - ord('A')


def cesar(message, decalage):
    '''Renvoie le message codé par la méthode de César
    pour le decalage donné'''
    resultat = ''
    for c in message:
        if 'A' <= c and c <= 'Z':
            indice = (position_alphabet(c) + decalage) % 26
            resultat = resultat + alphabet[indice]
        else:
            resultat = resultat + c
    return resultat


assert cesar('BONJOUR A TOUS. VIVE LA MATIERE NSI !', 4) == 'FSRNSYV E XSYW. ZMZI PE QEXMIVI RWM !', "Pb Test 3"
print("Test 3 OK")
print(cesar('BONJOUR A TOUS. VIVE LA MATIERE NSI !', 4))
print('-----------------')

assert cesar('GTSOTZW F YTZX. ANAJ QF RFYNJWJ SXN !', -5) == 'BONJOUR A TOUS. VIVE LA MATIERE NSI !', "Pb Test 4"
print("Test 4 OK")
print(cesar('GTSOTZW F YTZX. ANAJ QF RFYNJWJ SXN !', -5))
