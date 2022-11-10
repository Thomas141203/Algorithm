def init(m, n):
    var = float('inf')
    T = []
    for j in range(m):
        L = []
        for i in range(n):
            L.append(var)            
        T.append(L)
    return T

def cmax(T,i,j):
    if T[i][j] > T[i-1][j] and T[i][j] > T[i][j-1]:
        return i, j
    elif T[i-1][j] > T[i][j] and T[i-1][j] > T[i][j-1]:
        return i-1, j
    elif T[i][j-1] > T[i][j] and T[i][j-1] > T[i-1][j]:
        return i, j-1

def monter(T, i, j):
    while cmax(T, i, j) != (i, j):
        a, b = cmax(T, i, j)
        T[a, b], T[i, j] = T[i, j], T[a, b]
        i, j = a, b
    
def cmin(T, i, j):
    a, b = i, j
    if i < len(T)-1 and T[i+1][j] < T[i][j]:
        a = i+1
    if j < len(T[0])-1 and T[i][j+1] < T[a][b]:
        a, b = i, j+1
    return a, b

def descendre(T, i, j):
    while cmin(T, i, j) != (i, j):
        a, b = cmin(T, i, j)
        T[a][b], T[i][j] = T[i][j], T[a][b]
        i, j = a, b
    
def inserer(T, x):
    n, m = len[T], len(T[0])
    T[n-1][m-1] = x
    monter(T, n-1, m-1)
        
def suppression_min(T):
    est_vide = True
    for x in T:
        if x != float("inf"):
            est_vide = False
    if est_vide == True:
        return "erreur à l'écran"
    else:
        T[0][0] = float("inf")
        return  T[0][0]
    
def tri_tableau(L):
    for x in L:
        inserer(L, x)
        suppression_min(L)
    print(L)

        
L = [37, 6, 1, 8, 42, 27, 20, 7, 31, 32] 
tri_tableau(L)