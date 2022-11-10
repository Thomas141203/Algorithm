def sommeChiffre(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    print(s)

def sommeChiffreV2(n):
    s = str(n)
    a = list(map(int, s.strip()))
    return sum(a)

sommeChiffre(11229129)
print(sommeChiffreV2(11229129))
