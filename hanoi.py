
def hanoi(n, depart, inter, arrivee):
	if 0 < n :
		hanoi(n-1, depart, arrivee, inter)
		print(str(n) + " va de " + str(depart) + " vers " + str(arrivee))
		hanoi(n-1, inter, depart, arrivee)

hanoi(3, "dep", "inter", "arr")