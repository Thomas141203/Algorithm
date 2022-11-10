def nombrePremier(n):
    for i in range(2, n):
        if (n%i)==0:
            return True
    return False

print(nombrePremier(35))