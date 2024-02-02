def fact(n):
    if n <= 1:
        return 1
    else:
        return n*fact(n-1)
    
def somme_chiffre(n):
    reponse = 0
    chaine = str(n)
    for chiffre in chaine:
        reponse += int(chiffre)
    return reponse


def multiple_neuf(n):
    if n < 10:
        return n == 9
    else:
        return multiple_neuf(somme_chiffre(n))
    

def fibonnaci(n):
    #cas de base
    if n <= 1:
        return 1
    else:
        return fibonnaci(n-1) + fibonnaci(n-2)
    
def pgcd(n1, n2): #plus grand diviseur commun algo d'euclide
    reste = n1 % n2
    if reste == 0:
        return n2
    else:
        return pgcd(n2, reste)
    
    
def maximum(tab):
    if tab == []:
        return 0
    else:
        return 1 + maximum(tab[1:])