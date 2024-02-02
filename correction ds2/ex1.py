class Compte:
    def __init__(self, titulaire, numero_de_compte, solde = 0):
        self.titulaire = titulaire
        self.numero_de_compte = numero_de_compte
        self.solde = solde
        
    def deposer(self, valeur):
        assert valeur >=0, "Erreur valeur impossible à déposer"
        self.solde += valeur
        
    def a_decouvert(self):
        return self.solde < 0 #self.solde < 0 est directement un booléen
        
    def __repr__(self):
        return f' M ou Mme {self.titulaire}\n numéro de compte {self.numero_de_compte}\n solde {self.solde}€'
#1) 
mon_compte = Compte("Kbida Abdellatif", "1110-FR-45-tvgh-8806", 74255.88)
#La méthode invoquée par Compte est le constructeur : __init__.

#2) méthode déposer
#assert permet de définir une précondition

#3) méthode __repr__
#f-methods

#4)voir a_decouvert

#5) modifiier attribut
mon_compte.titulaire = 'Le Boss'