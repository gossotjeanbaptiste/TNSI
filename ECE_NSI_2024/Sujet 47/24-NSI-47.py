def max_dico(dico):
    """ Renvoie la clé et la valeur associée à la plus grande valeur du dictionnaire. """
    max_cle = None
    max_valeur = None
    for cle, valeur in dico.items():
        if max_valeur == None or valeur > max_valeur:
            max_cle = cle
            max_valeur = valeur
    return max_cle, max_valeur



class Pile:
    """Classe définissant une structure de pile."""
    def __init__(self):
        self.contenu = []

    def est_vide(self):
        """Renvoie un booléen indiquant si la pile est vide."""
        return self.contenu == []

    def empiler(self, v):
        """Place l'élément v au sommet de la pile"""
        self.contenu.append(v)

    def depiler(self):
        """
        Retire et renvoie l'élément placé au sommet de la pile,
        si la pile n’est pas vide. Produit une erreur sinon.
        """
        assert not self.est_vide()
        return self.contenu.pop()

def eval_expression(tab):
    p = Pile()
    for element in tab: 
        if element != '+' and element != '*': 
            p.empiler(element) 
        else:
            if element == '+': 
                resultat = p.depiler() + p.depiler() 
            else:
                resultat = p.depiler() * p.depiler() 
            p.empiler(resultat) 
    return p.depiler() 


