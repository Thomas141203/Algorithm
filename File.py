from Pile import*

class File:
    def __init__(self):
        self.file = [Pile(), Pile()]
    
    #def creer_file(self):
        #return [creer_pile(), creer_pile()]
    def taille(self):
        return len(self.file)
    
    def file_vide(self, f):
        return pile_vide(f[0]) and pile_vide(f[1])
    
    def enfiler(self, f, c):
        self.file[1].empiler(c)
        #empiler(f[1], c)
        
    def defiler(self, f):
        if pile_vide(f[0]):
            while not pile_vide(f[1]):
                empiler(f[0],depiler(f[1]))
        return depiler(f[0])

    def __str__(self):
        N = self.taille()
        chaîne = "("
        i = 0
        while i < N:
           chaîne += str(self.file[i])
           if i < N - 1:
               chaîne += " ← "
           i += 1
        chaîne += ")"
        return chaîne
    
    
f = File()
f.enfiler(f, 4)
f.enfiler(f, 5)
f.enfiler(f, 6)
f.enfiler(f, 7)
f.enfiler(f, 8)
f.enfiler(f, 9)
print(f)