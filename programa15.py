#Programa 15: Obtiene la primera mitad de una cadena especificada de longitud par.

def obtenerMitad(cadena):
	tam = len(cadena) // 2

	nva = ""
	
	for i in range(tam):
		nva += cadena[i]

	return nva

#------------------ Main ------------------#

print("\nPrograma 15: Obtiene la primera mitad de una cadena especificada de longitud par.\n\n")

cadena = input("Ingrese la cedena: ")

cadena = obtenerMitad(cadena)

print(cadena)
