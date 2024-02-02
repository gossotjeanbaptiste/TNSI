def creer_liste():
    return None

def est_vide(L):
    return L is None

def ajouter_en_tete(x, L):
    return (x, L)

def tete(L):
    return L[0]

def queue(L):
    return L[1]

def nb_element(L):
    compteur = 0 
    temp = L
    while not est_vide(temp):
        compteur += 1
        temp = queue(temp)
    return compteur

def val(i, L):
    assert i < nb_element(L), "Out of range"
    temp = L
    for e in range(i):
        temp = queue(temp)
    return tete(temp)

def est_dans(x, L):
    if est_vide(L):
        return False
    else:
        if x == tete(L):
            return True
        else:
            return False or est_dans(x, queue(L))