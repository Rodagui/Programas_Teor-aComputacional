#Programa 10: cuenta las ocurrencias de cada palabra en una oración dada.

def frecuenciaDePalabras(oracion):

	listaPalabras = oracion.split(' ')

	diccionario = {}

	for i in range(len(listaPalabras)):
		
		if listaPalabras[i] in diccionario:
			diccionario[listaPalabras[i]] += 1
		else:
			diccionario[listaPalabras[i]] = 1


	for i in diccionario:
		print("{}\t\t{}".format(i, diccionario[i]))

	return

#------------------ Main -------------#

print("\nPrograma 10: cuenta las ocurrencias de cada palabra en una oración dada.\n\n")

oracion = input("Ingrese la oracion: ")

frecuenciaDePalabras(oracion)
