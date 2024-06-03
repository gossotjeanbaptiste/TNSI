def fusion(tab1, tab2):
    new_tab = []
    for i in range(len(tab1)):
        new_tab.append(tab1[i])
    for i in range(len(tab2)):
        new_tab.append(tab2[i])
    for i in range(len(new_tab)):
        for j in range(i, len(new_tab)):
            if new_tab[i] > new_tab[j]:
                new_tab[i], new_tab[j] = new_tab[j], new_tab[i]
    return new_tab

print(fusion([3, 5], [2, 5]))
print(fusion([-2, 4], [-3, 5, 10]))
print(fusion([4], [2, 6]))
print(fusion([], []))
print(fusion([1, 2, 3], []))


romains = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
def traduire_romain(nombre):
    """ Renvoie l'écriture décimale du nombre donné en chiffres
    romains """
    if len(nombre) == 1:
        return romains[nombre[0]] 
    elif romains[nombre[0]] >= romains[nombre[1]]: 
        return romains[nombre[0]] + traduire_romain(nombre[1:]) 
    else:
        return -romains[nombre[0]] + traduire_romain(nombre[1:]) 
    
print(traduire_romain("XIV"))
print(traduire_romain("CXLII"))
print(traduire_romain("MMXXIV"))


