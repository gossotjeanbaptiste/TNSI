import json 
import time
with open('fibo.json', 'r', encoding='utf-8') as file:
    fibocache = json.load(file)



# * renvoie le n-ième terme de la suite de Fibonacci
# * mémorisant les valeurs déjà calculées -> méthode dynamique
def fib_rec_dyn(n, cpt = 0):
    if str(n) in fibocache.keys():
        return fibocache[str(n)]
    cpt += 1
    fibocache[str(n)] = fib_rec_dyn(n-1, cpt) + fib_rec_dyn(n-2, cpt)
    if cpt > 10:
        update_json()
        cpt = 0
    return fibocache[str(n)]

def update_json():
    with open('fibo.json','w+') as json_file:
        json.dump(fibocache, json_file)


start = time.time()
print(fib_rec_dyn(100))
end = time.time()
print(end - start)