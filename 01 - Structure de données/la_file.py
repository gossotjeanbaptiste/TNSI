len_file = 10
def creer_file():
    return { "tableau" : ['-'] * len_file,
            "position_tete" : 0,
            "nombre_element" : 0}

def est_vide_file(file):
    return file ["nombre_element"] == 0  # True / False

def ajouter_file(file, element):
    nouvelle_position = (file["position_tete"] + file["nombre_element"]) % len_file
    file["tableau"][nouvelle_position] = element
    #incremente le nb d'élément
    file["nombre_element"] += 1


def retirer_file(file):
    if not (est_vide_file(file)):
        pos = file["position_tete"]
        sommet = file["tableau"][pos]
        file["tableau"][pos] = '-'
        file["position_tete"] = (file["position_tete"] + 1 ) % len_file
        file["nombre_element"] = file["nombre_element"] - 1
        return sommet
    else:
        return None
