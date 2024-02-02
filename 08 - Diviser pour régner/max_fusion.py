def max_fusion(tab):
    if len(tab) == 1:
        return tab[0]
    else:
        milieu = len(tab)//2
        a = max_fusion(tab[:milieu])
        b = max_fusion(tab[milieu:])
        if a < b:
            return b
        else:
            return a
        # return max(max_fusion(tab[:milieu]), max_fusion(tab[milieu:]))


print(max_fusion([1, 8, 4, 12, 13, 2]))
