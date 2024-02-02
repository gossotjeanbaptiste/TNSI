class Chien:
    def __init__(self, nom, race, date_naissance, num_tatouage):
        self.nom = nom
        self.race = race
        self.date_naissance = date_naissance
        self.num_tatouage = num_tatouage

    def abboie(self):
        print("Waouf ! Waouf !")

    def age(self):
        return (2023 - int(self.date_naissance[6:])) * 7

    def __repr__(self):
        return f"Je m'appelle {self.nom}, je suis un chien \U0001F415 de la race des {self.race}, mon identifitant est {self.num_tatouage} et j'ai {self.age()} ans"
