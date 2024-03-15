def rendu_rec(P:list, somme:int)->int:
    if somme == 0:
        return 0
    else:
        minimum = 1000
        for piece in P:
            if piece <= somme:
                nb_piece = 1 + rendu_rec(P, somme - piece)
                if nb_piece < minimum:
                    minimum = nb_piece
        return minimum

print(rendu_rec([10, 5, 2], 11))