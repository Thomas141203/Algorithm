from Pile import*

def casesVoisines(lab, i, j):
    #X1
    if i == 0 and j == 0:
        return [(i+1, j), (i, j+1)]
    #X2
    elif i == 0 and j != 0 and j < len(lab):
        return [(i, j-1), (i+1, j), (i, j+1)]
    #X3
    elif i == 0 and j == len(lab):
        return [(i-1, j), (i, j+1)]
    #X4
    elif j == 0 and i !=0 and i < len(lab):
        return [(i, j-1), (i+1, j), (i, j+1)]
    #X5
    elif i != 0 and j != 0 and i < len(lab) and j < len(lab):
        return [(i, j-1), (i-1, j), (i+1, j), (i, j+1)]
    #X6
    elif j == len(lab) and i !=0 and i < len(lab):
        return [(i, j-1), (i+1, j), (i, j+1)]
    #X7
    elif j == 0 and i == len(lab):
        return [(i-1, j), (i, j+1)]
    #X8
    elif i == len(lab) and j != 0 and j < len(lab):
        return [(i, j-1), (i+1, j), (i, j+1)]
    #X9
    elif i == len(lab) and j == len(lab):
        return [(i, j-1), (i-1, j)]
    else:
        return "What the hell is that !"


def parcoursLabyrinthe(L):
    pile = Pile()
    depart = (0, 0)
    ok = pile.pile_vide()
    for i in range(len(L)):
        for j in range(len(L[0])):
            if i == 0 and L[i][j] == 1:
                depart = (0, j)
            elif j == 0 and L[i][j] == 1:
                depart = (i, 0)
            elif i == len(L) and L[i][j] == 1:
                depart(len(L), j)
            elif j == len(L) and L[i][j] == 1:
                depart(i, len(L[i]))
            pile.empiler(depart)
    while ok:
        var = pile.depiler()
        let = casesVoisines(L, var[0], var[1])
        print(let)
        for elt in let:
            i, j = elt
            if L[i][j] == 1:
                nextCase = (i, j)
        if estUnBord(L, nextCase):
            print("youpi")
            ok = False
        else:
            pile.empiler(nextCase)
    
def estUnBord(l, case):
    if case[0] == 0 or case[1] == 0 or case[0] == len(l) or case[1] == len(l):
        return True
    else:
        return False
    
L = [[0, 1, 0, 0 ,0 ,0], [0, 1, 1, 1, 1, 0], [0, 1, 0, 1, 0, 0], [0, 1, 0, 1 ,1 ,0], [0, 1, 1, 0, 1, 0], [0, 0, 0, 0, 1, 0]]
print(casesVoisines(L, 1, 1))
parcoursLabyrinthe(L)