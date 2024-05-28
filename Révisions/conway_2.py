def conway_rec(n):
        reponse  = "" 
        texte = str(n)+' '
        n = len(texte)
        cpt = 1
        last = False
        for i in range(n-1):
            if texte[i] == texte[i+1]:
                cpt +=1
            else:
                reponse = reponse+str(cpt)+str(texte[i])
                cpt = 1
        return reponse
 
def suite(n):
    texte ='1'
    resultat = []
    resultat.append(int(texte))
    for i  in range(n):
         texte = conway_rec(int(texte))
         resultat.append(int(texte))
    return resultat

test = suite(10)
for tr in test:
    print(tr)