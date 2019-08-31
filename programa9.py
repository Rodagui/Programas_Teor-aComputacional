#Programa 9: Elimina los caracteres que tienen valores de indice impar de una cadena.

def eliminarImpares(cadena):
	nva = ""

	for i in range(1, len(cadena), 2):
		nva += cadena[i]

	return nva
#------------------ Main ------------------#

print("\nPrograma 9: Elimina los caracteres que tienen valores de indice impar de una cadena.\n\n")

cadena = input('Ingrese la cadena:  ')

cadena = eliminarImpares(cadena)

print(cadena)