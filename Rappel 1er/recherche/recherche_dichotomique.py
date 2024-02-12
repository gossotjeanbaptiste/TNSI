def dichotomie(tab, valeur):
    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        milieu = (debut + fin) // 2
        if tab[milieu] == valeur:
            return milieu
        elif tab[milieu] > valeur:
            fin = milieu - 1
        else:
            debut = milieu + 1
    return -1


test = [3*i+8 for i in range(10000)]

assert dichotomie(test, 1626) == -1, 'Attention pb test 1'
print(f'test 1 ok -> {dichotomie(test, 1626)}')

assert dichotomie(test, 1526) == 506, 'Attention pb test 2'
print(f'test 2 ok --> {dichotomie(test, 1526)}')
