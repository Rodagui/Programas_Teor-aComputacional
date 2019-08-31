#Programa 27: Muestra número con comas como separadores.

def agregaComas(numero):

	nva = ""
	tam = len(numero)
	cont = 0
	for i in range(tam - 1, -1, -1): #for desde i a 0, el tercer parametro decrementa
		cont += 1

		if(cont == 4):
			cont = 1
			nva +=','

		nva += numero[i]

	nva = nva[::-1] #Hace reverse a la cadena "nva"

	return nva


# ------------- Main -------------#

print("\nPrograma 27: Muestra número con comas como separadores.\n\n")

numero = input("Ingrese el número: ")

print(agregaComas(numero))