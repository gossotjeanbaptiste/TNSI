def fibonnaci(n):
    if n == 0:
        return 0
    else:
        if n == 1:
            return 1
        else:
            return fibonnaci(n-1) + fibonnaci(n-2)


print(fibonnaci(1))
print(fibonnaci(2))
print(fibonnaci(25))


def eleves_du_mois(eleves, notes):
    note_maxi = 0
    meilleurs_eleves = []

    for i in range(len(eleves)):
        if notes[i] == note_maxi:
            meilleurs_eleves.append(eleves[i])
        elif notes[i] > note_maxi:
            note_maxi = notes[i]
            meilleurs_eleves = [eleves[i]]

    return (note_maxi, meilleurs_eleves)


eleves_nsi = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
notes_nsi = [30, 40, 80, 60, 58, 80, 75, 80, 60, 24]
print(eleves_du_mois(eleves_nsi, notes_nsi))
print(eleves_du_mois([], []))