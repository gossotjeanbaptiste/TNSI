notes_eval = [2, 0, 5, 9, 6, 9, 10, 5, 7, 9, 9, 5, 0, 9, 6, 5, 4]


def effectif_notes(notes):
    """renvoie un tableau de 11 entiers, le i-ème élément du tableau
    contient le nombre d'occurrences de la note i."""
    eff = [0] * 11
    for note in notes:
        eff[note] += 1
    return eff


eff = effectif_notes(notes_eval)
assert eff == [2, 0, 1, 0, 1, 4, 2, 1, 0, 5, 1], "Test 1"
print('Test 1 : ok')
print(eff)  # ![2, 0, 1, 0, 1, 4, 2, 1, 0, 5, 1]
print('----------------------------')


def notes_tries(eff):
    """renvoie un tableau de notes triées dans l'ordre croissant."""
    notes = []
    for i in range(11):
        notes.extend([i] * eff[i])
    return notes


notes = notes_tries(eff)
assert notes == [0, 0, 2, 4, 5, 5, 5, 5, 6, 6, 7, 9, 9, 9, 9, 9, 10], "Test 2"
print('Test 2 : ok')
print(notes)  # [0, 0, 2, 4, 5, 5, 5, 5, 6, 6, 7, 9, 9, 9, 9, 9, 10]
print('----------------------------')


def dec_to_bin(nb_dec):
    q, r = nb_dec // 2, nb_dec % 2
    if q == 0:
        return str(r)
    else:
        return dec_to_bin(q) + str(r)


assert dec_to_bin(25) == '11001', "Test 1"
print('Test 1 : ok')
print(dec_to_bin(25))  # 11001
print('----------------------------')


def bin_to_dec(nb_bin):
    if len(nb_bin) == 1:
        if nb_bin == '0':
            return 0
        else:
            return 1
    else:
        if nb_bin[-1] == '0':
            bit_droit = 0
        else:
            bit_droit = 1
        return bit_droit + 2 * bin_to_dec(nb_bin[:-1])


assert bin_to_dec('101010') == 42, "Test 2"
print('Test 2 : ok')
print(bin_to_dec('101010'))  # 42
print('----------------------------')
