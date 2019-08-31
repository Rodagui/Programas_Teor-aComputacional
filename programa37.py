#Programa 37: Convierte una cadena en una lista. 

def convierteALista(cadena):
	lista = cadena.split()

	print("Lista: ")
	for i in range(len(lista)):
		print('{}.- {}'.format(i+1, lista[i]))

	return

# -------------- Main ------------

print("\nPrograma 37: Convierte una cadena en una lista.\n\n")

cadena = input("Ingrese la cadena: ")

convierteALista(cadena)