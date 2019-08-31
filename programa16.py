#Programa 16: Invierte una cadena si su longitud es un múltiplo de la suma de los tres últimos dígitos de su No. de Boleta.

def invertirCadena(cadena, numBoleta):
	
	nva = ""

	suma = numBoleta % 10
	numBoleta = numBoleta // 10

	suma += numBoleta % 10
	numBoleta = numBoleta // 10

	suma += numBoleta % 10

	tam = len(cadena)

	print("\nSuma = {}".format(suma))
	print("Longitud de la cadena = {}".format(len(cadena)))

	if(tam % suma == 0):
		print("\nSí es multiplo de la suma\n\nCadena invertida.")
		nva = cadena[::-1]
	else:
		print("\nNo es multiplo")
		nva = cadena

	return nva

#-------------- Main ----------------

print("\nPrograma 16: Invierte una cadena si su longitud es un múltiplo de la suma de los tres últimos dígitos de su No. de Boleta.\n\n")


cadena = input("Ingrese su cadena: ")
numBoleta = int(input("Ingrese su numero de boleta: "))

cadena = invertirCadena(cadena, numBoleta)

print(cadena)