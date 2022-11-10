#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' 
info3A
TP1
'''

from random import randint
from math import sqrt

#1 somme des chiffres avec chaine
def sdc2(n):
    c=str(n)
    s=0
    for c in s:
        s+=int(c)
    return s
#n = int(input())
#print(sdc2(n))

# 2
#n = int(input())
#est_premier=True 
#d=2
#while d<n and est_premier:
##optimisé : while d*d<=n and estpremier:
#    if n%d==0: 
#        est_premier=False
#    d+=1
#print(est_premier)

    
# 3 conway
def suivant(s): 
    n=1 #le premier caractère y est une fois.
    c=""
    for i in range(1,len(s)+1): #boucle à partir de l'indice 1.
        if i<len(s) and s[i]==s[i-1]: #même caractère
            n+=1
        else:
            c+=(str(n)+s[i-1])
            n=1
    return c

def suite(n):
    L=["1"]
    for i in range(1,n):
        L.append(suivant(L[-1]))
    return L
  
def rapport(n):
    L=suite(n)
    for i in range(n-1):
        print(len(L[i+1])/len(L[i]))

#n = int(input())
#print(suite(n))
#rapport(n)
    

#4 matrices
def init_mat_alea(m,n,sup):
    T=[[0]*n for i in range(m)]
    for i in range(m):
        for j in range(n):
            T[i][j]=randint(0,sup)
    return T
#variante
def matrice_alea(m,n,sup):
    return [[randint(0,sup) for i in range(n)] for j in range(m)]
    
#les trois fonctions suivantes ont été vues en CM sur des listes 1D
def somme(T):
    s=0
    for i in range(len(T)):
        for j in range(len(T[0])):
            s+=T[i][j]
    return s

def pos_min(T):
    im, jm=0, 0
    for i in range(len(T)):
        for j in range(len(T[0])):
            if T[i][j]<T[im][jm]:
                im, jm=i, j
    return im, jm

def est_croissante(T):
    l=len(T)
    c=len(T[0])
    for i in range(l):
        for j in range(c-1):
            if T[i][j]>T[i][j+1]:
                return False
        if i<len(T)-1:
            if T[i][c-1]>T[i+1][0]:
                return False
    return True

#S=init_mat_alea(3,4,20)
#print(S)
#print(est_croissante(S))
#T=init_mat3(2,3)
#print(T)
#print(est_croissante(T))
#print(somme(T))
#print(pos_min(S))

# 5 pascal
def pascal(n):
    T = [[0]*n for i in range(n)]
    for i in range(n): 
       for j in range(i+1):
           if (j == 0 or i == j):
               T[i][j] = 1
           else:
               T[i][j] = T[i-1][j-1] + T[i-1][j]
#           print(T[i][j], end=" ")
#       print()
    return T

#variante
def pascal2(n):
    T= [[1]] 
    for i in range(1, n):
        ligne_suivante = [1] * (i+1)
        for j in range(1, i):
            ligne_suivante[j] = T[i-1][j] + T[i-1][j-1]
        T.append(ligne_suivante)
    return T

#n = int(input())
#pascal(n)
#print(pascal2(n))  

def is_squarefree(n):  
    for i in range(2,int(sqrt(n))+1): 
        if n % (i*i) == 0:
            return False
    return True

#Détermine la somme des entiers squarefree distincts du triangle de Pascal
def pb203(n):
    T = pascal(n)
    sqrfree = []
    s=0
    for L in T:
        for x in L:
            if x not in sqrfree and is_squarefree(x):
                sqrfree.append(x)
                s+=x
    return s

#print(pb203(8))
#print(somme_squarefree_pascal(51))



