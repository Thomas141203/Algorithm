class Pile:
    def __init__(self):
        self.pile = []
    
    #def creer_pile(self):
        #return []
    
    def pile_vide(self):
        return self.pile == []
    
    def sommet(self):
        return self.pile[-1]
    
    def empiler(self, x):
        self.pile.append(x)
        
    def depiler(self):
        return self.pile.pop()
    
    def __str__(self):
        ch = ''
        for x in self.pile:
            ch = "|\t" + str(x) + "\t|" + "\n" + ch
        ch = "\nEtat de la pile:\n" + ch
        return ch
    
    
p = Pile()
p.empiler(4)
p.empiler(5)
p.empiler(6)
    