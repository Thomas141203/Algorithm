from random import randint

def init_mat(m, n):
    T = []
    for j in range(m):
        L = []
        for i in range(n):
            L.append(4*j+i)            
        T.append(L)
    return T

def affiche_mat(T):
    for i in T:
        print(i)

def init_mat_alea(m, n, sup):
    T = [[0]*n for i in range(m)]
    for i in range(m):
        for j in range(n):
            val = randint(0,sup)
            T[i][j] = val
    return T
        
def somme(T):
    sum = 0
    for i in range(len(T)):
        for j in range(len(T[0])):
            sum += T[i][j]
    return sum

def pos_min(T):
    couple_min = T[0][0]
    for i in range(len(T)):
        for j in range(len(T[0])):
            if couple_min > T[i][j]:
                couple_min = T[i][j]
    return couple_min
    
def est_croissante(T):
    n = len(T)
    for i in range(n-1):
        for j in range(n-1):
            if T[i][j] > T[i+1][j+1]:
                return False
    return True

#print(init_mat(3,4))
#affiche_mat(init_mat(3,4))
#print(init_mat_alea(3,4,9))
#print(somme(init_mat_alea(3, 4, 9)))
#print(pos_min(init_mat_alea(3, 4, 9)))
#print(est_croissante(init_mat_alea(3, 4, 9)))