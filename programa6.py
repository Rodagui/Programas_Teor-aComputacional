#Programa 6: Toma una lista de palabras y devuelve la longitud de la palabra más larga

def palabraMasLarga(lista):
	mayorLen = 0

	for i in range(len(lista)):
		longActual = len(lista[i])
		if(longActual > mayorLen):
			mayorLen = longActual

	
	return mayorLen

#------------------ Main ------------------#

print("\nPrograma 6: Toma una lista de palabras y devuelve la longitud de la palabra más larga\n\n")

lista = []

numPal = int(input("Numero de palabras: "))

for i in range(numPal):
	lista.append(input('Palabra: '))


print("La palabra mas larga tiene una longitud de: {}".format(palabraMasLarga(lista)))