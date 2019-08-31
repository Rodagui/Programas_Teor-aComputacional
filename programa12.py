#Programa 12: Acepta una secuencia de palabras separada por comas e imprimae las palabras en forma ordenada (alfanuméricamente).

def ordena(cadena):

	listaPalabras = cadena.split(',')

	listaPalabras.sort()

	for i in range(len(listaPalabras)):
		print(listaPalabras[i])

	return

#------------------ Main ------------------#

print("\nPrograma 12: Acepta una secuencia de palabras separada por comas e imprimae las palabras en forma ordenada (alfanuméricamente).\n\n")	

cadena = input("Ingrese la cadena separada por comas: ")

ordena(cadena)