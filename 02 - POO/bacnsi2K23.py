class Region:
    def __init__(self, nom_region):
        self.nom = nom_region
        self.tab_voisines = []
        self.tab_couleurs_disponibles = ['rouge', 'vert', 'bleu', 'jaune', 'orange', 'marron']
        self.couleur_attribuee = None
    def renvoie_premiere_couleur_dispo(self):
        #Q4
        return self.tab_couleurs_disponibles[0]
    def renvoie_nb_voisines(self):
        #Q5
        return len(self.tab_voisines)
    def est_coloriee(self):
        #Q6
        return not (self.couleur_attribuee is None)
    def retire_couleur(self, couleur):
        #Q7
        if couleur in self.tab_couleurs_disponibles:
            self.tab_couleurs_disponibles.remove(couleur)      
    def est_voisine(self, region):
        #Q8
        for voisine in self.tab_voisines:
            if region.nom_region == voisine:
                return True
        return False



class Pays:
    def __init__(self, tab_region):
        self.tab_region = tab_region
        
    def renvoie_tab_region_no_colored(self):
        #Q9
        answer = []
        for i in self.tab_region:
            if not i.est_coloriee:
                answer.append(i)
            return answer
    def renvoie_max(self):
        #Q10
        #a)la méthode renvoie None ssi toutes les regions sont coloriées
        #b) Non coloriée et celle dont le nombre de region est au maximum
        nb_voisine_max = -1
        region_max = None
        for reg in self.renvoie_tab_region_no_colored():
            if reg.renvoie_nb_voisines() > nb_voisine_max:
                nb_voisine_max = reg.renvoie_nb_voisines()
                region_max = reg
        return region_max
    def colorie(self):
        #Q11
        region_colorie = self.renvoie_max()
        while region_colorie:
            couleur_dispo = region_colorie.renvoie_premiere_couleur_dispo()
            region_colorie.couleur_attribue = couleur_dispo
            for voisine in region_colorie.tab_voisine:
                if couleur_dispo in voisine.self.tab_couleurs_disponibles():
                    voisine.retire_couleur(couleur_dispo)
            region_colorie = self.renvoie_max()