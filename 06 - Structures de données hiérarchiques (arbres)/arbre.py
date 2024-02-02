class Noeud:
    def __init__(self, racine):
        self.gauche = None
        self.droit = None
        self.racine = racine

    # setteurs optionnel en py obligatoire en Java et C++

    def set_arbre_g(self, abg):
        self.gauche = abg

    def set_arbre_d(self, abd):
        self.droit = abd

    def set_racine(self, racine):
        self.racine = racine

    def prefixe(self, liste_valeurs=None):
        if liste_valeurs == None:
            liste_valeurs = []
        if self.racine:
            liste_valeurs.append(self.racine)
        if self.gauche:
            self.gauche.prefixe(liste_valeurs)
        if self.droit:
            self.droit.prefixe(liste_valeurs)
        return liste_valeurs

    def postfixe(self, liste_valeurs):
        if liste_valeurs == None:
            liste_valeurs = []
        if self.gauche:
            self.gauche.postfixe(liste_valeurs)
        if self.droit:
            self.droit.postfixe(liste_valeurs)
        if self.racine:
            liste_valeurs.append(self.racine)
        return liste_valeurs

    def infixe(self, liste_valeurs):
        if liste_valeurs == None:
            liste_valeurs = []
        if self.gauche:
            self.gauche.infixe(liste_valeurs)
        if self.racine:
            liste_valeurs.append(self.racine)
        if self.droit:
            self.droit.infixe(liste_valeurs)
        return liste_valeurs

    def est_dans(self, element):
        """renvoie True si element dans l'arbre, False sinon"""
        if self.racine == element:
            return True
        elif self.gauche and self.gauche.est_dans(element):
            return True
        elif self.droit and self.droit.est_dans(element):
            return True
        else:
            return False

    def hauteur(self):
        if self is None:
            return 0
        else:
            hauteur_gauche = self.gauche.hauteur() if self.gauche else 0
            hauteur_droit = self.droit.hauteur() if self.droit else 0
            return 1 + max(hauteur_gauche, hauteur_droit)

    # Ex1
    def taille(self):
        if self is None:
            return 0
        else:
            taille_gauche = self.gauche.taille() if self.gauche else 0
            taille_droit = self.droit.taille() if self.droit else 0
            return 1 + taille_gauche + taille_droit

    def __repr__(self):
        return f'{self.racine}({str(self.gauche)}, {str(self.droit)})'


"""
Xd = Noeud('Cpt Marvel')
Xg = Noeud('Dr Strange')
H = Noeud('Hulk')
H.set_arbre_g(Xg)
H.set_arbre_d(Xd)

V = Noeud('Venom')
Spi = Noeud('Spiderman')
Spi.set_arbre_d(V)
Spi.set_arbre_g(H)

T = Noeud('Thor')
L = Noeud('Loki')
Bl = Noeud('Black Widow')
Bl.set_arbre_d(L)
Bl.set_arbre_g(T)

I = Noeud('Iron Man')
I.set_arbre_d(Bl)
I.set_arbre_g(Spi)

print(I)"""


class ArbreBinaireDeRecherche:
    def __init__(self, racine):
        self.racine = racine
        self.gauche = None
        self.droit = None

    def inserer(self, element):
        if self:
            if element < self.racine:
                if self.gauche is None:
                    self.gauche = ArbreBinaireDeRecherche(element)
                else:
                    self.gauche.inserer(element)
            else:
                if self.droit is None:
                    self.droit = ArbreBinaireDeRecherche(element)
                else:
                    self.droit.inserer(element)
        else:
            self.racine = element

    def postfixe(self, liste_valeurs):
        if liste_valeurs == None:
            liste_valeurs = []
        if self.gauche:
            self.gauche.postfixe(liste_valeurs)
        if self.droit:
            self.droit.postfixe(liste_valeurs)
        if self.racine:
            liste_valeurs.append(self.racine)
        return liste_valeurs
    
    def rechercher(self, element):
        if self.racine[0] == element:
            return self.racine[1]
        elif element < self.racine[0]:
            if self.gauche is None:
                return 'Pas trouvé'
            else:
                return self.gauche.rechercher(element)
        else:
            if self.droit is None:
                return 'Pas trouvé'
            else:
                return self.droit.rechercher(element)

    def __repr__(self):
        return f'{str(self.gauche)} {self.racine} {str(self.droit)} '


test = ArbreBinaireDeRecherche(5)
test.inserer(3)
test.inserer(2)
test.inserer(4)
test.inserer(7)
test.inserer(6)
test.inserer(8)
print(test)


liste = [('kebab', "sandwich salade tomates ognion"),
        ('christmas', 'période de l\'année'),
        ('touche', 'zqsd et espace'),
        ('chien', 'animal'),
        ('voiture', 'vehicule à moteur'),
        ('jambon', 'boeuf pas halal'),
        ('poulet', 'volaille'),
        ('bruxomanie', 'malade de la mâchoire'),
        ('finition', 'inverse de thomas'),
        ('singe', 'animal qui ressemble à l\'homme'),
        ('chat', 'animal domestique qui se prend pour un dieu'),
        ('site', 'endroit sur internet'),
        ('déni', 'prénom de mon voisin'),
        ('programmation', 'art de coder'),
        ('tanatopracteur', 'influenceur makeup de la mort')]

liste.sort()

dico = ArbreBinaireDeRecherche(('kebab', 'sandwich salade tomates oignons'))
dico.inserer(('christmas', 'jingle bells jingle bells jingle all the way'))
dico.inserer(('site', 'ensemble de pages web'))
dico.inserer(('chat', 'animal domestique qui se prend pour un dieu'))
dico.inserer(('finition', 'inverse thomas'))
dico.inserer(('programmation', 'art de coder'))
dico.inserer(('touche', 'zqsd et espace'))
dico.inserer(('bruxomanie', 'maladie de la mâchoire'))
dico.inserer(('chien', 'animal domestique plus intellignet que mon voisin'))
dico.inserer(('deni', 'prénom de mon voisin'))
dico.inserer(('jambon', 'boeuf pas halal'))
dico.inserer(('poulet', 'volaille'))
dico.inserer(('singe', 'animal qui ressemble à l\'homme'))
dico.inserer(('tanatopracteur', 'influenceur makeup pour mort'))
dico.inserer(('voiture', 'véhicule à moteur polluant diesel'))


#la complexité en tps de la recherche est O(log(n)) car on divise par 2 à chaque fois