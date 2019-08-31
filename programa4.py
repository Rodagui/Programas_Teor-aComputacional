#Programa 4: Cambia los caracteres igual al primero al caracter '$', excepto el primero

def cambiarCaracteres(cadena):
	nva = ""
	caracter = cadena[0]
	nva += caracter

	for i in range(1, len(cadena)):
		if(cadena[i] == caracter and i > 0):
			nva += "$"
		else:
			nva += cadena[i]
	return nva


#------------------ Main ------------------#

print("\nPrograma 4: Cambia los caracteres igual al primero al caracter '$', excepto el primero\n\n")

cadena = input('Ingrese la cadena:  ')

cadena = cambiarCaracteres(cadena)

print(cadena)