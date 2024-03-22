notes_eval = [2, 0, 5, 9, 6, 9, 10, 5, 7, 9, 9, 5, 0, 9, 6, 5, 4]


def effectif_notes(notes: list) -> list:
    # ! renvoie un tableau de 11 éléments
    eff = [0] * 11
    # ! Deuxième méthode : compréhension
    # * eff = [0 for _ in range(11)]
    for note in notes:
        eff[note] += 1
    return eff


"""assert effectif_notes(notes_eval) == [2, 0, 1, 0, 1, 4, 2, 1, 0, 5, 1], 'Test 1 prblm'
print('test 1 ok')
print(effectif_notes(notes_eval))"""


def notes_tries(eff: list) -> list:
    resultat = []
    for i in range(len(eff)):
        for j in range(eff[i]):
            resultat.append(i)
    return resultat


"""eff = effectif_notes(notes_eval)
notes = notes_tries(eff)
assert notes == [0, 0, 2, 4, 5, 5, 5, 5, 6, 6, 7, 9, 9, 9, 9, 9, 10], "Test 2"
print('Test 2 : ok')
print(notes)  # [0, 0, 2, 4, 5, 5, 5, 5, 6, 6, 7, 9, 9, 9, 9, 9, 10]
print('----------------------------')"""


def notes_tries_v2(eff):
    # TODO faire la fonction notes triées 2
    # pass #! [5] * 4 -> [5, 5, 5, 5]
    note = []
    for i in range(11):
        note = note + [i]*eff[i]
    return note


"""eff = effectif_notes(notes_eval)
notes = notes_tries_v2(eff)
assert notes == [0, 0, 2, 4, 5, 5, 5, 5, 6, 6, 7, 9, 9, 9, 9, 9, 10], "Test 3"
print('Test 3 : ok')
print(notes)  # [0, 0, 2, 4, 5, 5, 5, 5, 6, 6, 7, 9, 9, 9, 9, 9, 10]
print('----------------------------')"""


def notes_tries_v3(eff):
    note = [i for i in range(11) for _ in range(eff[i])]
    return note


"""notes = notes_tries_v3(eff)
assert notes == [0, 0, 2, 4, 5, 5, 5, 5, 6, 6, 7, 9, 9, 9, 9, 9, 10], "Test 4"
print('test 4 ok')
print(notes)  # [0, 0, 2, 4, 5, 5, 5, 5, 6, 6, 7, 9, 9, 9, 9, 9, 10]
print('----------------------------')"""


def dec_to_bin(nb_dec: int) -> str:
    q, r = nb_dec // 2, nb_dec % 2
    if q == 0:
        return str(r)
    else:
        return dec_to_bin(q) + str(r)


"""assert dec_to_bin(25) == '11001', "Test 1"
print('Test 1 : ok')
print(dec_to_bin(25))  # 11001
print('----------------------------')"""


def bin_to_dec(nb_bin: str) -> int:
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
    return 2 * bin_to_dec(nb_bin[:-1]) + bit_droit 


print(bin_to_dec('11001'))
print(bin_to_dec('101010'))
"""assert bin_to_dec('101010') == 42, "Test 2"
print('Test 2 : ok')
print(bin_to_dec('101010'))  # 42
print('----------------------------')"""
