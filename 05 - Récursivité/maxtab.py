from icecream import ic
def rechercheMaxRec(tab):
    #cas de base
    if len(tab) == 1:
        return tab[0]
    #recursion step
    else:
        #le slicing n'est pas au programme mais c'est plus simple
        ic((tab[0], tab[1:]))
        return max(tab[0], rechercheMaxRec(tab[1:]))
    
