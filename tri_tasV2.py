
def imax_pere_fg_fd(L,i,p):
    x = i
    gauche = 2 * i + 1 
    droite = 2 * i + 2
    if gauche < p and L[gauche] > L[x]:
            x = gauche
    if droite < p and L[droite] > L[x]:
            x = droite
    return x

def entasser(L,i,p):
    L.append(L[:])
    j = i
    m = imax_pere_fg_fd(L, j, p)
    while m != j:
        L[j],L[m] = L[m],L[j]
        j = m
        m = imax_pere_fg_fd(L, j, p)
        L.append(L[:])

def construit_tas(L):
    n = len(L)
    for i in range(n//2-1, -1, -1):
        entasser(L, i, n)
        L.append(L[:])
    return L

def tri_tas(L):
    L.append(L[:])
    construit_tas(L)
    p = len(L)
    for i in range(p-1):
        L[0],L[p-1] = L[p-1],L[0]
        L.append(L[:])
        p-=1
        entasser(L, 0, p)

L = [9, 10, 0, 7, 1, 11, 6, 2, 8]
print(tri_tas(L))
