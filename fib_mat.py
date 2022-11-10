from math import*
from time import*

def mat22mult(A, B):
    C = []
    C.append(A[0]*B[0] + A[1]*B[2])
    C.append(A[0]*B[1] + A[1]*B[3])
    C.append(A[2]*B[0] + A[3]*B[2])
    C.append(A[2]*B[3] + A[1]*B[3])
    return C

def mat22expo(A, n):
    B = []
    for i in range(n/2):
        B = mat22mult(A, A)
    return B

def expoRap(x, n):
    res = 1
    while n != 0:
        if n%2 == 1:
            res *= x
        x *= x
        n//=2
    return res


def fib_mat(n):
    res = 0
    a = 1/sqrt(5)
    b = (1+sqrt(5))/2
    c = (1-sqrt(5))/2
    
    res = a * (expoRap(b, n) - expoRap(c, n))
    
    return round(res)
 
    
a= time()
print(fib_mat(50))
b = time()
print(b-a)
