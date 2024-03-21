from distance import leven
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

data = []
with open('dict_fr.txt') as f:
    contents = f.read()
    data = contents.split('\n')

dico_index = {'a': (1, 6140), 'b': (6141, 9708), 'c': (9709, 17375), 'd': (17376, 22159),
              'e': (22160, 26703), 'f': (26704, 29266), 'g': (29267, 31690), 'h': (31691, 33813),
              'i': (33814, 37009), 'j': (37010, 37552), 'k': (37553, 37853), 'l': (37854, 39816),
              'm': (39817, 44287), 'n': (44288, 45692), 'o': (45693, 47277), 'p': (47278, 54315),
              'q': (54316, 54752), 'r': (54753, 58853), 's': (58854, 64186), 't': (64187, 67955),
              'u': (67956, 68362), 'v': (68363, 69995), 'w': (69996, 70133),
              'x': (70134, 70215), 'z': (70293, 70752)}


def proche(mot:str)->list[str]:
    """
    Fonction qui renvoie les mots les plus proches du mot donné en paramètre
    :param mot: mot dont on veut trouver les mots les plus proches
    :return: liste des mots les plus proches
    # TODO a mettre dans l'ordre le plus proche. 
    """
    mots = []
    premier_lettre = mot[0]
    debut, fin = dico_index[premier_lettre]
    for mot_dico in data[debut:fin]:
        distance = leven(mot, mot_dico)
        if distance <= 3:
            mots.append((distance,mot_dico))
        mots.sort()
    return [truc for _, truc in mots[:3]]

print(proche('gossot'))