def verifie(tab):
    for i in range(1, len(tab)):
        if tab[i-1] > tab[i]:
            return False
    return True

print(verifie([0, 5, 8, 8, 9]))
print(verifie([8, 12, 4]))
print(verifie([-1, 4]))
print(verifie([]))
print(verifie([5]))

def depouille(urne):
    '''prend en paramètre une liste de suffrages et renvoie un 
    dictionnaire avec le nombre de voix pour chaque candidat'''
    resultat = {} 
    for bulletin in urne:
        if bulletin in resultat: 
            resultat[bulletin] = resultat[bulletin] + 1
        else:
            resultat[bulletin] = 1
    return resultat

def vainqueurs(election):
    '''prend en paramètre un dictionnaire non vide avec le nombre de voix
    pour chaque candidat et renvoie la liste des vainqueurs'''
    nmax = 0
    for candidat in election:
        if election[candidat] > nmax:
            nmax = election[candidat] 
    liste_finale = [ nom for nom in election if election[nom] == nmax] 
    return liste_finale 


print(depouille(['A', 'B', 'A']))
print(depouille([]))
election = depouille(['A', 'A', 'A', 'B', 'C',\
                    'B', 'C', 'B', 'C', 'B'])
print(election)
print(vainqueurs(election))
print(vainqueurs({'A': 2, 'B': 2, 'C': 1}))
