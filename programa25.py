#Programa 25: Imprime enteros con ceros a la izquierda hasta un ancho especificado.
def imprimeCeros(numero, ceros):

	for i in range(ceros):
		cero = 0
		print(cero, end="")

	print(numero)

	return


#------------------ Main -------------#

print('\nPrograma 25: Imprime enteros con ceros a la izquierda hasta un ancho especificado.\n\n')

numero = input("Ingrese numero: ")
ceros = int(input("Numero de ceros a la izquierda: "))

imprimeCeros(numero, ceros)


