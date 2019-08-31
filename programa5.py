#Programa 5: Obtiene una cadena de dos que se dan  intercambiando sus do sprimeros caracteres

def obtenerUnaPalabra(cadena1, cadena2):
	nva = ""
	nva += cadena2[0] + cadena2[1]

	for i in range(2, len(cadena1)):
		nva += cadena1[i]

	nva += ' ' + cadena1[0] + cadena1[1]

	for i in range(2, len(cadena2)):
		nva += cadena2[i]

	return nva

#------------------ Main ------------------#

print("\nPrograma 5: Obtiene una cadena de dos cadenas que se dan, intercambiando sus dos primeros caracteres\n\n")

cadena1 = input('Ingrese la primer cadena:  ')
cadena2 = input('Ingrese la segunda cadena:  ')


print(obtenerUnaPalabra(cadena1, cadena2))