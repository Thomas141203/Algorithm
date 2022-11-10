from math import*

def pascal(n):
    P = [[1]]
    ligne = [1]
    for j in range(n):
        nl = ligne + [1]
        for i in range(len(ligne) - 1):
            nl[i+1] = ligne[i] + ligne[i+1]
        ligne = nl
        P.append(ligne)
        print(P)


def squareFree(n):
    triangle = pascal2(n)
    sqrfree = []
    for L in triangle:
         for x in L:        
             if x not in sqrfree and is_squarefree(x):
                 sqrfree.append(x)
    return sum(sqrfree)

        
def is_squarefree(n):
    if n == 0:
        return False
    for i in range(2, int(sqrt(n))+2):
        if n % (i*i) == 0:
            return False
    return True


def pascal2(n):
    pascal= [[1]] 
    for i in range(1, n+1):
        ligne_suivante = [1] * (i+1)
        for p in range(1, i):
            ligne_suivante[p] = pascal[i-1][p] + pascal[i-1][p-1]
        pascal.append(ligne_suivante)
    
    
    return pascal



#pascal(5)
print(squareFree(8))

