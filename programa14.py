#Programa 14: Obtiene una cadena hecha de los primeros tres caracteres de la misma. Si la longitud es menor que 3, devuelva la cadena original.

def obtenerCadena(cadena):
	tam = len(cadena)
	nva = ""
	
	if(tam < 3):
		nva = cadena
	else:
		nva += cadena[0] + cadena[1] + cadena[2]

	return nva

#--------------- Main ----------------#

print("\nPrograma 14: Obtiene una cadena hecha de los primeros tres caracteres de la misma.\nSi la longitud es menor que 3, devuelva la cadena original.\n\n")

cadena = input("Ingrese la cedena: ")

cadena = obtenerCadena(cadena)

print(cadena)