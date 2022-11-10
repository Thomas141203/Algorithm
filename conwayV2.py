def Conway2(texte):
        p = 0
        ligne = ""
        while p < len(texte):
            var = texte[p]
            d = 1
            p+=1
            while p < len(texte) and texte[p] == var:
                d+=1
                p+=1
            ligne += str(d) + var
        return ligne
    
def Conway(texte):
        liste = list('1')
        for i in range(texte):
            suiv = []
            ca = liste[0]
            cpt = 0
            for c in texte:
                if c == ca:
                    cpt+=1
                else:
                    suiv.append(str(cpt))
                    suiv.append(ca)
                    ca = c
                    cpt = 1
            suiv.append(str(cpt))
            suiv.append(ca)
        liste.append("".join(suiv))
        return liste

print(Conway2("1211"))
print(Conway(5))