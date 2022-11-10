
def melanger(array, n, i):
	largest = i
	gauche = 2 * i + 1 
	droite = 2 * i + 2 
	if gauche < n and array[i] < array[gauche]:
		largest = gauche

	if droite < n and array[largest] < array[droite]:
		largest = droite

	if largest != i:
		(array[i], array[largest]) = (array[largest], array[i])

		melanger(array, n, largest)

def tri_par_tas(array):
	n = len(array)
	for i in range(n // 2 - 1, -1, -1):
		melanger(array, n, i)
	for i in range(n - 1, 0, -1):
		(array[i], array[0]) = (array[0], array[i]) 
		melanger(array, i, 0)

arbre =  [9, 10, 0, 7, 1, 11, 6, 2, 8, 4, 3, 5]
tri_par_tas(arbre)
print(arbre)