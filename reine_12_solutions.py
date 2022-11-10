def reine(n, i, a, b, c):
    if i < n:
        for j in range(n):
            if j not in a and i+j not in b and i-j not in c:
                yield from reine(n, i+1, a+[j], b+[i+j], c+[i-j])
    else:
        yield a

for solution in reine(8, 0, [], [], []):
    print(solution)
    
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
                                    dames = [a, b, c, d, e, f, g, h]
                                    if position_valide(8, dames):
                                        ok = True
                                        q = 0
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