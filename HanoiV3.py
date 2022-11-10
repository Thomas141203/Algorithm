
def afficheTour(t1, t2, t3):
    max = 0
    if len(t1) > len(t2) and len(t1) > len(t3):
        max = len(t1)
    elif len(t2) > len(t1) and len(t2) > len(t3):
        max = len(t2)
    elif len(t3) > len(t1) and len(t3) > len(t2):
        max = len(t3)
    for i in range(max):
        pass
        

def Hanoi(n):
    t1 = [0]*(n+1)
    for i in range(n+1):
        t1[i] = i
    t2 = [1]
    t3 = [0]
    mem = 0
    while len(t3) != (n+1):
        #Mouvement t1 --> t2
        if len(t1) != 1 and (t1[-1] % 2 != t2[-1] % 2) and t2[-1] < t1[-1] and mem != 1:
            t2.append(t1[-1])
            mem = 2
            t1.pop()
        #Mouvement t1 --> t3    
        elif len(t1) != 1 and (t1[-1] % 2 != t3[-1] % 2) and t3[-1] < t1[-1] and mem != 1:
            t3.append(t1[-1])
            mem = 3
            t1.pop()
        #Mouvement t2 --> t1
        elif len(t2) != 1 and (t2[-1] % 2 != t1[-1] % 2) and t1[-1] < t2[-1] and mem != 2:
            t1.append(t2[-1])
            mem = 1
            t2.pop()
        #Mouvement t2 --> t3
        elif len(t2) != 1 and (t2[-1] % 2 != t3[-1] % 2) and t3[-1] < t2[-1] and mem != 2:
            t3.append(t2[-1])
            mem = 3
            t2.pop()
        #Mouvement t3 --> t1
        elif len(t3) != 1 and (t3[-1] % 2 != t1[-1] % 2) and t1[-1] < t3[-1] and mem != 3:
            t1.append(t3[-1])
            mem = 1
            t3.pop()
        #Mouvement t3 --> t2
        elif len(t3) != 1 and (t3[-1] % 2 != t2[-1] % 2) and t2[-1] <t3[-1] and  mem != 3:
            t2.append(t3[-1])
            mem = 2
            t3.pop()
        print(t1, t2, t3)
        
        
Hanoi(3)

t1 = [0]*(3+1)
for i in range(3+1):
    t1[i] = i
t2 = [1]
t3 = [0]

afficheTour(t1, t2, t3)
