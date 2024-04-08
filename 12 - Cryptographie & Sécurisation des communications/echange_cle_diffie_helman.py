from random import randint # ! Nombre premier et générateur
from math import sqrt

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

prime_numbers = [num for num in range(1, 101) if is_prime(num)]

def liste_premiers_3_chiffres():
    tab = []
    for n in range(100, 1000):
        if is_prime(n):
            tab.append(n)
    return tab

liste = liste_premiers_3_chiffres()

print(prime_numbers)

def generate_public_key() -> tuple[int, int]:
    p = liste[randint(0, len(liste) - 1)]
    g = randint(2, p - 1)
    return (p, g)

# ? Chosir un nb alpha secret 
alpha = 63 # ! à modifier si l'on veut. 
p, g = generate_public_key()
print(f"clé publique = {p} base puissance,g = {g}")

def generate_symetric_key(M:int, p:int, alpha:int) -> int:
    return pow(M, alpha, p)

def transmit_message(g, p, alpha) -> int:
    return pow(g, alpha, p)

print(f"a transmettre : {transmit_message(g, p, alpha)}")
