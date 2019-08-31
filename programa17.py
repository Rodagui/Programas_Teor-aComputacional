#Programa 17: Convierte una cadena dada en mayúsculas si contiene al menos 2 caracteres en mayúsculas en los primeros 4 caracteres.

def convierteMayus(cadena):
	nva =  ""
	cont = 0

	for i in range(4):
		cod = ord(cadena[i])

		if(cod  > 64 and cod < 91):
			cont += 1

	if(cont > 1):
		nva = cadena.upper()
	else:
		nva = cadena

	return nva


#------------------ Main ------------------#

print("\nPrograma 17: Convierte una cadena dada en mayúsculas si contiene al menos 2 caracteres en mayúsculas\nen los primeros 4 caracteres.\n\n")

cadena = input("Ingrese la cadena: ")

cadena = convierteMayus(cadena)

print(cadena)