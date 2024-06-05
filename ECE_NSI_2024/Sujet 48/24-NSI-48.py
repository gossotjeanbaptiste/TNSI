def voisins_entrants(graphe, sommet):
    '''Écrire une fonction voisins_entrants(adj, x) qui prend en paramètre le graphe
    donné sous forme de liste d’adjacence et qui renvoie une liste contenant les voisins entrants
    du sommet x, c’est-à-dire les sommets y tels qu’il existe une arête de y vers x.'''
    voisins = []
    for i in range(len(graphe)):
        if sommet in graphe[i]:
            voisins.append(i)
    return voisins



def nombre_suivant(s):
    '''Renvoie le nombre suivant de celui representé par s
    en appliquant le procédé de lecture.'''
    resultat = ''
    chiffre = s[0]
    compte = 1
    for i in range(1, len(s)): 
        if s[i] == chiffre:
            compte += 1 
        else:
            resultat += str(compte) + chiffre
            chiffre = s[i] 
            compte = 1
    lecture_chiffre = str(compte) + chiffre 
    resultat += lecture_chiffre
    return resultat


