from la_file import *
from collections import namedtuple


# tableau de 3 files
# urgence[0]=vert -> moins urgent
# urgence[1]=orange -> urgent
# urgence[2]=rouge -> très urgent
# urgence[0] --> urgence[1] --> urgence[2]

urgence = [creer_file(), creer_file(), creer_file()]

# patient sera modeliser par un tuple
# ("nom prenom", "pathologie", priorité 0, 1, 2)

jb = ("Jean-Baptiste Gossot", "plaie ouverte au doigt", 1)
matheo = ("Matheo", "rein détaché", 2)
zorro = ("Don Diego de la Vega", "blessure par arme blanche", 2)
ezio = ("Ezio Auditore", "Chute d'un toit", 0)
mario = ("Mario Bros", "conso de champi inconnue", 1)
homer = ("Homer Simpson", "état d'ébriété", 0)


def enfiler_prio(patient):
    # on insère le patient dans la file correspondant à sa priorité
    ajouter_file(urgence[patient[2]], patient)


def defiler_prio():
    if not est_vide_file(urgence[2]):
        return retirer_file(urgence[2])
    elif not est_vide_file(urgence[1]):
        return retirer_file(urgence[1])
    else:
        return retirer_file(urgence[0])
    
def affichage():
    for indice, file in enumerate(urgence):
        print(f"file {indice} : {file['tableau']}")
        print('*************************')

enfiler_prio(homer)
enfiler_prio(zorro)
affichage()
defiler_prio()
enfiler_prio(matheo)
affichage()
enfiler_prio(ezio)
enfiler_prio(mario)
defiler_prio()
enfiler_prio(jb)
defiler_prio()
defiler_prio()
defiler_prio()
defiler_prio()