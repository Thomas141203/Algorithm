
from math import*
from random import*

def en_prise(r,i,j):
    return r[i] == r[j] or abs(r[i]-r[j]) == abs(i-j)

def pos_valide(r,n):
    ok, i = True, 0
    while ok and i < n-1:
        j=i+1
        while ok and j<=n-1:
            ok = not en_prise(r,i,j)
            j += 1
        i += 1
    return ok
        
def reine():
    r = list(range(8))
    while not pos_valide(r, 8):
        a = randint(0,7)
        b = randint(0,7)
        r[a], r[b] = r[b], r[a]
    print(r)
    
    
reine()