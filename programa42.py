#Programa 42: Obtiene la última parte de una cadena antes de un carácter especificado.

def dividePalabra(cadena, caracter):

	indices =  []
	indice = 0

	while(indice != -1):
		
		indice = cadena.find(caracter, indice)
		
		if(indice != -1):
			indices.append(indice)
			indice += 1

	tam = len(indices) - 1
	ultimaPos = indices[tam]

	cad2 = ""

	for i in range(ultimaPos + 1 , len(cadena)):
		cad2 += cadena[i]

	print(cad2)

	return

# ------------ Main -----------

print("\nPrograma 42: Obtiene la última parte de una cadena antes de un carácter especificado.\n\n")

cadena = input("Ingrese la cadena: ")
delimitador = input("Ingrese el delimitador: ")

dividePalabra(cadena, delimitador)