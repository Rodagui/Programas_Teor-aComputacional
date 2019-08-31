#Programa 8: Intercambia el primer y el ultimo caracter de una cadena

def intercambia(cadena):
	pos = len(cadena) - 1
	
	nva = cadena[pos]

	for i in range(1, pos):
		nva += cadena[i]

	nva += cadena[0]

	return  nva


#------------------ Main ------------------#

print("\nPrograma 8: Intercambia el primer y el ultimo caracter de una cadena\n\n")

cadena = input('Ingrese la cadena:  ')

cadena = intercambia(cadena)

print(cadena)