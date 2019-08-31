#Programa 38: Pone en minúsculas los primeros n caracteres de una cadena.

def ponerEnMinus(cadena, caracteres):

	copia = cadena.lower()
	tam = len(cadena)

	nva = ""
	cont = 0
	for i in range(tam):

		if(cont < caracteres and copia[i].isalpha()):
			nva += copia[i]
			cont += 1
		else:
			nva += cadena[i]

	return nva

# ------------- Main ------------

print("\nPrograma 38: Pone en minúsculas los primeros n caracteres de una cadena.\n\n")

cadena = input("Ingrese cadena: ")

caracteres = int(input("Numero de caracteres: "))


cadena = ponerEnMinus(cadena, caracteres)

print(cadena)