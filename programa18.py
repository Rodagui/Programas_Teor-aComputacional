#Programa 18: Ordena una cadena lexicográficamente.

def ordenaPalabra(cadena):
	
	nva = ""
	lista = sorted(cadena)

	for i in range(len(lista)):
		nva += lista[i]

	return nva

#------------------ Main ------------------#

print("\nPrograma 18: Ordena una cadena lexicográficamente.\n\n")

cadena = input("Ingrese la cadena: ")

cadena = ordenaPalabra(cadena)

print(cadena)