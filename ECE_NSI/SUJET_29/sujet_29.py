class Arbre:
    def __init__(self, etiquette):
        self.v = etiquette
        self.fg = None
        self.fd = None
        
a = Arbre(0)
a.fg = Arbre(1)
a.fg.fg = Arbre(3)
a.fd = Arbre(2)
a.fd.fg = Arbre(4)
a.fd.fd = Arbre(5)
a.fd.fg.fd = Arbre(6)

def taille(arbre):
    if arbre is None:
        return 0
    return 1 + taille(arbre.fg) + taille(arbre.fd)

def hauteur(arbre):
    if arbre is None:
        return 0
    return 1 + max(hauteur(arbre.fg), hauteur(arbre.fd))

print(taille(a))
print(hauteur(a))


def ajoute(indice, element, liste):
    nbre_elts = len(liste)
    L = [0 for i in range(nbre_elts + 1)]
    if indice < nbre_elts:
        for i in range(indice):
            L[i] = liste[i]
        L[indice] = element
        for i in range(indice + 1, nbre_elts + 1):
            L[i] = liste[i-1]
    else:
        for i in range(nbre_elts):
            L[i] = liste[i]
        L[nbre_elts] = element
    return L



assert ajoute(1, 4, [7, 8, 9]) == [7, 4, 8, 9], 'Y a un bug t1'
print('t1 ok', ajoute(1, 4, [7, 8, 9]))
assert ajoute(3, 4, [7, 8, 9]) == [7, 8, 9, 4], 'Y a un bug t2'
print('t2 ok', ajoute(3, 4, [7, 8, 9]))
assert ajoute(4, 4, [7, 8, 9]) == [7, 8, 9, 4], 'Y a un bug t3'
print('t3 ok', ajoute(4, 4, [7, 8, 9]))
