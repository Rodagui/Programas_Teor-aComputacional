#Programa 35: Imprime el índice del carácter en una cadena.

def imprimirIndice(cadena):

	for i in range(len(cadena)):
		print('Carácter actual {}, posicion {}'.format(cadena[i], i))

	return

#------------ Main -----------

print("\nPrograma 35: Imprime el índice del carácter en una cadena.\n\n")

cadena = input("Ingrese la cadena: ")

imprimirIndice(cadena)