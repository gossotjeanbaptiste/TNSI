dico_rendu = {0: 0}


def rendu_rec_dyn(P, somme):
    if somme in dico_rendu.keys():
        return dico_rendu[somme]
    else:
        minimum = 1000
        for piece in P:
            if piece <= somme:
                nb_pieces = 1 + rendu_rec_dyn(P, somme - piece)
                if nb_pieces < minimum:
                    minimum = nb_pieces
        dico_rendu[somme] = minimum
        return minimum

print(rendu_rec_dyn([10, 5, 2], 11))
print(rendu_rec_dyn([10, 5, 2], 72))