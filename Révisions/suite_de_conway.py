def suite_de_conway_rec(n, seq="1"):
    if n == 1:
        return seq
    else:
        new_seq = ""
        i = 0
        while i < len(seq):
            count = 1
            while i + 1 < len(seq) and seq[i] == seq[i+1]:
                i += 1
                count += 1
            new_seq += str(count) + seq[i]
            i += 1
        return suite_de_conway_rec(n-1, new_seq)


def suite_de_conway(n, seq="1"):
    for _ in range(n-1):
        new_seq = ""
        i = 0
        while i < len(seq):
            count = 1
            while i + 1 < len(seq) and seq[i] == seq[i+1]:
                i += 1
                count += 1
            new_seq += str(count) + seq[i]
            i += 1
        seq = new_seq
    return seq

print(suite_de_conway_rec(5))
print(suite_de_conway(5))