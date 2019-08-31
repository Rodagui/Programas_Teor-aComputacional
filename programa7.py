#Programa 7: Quita el caracter de una posicion de una cadena dada

def quitarCaracter(cadena, indice):

	nva = ""

	for i in range(indice):
		nva += cadena[i]

	for i in range(indice + 1, len(cadena)):
		nva += cadena[i]

	return nva

#------------------ Main ------------------#

print("\nPrograma 7: Quita el caracter de una posicion dada de una cadena.\n\n")

cadena = input('Ingrese la cadena:  ')

indice = int(input("Ingrese la posicion (0...n): "))

cadena = quitarCaracter(cadena, indice)

print(cadena)