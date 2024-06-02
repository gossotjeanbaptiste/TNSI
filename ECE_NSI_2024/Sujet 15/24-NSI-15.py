def moyenne(tab):
    somme = 0
    for i in range(len(tab)):
        somme += tab[i]
    return somme / len(tab)

print(moyenne([1.0]))
print(moyenne([1.0, 2.0, 4.0]))

def binaire(a):
    '''convertit un nombre entier a en sa representation 
    binaire sous forme de chaine de caractères.'''
    if a == 0:
        return '0' 
    bin_a = '' 
    while a > 0: 
        bin_a = str(a % 2) + bin_a
        a = a // 2 
    return bin_a

print(binaire(83))
print(binaire(6))
print(binaire(127))
print(binaire(0))