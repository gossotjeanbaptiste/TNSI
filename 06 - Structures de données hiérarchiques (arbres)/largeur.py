from collections import deque

class ArbreBinaire:
    def __init__(self, valeur, gauche = None, droite = None):
        self.valeur = valeur
        self.gauche = gauche
        self.droite = droite
        
    
    
    def __repr__(self):
        return f'({self.valeur}, {self.gauche}, {self.droite})'
    
    
A = ArbreBinaire('A', ArbreBinaire('S', ArbreBinaire('W')),
                 ArbreBinaire('I', ArbreBinaire('L'), ArbreBinaire('O')))

L = []
F = deque()
F.append(A)
while F:
    x = F.popleft()
    L.append(x.valeur)
    if x.gauche:
        F.append(x.gauche)
    if x.droite:
        F.append(x.droite)
        
print(L)