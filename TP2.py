"""
info3A
TP2
"""
#1 Trouve 1 solution au probleme des n dames
from random import randint

def prise2(dames,i,j):
    # deux dames sont sur la meme diagonale si la pente vaut 1 ou -1
    return abs(dames[j]-dames[i]) == abs(j-i)

def position_valide2(n,dames):
    ok = True
    i=0
    while ok and i<n-1 :
        j = i+1
        while ok and j<=n-1 :
            ok = not prise2(dames,i,j)
            j += 1
        i += 1
    return ok

def echanger(n,dames):
    a=randint(0,n-1) 
    b=randint(0,n-1)
    while b==a:
        b=randint(0,n-1)
    dames[a], dames[b] = dames[b], dames[a]

def une_solution():
    n = 8                   # nombre de dames
    dames = list(range(n))  # position des dames dans les n colonnes
    nb_echanges = 0
    while not position_valide2(n,dames):
        echanger(n,dames)
        nb_echanges += 1
    print(dames)
    print(nb_echanges,"echanges")

#une_solution()


#2 tours hanoi
#troisième solution itérative de wikipedia
#tour1 noire, tour2 blanche, tour3 noire
#chaque tour est représentée par une liste, dont la valeur à l'indice 0 est 
#la couleur : blanc = 1, noir = 0
#les valeurs aux indices > 0 représentent les disques posés sur la tour, 
#de bas en haut, repérés par leur tailles (numéros à partir de 1, plus le
#numéro est petit, plus le disque est grand)
#un disque de numéro impair est blanc, un disque de numéro pair est noir
def hanoi():
    n=int(input("donner le nb de disques"))
    t1=list(range(n+1))
    t2=[1]
    t3=[0]
    mem=0 #pour mémoriser d'où venait le disque qui vient de bouger
    print("t1 : ",t1)
    while len(t3)<=n:
        #si tour non vide et mvt avec couleurs différentes et sur disque sur plus grand et n'annule pas le mvt précédent
        if len(t1) > 1 and (t1[-1]+t2[-1])%2 == 1 and t1[-1] > t2[-1] and mem!=1:
            t2.append(t1.pop())
            print("déplacement de t1 vers t2")
            mem=2
        elif len(t1) > 1 and (t1[-1]+t3[-1])%2 == 1 and t1[-1] > t3[-1] and mem!=1:
            t3.append(t1.pop())
            print("déplacement de t1 vers t3")
            mem=3
        elif len(t2) > 1 and (t2[-1]+t1[-1])%2 == 1 and t2[-1] > t1[-1] and mem!=2:
            t1.append(t2.pop())
            print("déplacement de t2 vers t1")
            mem=1
        elif len(t2) > 1 and (t2[-1]+t3[-1])%2 == 1 and t2[-1] > t3[-1] and mem!=2:
            t3.append(t2.pop())
            print("déplacement de t2 vers t3")
            mem=3
        elif len(t3) > 1 and (t3[-1]+t1[-1])%2 == 1 and t3[-1] > t1[-1] and mem!=3:
            t1.append(t3.pop())
            print("déplacement de t3 vers t1")
            mem=1
        elif len(t3) > 1 and (t3[-1]+t2[-1])%2 == 1 and t3[-1] > t2[-1] and mem!=3:
            t2.append(t3.pop())
            print("déplacement de t3 vers t2")
            mem=2
        print("t1 : ",t1, "t2 : ",t2, "t3 : ",t3)

#hanoi()
        
#3 Trouve par force brute les solutions au probleme des 8 dames, puis 12 solutions
def prise(dames,i,j):
     return abs(dames[j]-dames[i]) == abs(j-i) or (dames[j]==dames[i])

def position_valide(n,dames):
     ok = True
     i=0
     while ok and i<n-1 :
         j = i+1
         while ok and j<=n-1 :
             ok = not prise(dames,i,j)
             j += 1
         i += 1
     return ok

#indique si 2 configurations sont symétriques par symétrie d'axe horizontal
def is_symh(t1,t2):
    ok = True
    i=0
    while ok and i<8:
        ok = t1[i] == t2[7-i] 
        i+=1
    return ok
#indique si 2 configurations sont symétriques par symétrie d'axe vertical
def is_symv(t1,t2):
    ok = True
    i=0
    while ok and i<8:
        ok = t1[i] == 7-t2[i] 
        i+=1
    return ok
#indique si 2 configurations sont symétriques par symétrie d'axe diagonale ascendante
def is_symd1(t1,t2):
    ok = True
    i=0
    while ok and i<8:
        ok = t2[7-t1[i]] == 7-i 
        i+=1
    return ok
#indique si 2 configurations sont symétriques par symétrie d'axe diagonale descendante
def is_symd2(t1,t2):
    ok = True
    i=0
    while ok and i<8:
        ok = t2[t1[i]] == i 
        i+=1
    return ok
#indique si 2 configurations sont symétriques par reflexion droite
def is_symd(t1,t2):
    ok = True
    i=0
    while ok and i<8:
        ok = t2[t1[i]] == 7-i 
        i+=1
    return ok
#indique si 2 configurations sont symétriques par reflexion gauche
def is_symg(t1,t2):
    ok = True
    i=0
    while ok and i<8:
        ok = t2[7-t1[i]] == i 
        i+=1
    return ok
#indique si 2 configurations sont symétriques par symétrie centrale
def is_symc(t1,t2):
    ok = True
    i=0
    while ok and i<8:
        ok = t2[7-i] == 7-t1[i] 
        i+=1
    return ok

def is_sym(t1,t2):
    return is_symh(t1,t2) or is_symv(t1,t2) or is_symd1(t1,t2) or is_symd2(t1,t2) or is_symd(t1,t2) or is_symg(t1,t2) or is_symc(t1,t2) 
 
def dames_12_solutions():
    nb_solutions = 0
    dames_sym = []   #stocke les solutions sans symétrie
    for a in range(8):
       for b in range(8):
           for c in range(8):
                 for d in range(8):
                     for e in range(8):
                         for f in range(8):
                             for g in range(8):
                                 for h in range(8):
                                     dames = [a,b,c,d,e,f,g,h]
                                     if position_valide(8,dames):
                                         ok=True
                                         q=0
                                         #recherche d'une symétrie de cette solution dans dames_sym
                                         while ok and q < len(dames_sym):
                                             if is_sym(dames,dames_sym[q]):
                                                 ok=False
                                             q+=1
                                         if ok:   #si pas trouvée, nouvelle solution sans sym
                                             dames_sym.append(dames)
                                             print(dames)
                                             nb_solutions += 1
    print(nb_solutions,"solutions")
    
#dames_12_solutions()

#version alternative de génération des 92 solutions, proposée par Maxime Véry, merci à lui !
def reines_force():
    #La liste L contiendra l'ensemble des solutions
    L=[]
    #compteur compte le nombre de solutions
    compteur=0
    for i in range(16777216): #8^8
      #p contient la valeur de i en base 8
      p=[]
      #algorithme qui transforme i en base 8
      while i>=8:
         p=[i%8]+p
         i//=8
      p=[i]+p
      while len(p)<=7:
          #complète la liste p avec des 0 à gauche
          p=[0]+p
      #test de la validité de la liste p
      if position_valide(8,p):
          L+=[p]
          compteur+=1
          print(p)
    print(compteur)  

#reines_force()