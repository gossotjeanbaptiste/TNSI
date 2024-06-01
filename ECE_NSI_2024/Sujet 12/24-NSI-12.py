from random import randint

def tri_selection(tab):
    for i in range(len(tab)):
        min = i
        for j in range(i+1, len(tab)):
            if tab[j] < tab[min]:
                min = j
        tab[i], tab[min] = tab[min], tab[i]
        
tab = [1, 52, 6, -9, 12]
tri_selection(tab)
print(tab)

def plus_ou_moins():
    nb_mystere = randint(1, 99) 
    nb_test = int(input("Proposez un nombre entre 1 et 99 : "))
    compteur = 0 
    while nb_mystere != nb_test and compteur < 10: 
        compteur = compteur + 1
        if nb_mystere < nb_test: 
            nb_test = int(input("Trop petit ! Testez encore : "))
        else:
            nb_test = int(input("Trop grand ! Testez encore : "))
    if nb_mystere == nb_test:
        print ("Bravo ! Le nombre était ", str(nb_mystere) + ".") 
        print("Nombre d'essais : ", + str(compteur) + ".")
    else:
        print ("Perdu ! Le nombre était ", str(nb_mystere) + '.') 

