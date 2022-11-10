def tri_shaker(L):
    permutation = True
    sens = 1
    en_cours = 0
    debut = 0
    fin = len(L)-2
    while permutation == True:
        permutation = False
        while (en_cours < fin and sens == 1) or (en_cours > debut and sens == -1) :
            if L[en_cours] > L[en_cours + 1]:
                permutation = True
                L[en_cours], L[en_cours + 1] = L[en_cours + 1],L[en_cours]
            en_cours = en_cours + sens
        if sens == 1:
            fin -=1
        else:
            debut += 1
        sens = -sens
    return L

L = [9,6,1,5,3,3,10,4,8,2]
print(tri_shaker(L))