from pile import *
# application reconnaitre un palindrome
def palindrome(mot):
    alphabet = creer_pile()

    for lettre in mot:
        empiler(alphabet, lettre)

    tom = ""
    while not(est_vide(alphabet)):
        tom += depiler(alphabet)
    return  tom == mot
