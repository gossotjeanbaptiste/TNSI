class Noeud:
    def __init__(self, etiquette, gauche, droite):
        self.v = etiquette
        self.gauche = gauche
        self.droite = droite
        
def taille(arbre):
    '''Renvoie le nombre de noeuds de l'arbre binaire arbre.'''
    if arbre is None:
        return 0
    else:
        return 1 + taille(arbre.gauche) + taille(arbre.droite)
    
def hauteur(arbre):
    '''Renvoie la hauteur de l'arbre binaire arbre.'''
    if arbre is None:
        return -1
    else:
        return 1 + max(hauteur(arbre.gauche), hauteur(arbre.droite))
    

a = Noeud(1, Noeud(4, None, None), Noeud(0, None, Noeud(7, None, None)))

print(hauteur(a))
print(taille(a))
print(hauteur(None))
print(taille(None))
print(hauteur(Noeud(1, None, None)))
print(taille(Noeud(1, None, None)))



def ajoute(indice, element, tab):
    '''Renvoie un nouveau tableau obtenu en insérant
    element à l'indice indice dans le tableau tab.'''
    nbre_elts = len(tab)
    tab_ins = [0] * (nbre_elts + 1)
    for i in range(indice):
        tab_ins[i] = tab[i] 
    tab_ins[indice] = element 
    for i in range(indice + 1, nbre_elts + 1):
        tab_ins[i] = tab[i - 1]
    return tab_ins


print(ajoute(1, 4, [7, 8, 9]))
print(ajoute(3, 4, [7, 8, 9]))
print(ajoute(0, 4, [7, 8, 9]))

