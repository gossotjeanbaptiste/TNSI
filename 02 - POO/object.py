from colorama import Fore, Back, Style, init
class Point:
    # un point de plan
    def __init__(self, x, y, color = '#000000'):
        self.abscisse = x
        self.ordonnee = y
        self.couleur = color
    # methpde deplace le point
    def deplace(self, dx, dy):
        self.abscisse += dx
        self.ordonnee += dy
    def rotation180(self):
        self.abscisse = -self.abscisse
        self.ordonnee = -self.ordonnee
    # méthode d'affichage
    def __repr__(self):
        return Fore.BLUE + f"({self.abscisse!r}, {self.ordonnee!r})" + Style.RESET_ALL

#ecrire une fonction qui prends en argument deux Points et renvoie un autre point qui est le milieu de ces deux points

def milieu(point1, point2):
    '''
    x = (point1.abscisse + point2.abscisse)/2
    y = (point1.ordonnee + point2.ordonnee)/2
    return Point(x, y)
    '''
    return Point((point1.abscisse + point2.abscisse)/2, (point1.ordonnee + point2.ordonnee)/2)