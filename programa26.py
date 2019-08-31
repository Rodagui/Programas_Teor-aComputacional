#Programa 26: Programa 26: Imprime los siguientes numeros enteros con "*" a la derecha, del ancho especificado
def imprimeAsteriscos(numero, asteriscos):

	print(numero, end="")

	for i in range(asteriscos):
		cero = '*'
		print(cero, end="")

	return


#------------------ Main -------------#

print('\nPrograma 26: Imprime los siguientes numeros enteros con "*" a la derecha, del ancho especificado.\n\n')

numero = int(input("Ingrese numero: "))
asteriscos = int(input("Numero de *'s a la derecha: "))

imprimeAsteriscos(numero, asteriscos)


