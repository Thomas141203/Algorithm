from time import time

def eratosthene(n):
    prime = [True]*(n+1)
    print(prime)
    for i in range(2, n+1, 1):
        if prime[i]:
            print(str(i))
            for ki in range(i*i, n+1, i):
                prime[ki] = False
    return prime

a= time()
eratosthene(50000)
b = time()
print(b-a)