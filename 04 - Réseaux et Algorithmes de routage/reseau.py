class Reseau:
    def __init__(self, adresse, cidr):
        """    
        adresse une chaine de caractères
        cidr est un entier
        """
        self.adresse = adresse
        self.cidr = cidr
        
    def nombre_adresse(self):
        return 2**(32 - self.cidr)
    
    def masque(self):
        masque_bin = '1'*self.cidr + '0'*(32-self.cidr)
        #return [int(masque_bin[i:i+8]) for i in range(0, 32, 8)]
        #je veux que ca ce renvoie en décimal
        return [int(masque_bin[i:i+8], 2) for i in range(0, 32, 8)] #2 dans int() défini la base
    
    def masque_binaire(self):
        masque_bin = '1'*self.cidr + '0'*(32-self.cidr)
        return [int(masque_bin[i:i+8]) for i in range(0, 32, 8)]
    
    def adresse_reseau(self):
        adre = [int(element) for element in self.adresse.split('.')]
        return [(adr & masque) for adr, masque in zip(adre, self.masque())]
    
    def adresse_hote(self):
        adre = [int(element) for element in self.adresse.split('.')]
        return [(adr - masque) for adr, masque in zip(adre, self.adresse_reseau())]
    
    def meme_reseau(self, adresse):
        return self.adresse_reseau() == [truc & machin for truc, machin in zip(adresse, self.masque())] #adresse.adresse_reseau()
        
    def __repr__(self):
        return f'{self.adresse}/{self.cidr}'
    
mon_reseau = Reseau('91.198.174.2', 19)