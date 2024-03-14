fibocache = {1 : 1, 2: 1}
def fib_rec_dyn(n):
    if n in fibocache.keys():
        return fibocache[n]
    value = fib_rec_dyn(n-1) + fib_rec_dyn(n-2)
    fibocache[n] = value
    return value

print(fib_rec_dyn(7))