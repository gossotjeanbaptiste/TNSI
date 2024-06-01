def nombre_de_mots(phrase):
    '''Renvoie le nombre de mots dans une phrase.'''
    return len(phrase.split())


def nombre_de_mots_v2(phrase):
    '''Renvoie le nombre de mots dans une phrase.'''
    nb_mots = 0
    for i in range(len(phrase)):
        if phrase[i] == ' ':
            nb_mots += 1
        if phrase[i] == '.': # On suppose que la phrase se termine par un point.
            nb_mots += 1
    return nb_mots


print(f'{nombre_de_mots_v2('Cet exercice est simple.')}')
print(f'{nombre_de_mots_v2('Le point d exclamation est séparé !')}')
print(f'{nombre_de_mots_v2('Combien de mots y a t il dans cette phrase ?')}')
print(f'{nombre_de_mots_v2('Fin.')}')


class Noeud:
    def __init__(self, etiquette):
        '''Méthode constructeur pour la classe Noeud.
        Crée une feuille d'étiquette donnée.'''
        self.etiquette = etiquette
        self.gauche = None
        self.droit = None

    def inserer(self, cle):
        '''Insère la clé dans l'arbre binaire de recherche
        en préservant sa structure.'''
        if cle < self.etiquette:
            if self.gauche != None:
                self.gauche.inserer(cle)
            else:
                self.gauche = Noeud(cle)
        else:
            if self.droit != None:
                self.droit.inserer(cle)
            else:
                self.droit = Noeud(cle)


arbre = Noeud(7)
for cle in (3, 9, 1, 6):
    arbre.inserer(cle)
print(arbre.gauche.etiquette)
print(arbre.droit.etiquette)
print(arbre.gauche.gauche.etiquette)
print(arbre.gauche.droit.etiquette)
