
def enumere(L):
    dico = {}
    for position, val in enumerate(L):
        if val in dico.keys:
            dico[val].append(position)
        else:
            dico[val] = [position]
    return dico