LEN_PILE = 100
def creer_pile():
    return {"tableau" : ['-'] * LEN_PILE,
            "position_sommet" : -1
           }
def est_vide(pile):
    return pile["position_sommet"] == -1

def empiler(pile, element):
    # à écrire
    if pile['position_sommet'] < LEN_PILE:
        pile['position_sommet'] = pile['position_sommet'] +  1
        nouvelle_pos = pile['position_sommet']
        pile["tableau"][nouvelle_pos] = element 

def depiler(pile):
    # à écrire
    if est_vide(pile):
        return None
    else:
        sommet = pile['tableau'][pile['position_sommet']]
        pile['tableau'][pile['position_sommet']] = '-'
        pile['position_sommet'] = pile['position_sommet'] -1
        return sommet
