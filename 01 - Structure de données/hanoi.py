def nombre_hanoi(n):
    u_1 = 0
    u_2 = 0
    for i in range(n):
        u_1 = 2*u_1 + 1
        u_2 = 2**n - 1
    return u_1, u_2