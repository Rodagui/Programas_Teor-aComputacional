# Programa 43: Imprime todas las subcadenas de una cadena
#Identifica prefijos, prefijos propios, sufijos y sufijos propios
#Imprime el número total de subcadenas.


def obtenerSubcadenas(cadena):

	diccionario = {}


	ini = 0
	fin = len(cadena) - 1

	tam = len(cadena)

	

	for i in range(len(cadena)):
		j = i
		nva = ""
		nva += cadena[i]

		if not nva in diccionario: #si la cadena nueva no esta en el diccionario se agrega
			diccionario[nva] = [i, j]
		
		for j in range(i + 1, len(cadena)):
			
			nva += cadena[j]
			
			if not nva in diccionario: 
				diccionario[nva] = [i, j]
			else:
				diccionario[nva][1] = j
	
	ultimaLetra = cadena[fin]
	diccionario[ultimaLetra] = [fin, fin]

	print("Número de subcadenas = {}\n\n".format(len(diccionario)))

	for i in diccionario:
		print(i, end="") #Imprime la llave
		#print(diccionario[i][0])  # imprime el valor de la llave
		#print(diccionario[i][1])  # imprime el valor de la llave

		if(diccionario[i][0] == ini):
			print("\t\tPrefijo", end="")
			
			if(len(i) < tam ):
				print(" propio")

		if(diccionario[i][1] == fin):
			print("\t\tSufijo", end="")
			if(len(i) < tam ):
				print(" propio")

		print('\n')


	return	

#----------------- Main ------------------#

print("\nPrograma 43: Imprime todas las subcadenas de una cadena")
print("Identifica prefijos, prefijos propios, sufijos y sufijos propios")
print("Imprime el número total de subcadenas.\n\n")

cadena = input("Ingrese la cadena: ")

print(cadena)

print("\nsubcadenas:")

obtenerSubcadenas(cadena)
