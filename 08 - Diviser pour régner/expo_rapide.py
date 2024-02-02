def exponantiation_rapide(x, n):
    if n == 1:
        return x
    elif n == 0:
        return 1
    else:
        a = exponantiation_rapide(x, n // 2)
        if n % 2 == 0:
            return a * a 
        else:
            return a * a * x
        
print(exponantiation_rapide(5, 112))