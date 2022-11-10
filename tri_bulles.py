def tri_bulles(L):
    n = len(L)
    trie = False
    while not trie:
        trie = True
        for i in range(n-1):
            if L[i] > L[i+1]:
                L[i],L[i+1] = L[i+1],L[i]
                trie = False
        n-=1
    return L
        
L = [9,6,1,5,3,3,10,4,8,2]
print(tri_bulles(L))