#Programa 33: Quita un conjunto de caracteres de una cadena.

def eliminarCaracteres(cadena, caracteres):

	nva = ""
	diccionario = {}

	for i in range(len(caracteres)):
		diccionario[caracteres[i]] = 1

	for i in range(len(cadena)):
		if not cadena[i] in diccionario:
			nva += cadena[i]

	return nva

# -------------- Main -------------- #

print("\nPrograma 33: Quita un conjunto de caracteres de una cadena.\n\n")
cadena = input("Ingrese la cadena: ")
caracteres = input("Ingrese los caracteres a eliminar: ")

cadena = eliminarCaracteres(cadena, caracteres)

print(cadena)