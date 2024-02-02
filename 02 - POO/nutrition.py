class Aliment:
    # constructeur
    def __init__(self, nom, energie, lipide, glucide, fibre, proteine, sel):
        self.nom = nom
        self.energie = energie
        self.lipide = lipide
        self.glucide = glucide
        self.fibre = fibre
        self.proteine = proteine
        self.sel = sel
        """
    def getGlucide(self): #getter permet d'obtenir la valeur de l'attribut
        return self.glucide
    def setGlucide(self, new_value): #setter permet de modifier la valeur de l'attribut
        self.glucide = new_value
        """
    def __repr__(self):
        return f"Intitulé : {self.nom} \nEnergie : {self.energie} \nLipides : {self.lipide} \nGlucides : {self.glucide} \nFibres : {self.fibre} \nProteines : {self.proteine} \nSel : {self.sel}"

    def masse_aliment(tableau_aliment):
        masse = 0
        #pythonesque ++
        for _, poids in tableau_aliment: # _, = joker pour ne pas utiliser la variable
            masse += poids
        """ 
        #pythonesque +
        for truc in tableau_aliment:
            masse += truc[1]
        
        #à l'arrache 
        for i in range(len(tableau_aliment)):
            masse += tableau_aliment[i][1]
            """
        return masse

def energie_plat(tableau_aliment):
    energie_total = 0
    for aliment, masse in tableau_aliment:
        energie_total += aliment.energie * masse / 100
    return f"{energie_total} kj"

def proteines_plat(tableau_aliment):
    proteine_total = 0
    for aliment, masse in tableau_aliment:
        proteine_total += aliment.proteine * masse / 100
    return f"{proteine_total} g"

def fiche_info(tableau_aliment):
    return {'Energie': energie_plat(tableau_aliment), 'Proteines': proteines_plat(tableau_aliment)}

# instanciation de l'aliment Riz
riz = Aliment("Riz Blanc", 1532, 0.6, 81, 1.3, 7.2, 0.01)
thon = Aliment("Thon", 490, 1.6, 0, 0, 25.6, 1.2)

salade_de_riz = [(riz, 500), (thon, 200)]

