
from math import*

def eval_pol(L, x):
    sum = 0
    for i in range(len(L)):
        sum += L[i]*pow(x, i)
    return sum
    
def eval_horner(L,x):
    val = L[len(L)-1]
    for i in range(len(L)-2,-1,-1):
        val = val * x + L[i]
    return val

def eval_horner_rec1(L,x):
    val = 0
    if L == []:
        return 0
    else:
        val = L[0] + x * eval_horner_rec1(L[1:], x)
    return val

def eval_horner_rec2(L, x, i=0):
    val = 0
    if i == len(L):
        return 0
    else:
        new = i + 1
        val = L[i] + x * eval_horner_rec2(L, x, new)
    return val
    
L = [-3, 5, 2, 7, -2, 3]
x = -1

print(eval_pol(L, x))
print(eval_horner(L, x))
print(eval_horner_rec1(L, x))
print(eval_horner_rec2(L, x))