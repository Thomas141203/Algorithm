def tri_comptage(A):
    k = max(A)
    C = [0]*(k+1) 
    for i in range(len(A)): 
        C[A[i]] += 1
    p = 0
    for i in range(k+1): 
        for j in range(C[i]): 
            A[p] = i
            p+=1 
    return A

Liste = [5, 7, 5, 2, 1, 1]
print(tri_comptage(Liste))

def tri_comptage_ameliorer(A):
    imax = max(A)
    imin = min(A)
    p = imax - imin+1
    C = [0]*(p)
    for x in A:
        C[x-imin] += 1
    T = []
    for i in range(p): 
        for j in range(C[i]):
            T.append(imin+i)
    return T

print(tri_comptage_ameliorer(Liste))