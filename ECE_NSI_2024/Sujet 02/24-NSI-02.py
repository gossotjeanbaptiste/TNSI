def correspond(mot:str, mot_a_trou:str)->bool:
    if len(mot) != len(mot_a_trou):
        return False
    for i in range(len(mot)):
        if mot_a_trou[i] != '*' and mot[i] != mot_a_trou[i]:
            return False
    return True

print(correspond('INFORMATIQUE', 'INFO*MA*IQUE'))
print(correspond('AUTOMATIQUE', 'INFO*MA*TIQ*E'))
print(correspond('STOP', 'S*'))
print(correspond('AUTO', '*UT*'))

print('**********')

def est_cyclique(plan):
    '''Prend en paramètre un dictionnaire `plan` correspondant à 
    un plan d'envoi de messages (ici entre les personnes A, B, C,
    D, E, F).
    Renvoie True si le plan d'envoi de messages est cyclique et 
    False sinon.'''
    expediteur = 'A'
    destinataire = plan[expediteur] 
    nb_destinataires = 1

    while destinataire != expediteur:
        destinataire = plan[destinataire] 
        nb_destinataires = nb_destinataires + 1

    return nb_destinataires == len(plan) 


print(est_cyclique({'A':'E','F':'A','C':'D','E':'B','B':'F','D':'C'}))
print(est_cyclique({'A': 'E', 'F': 'C', 'C': 'D', 'E': 'B', 'B': 'F', 'D': 'A'}))
print(est_cyclique({'A': 'B', 'F': 'C', 'C': 'D', 'E': 'A', 'B': 'F', 'D': 'E'}))
print(est_cyclique({'A': 'B', 'F': 'A', 'C': 'D', 'E': 'C', 'B': 'F', 'D': 'E'}))

