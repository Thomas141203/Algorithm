def suivant(ligne):
    suivante = []
    chiffre_actuel = ligne[0]
    compteur = 0
    for chiffre in ligne:
        if chiffre == chiffre_actuel:
            compteur += 1
        else:
            suivante.append(str(compteur))
            suivante.append(chiffre_actuel)
            chiffre_actuel = chiffre
            compteur = 1
    suivante.append(str(compteur))
    suivante.append(chiffre_actuel)
    return "".join(suivante)
 
 
def conway(n):
    ligne = ["1"]
    for i in range(n):
        ligne = suivant(ligne)
    return ligne


print(conway(5))