#Programa 41: Divide una cadena en la última aparición del delimitador dado.

def dividePalabra(cadena, caracter):

	indices =  []
	indice = 0

	while(indice != -1):
		
		indice = cadena.find(caracter, indice)
		
		if(indice != -1):
			indices.append(indice)
			indice += 1

	#for i in range(len(indices)):
		#print(indices[i])
	tam = len(indices) - 1
	ultimaPos = indices[tam]

	cad1 = ""
	cad2 = ""

	for i in range(ultimaPos):
		cad1 += cadena[i]

	for i in range(ultimaPos, len(cadena)):
		cad2 += cadena[i]

	print(cad1)
	print(cad2)

	return

#---------- Main ----------

print("\nPrograma 41: Divide una cadena en la última aparición del delimitador dado.\n\n")

cadena = input("Ingrese cadena: ")

caracter = input("Ingrese caracter delimitador: ")

dividePalabra(cadena, caracter)

