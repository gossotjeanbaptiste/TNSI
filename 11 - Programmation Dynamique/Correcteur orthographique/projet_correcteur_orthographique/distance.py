def leven(chaine1, chaine2):
    n1 = len(chaine1)
    n2 = len(chaine2)
    deplacement = [[i for i in range(n2+1)] for j in range(n1+1)]
    for i in range(n1+1):
        deplacement[i][0]=i
    
    for i in range(1,n1+1):
        for j in range(1, n2+1):
            c = 0 if chaine1[i-1] == chaine2[j-1] else 1
            deplacement[i][j] = min(deplacement[i-1][j], deplacement[i][j-1], deplacement[i-1][j-1]) + c

    return deplacement[n1][n2]

