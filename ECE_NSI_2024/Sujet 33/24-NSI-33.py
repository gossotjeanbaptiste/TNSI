def renverse(str):
    new_str = ""
    for i in range(len(str), 0, -1):
        new_str = new_str + str[i-1]
    return new_str

print(renverse(""))
print(renverse("abc"))
print(renverse("informatique"))


def crible(n):
    """Renvoie un tableau contenant tous les nombres premiers
    plus petits que n."""
    premiers = []
    tab = [True] * n
    tab[0], tab[1] = False, False
    for i in range(n):
        if tab[i]:
            premiers.append(i) 
            multiple = i * 2 
            while multiple < n:
                tab[multiple] = False 
                multiple = multiple + i 
    return premiers

print(crible(40))
print(crible(5))
