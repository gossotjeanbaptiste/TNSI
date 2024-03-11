
'''
Le codage par différence (delta encoding en anglais) permet de compresser un tableau
de données en indiquant pour chaque donnée, sa différence avec la précédente (plutôt
que la donnée elle-même). On se retrouve alors avec un tableau de données plus petit,
nécessitant donc moins de place en mémoire. Cette méthode se révèle efficace lorsque
les valeurs consécutives sont proches.
Programmer la fonction delta(liste) qui prend en paramètre un tableau non vide de
nombres entiers et qui renvoie un tableau contenant les valeurs entières compressées à
l’aide de cette technique.
'''


def delta_ia(liste):
    res = [liste[0]]
    for i in range(1, len(liste)):
        res.append(liste[i] - liste[i-1])
    return res


print("Fonction delta faite par IA")
print(delta_ia([1000, 800, 802, 1000, 1003]))
print(delta_ia([42]))
print('-----------------------------')


def delta_ece(liste):
    resultat = []
    if liste == []:
        return None
    else:
        resultat.append(liste[0])
        for i in range(len(liste)-1):
            resultat.append(liste[i+1] - liste[i])
    return resultat


print('Fonction delta faites par l\'humain en ECE')
print(delta_ece([1000, 800, 802, 1000, 1003]))
print(delta_ece([42]))
