# Programa 29: Muestra un número en alineación izquierda, derecha y central alineados en ancho 10. 

def alinearNumero(numero):

	tam = len(numero)


	#--------- Imprimmir a la izquierda
	print("\nIzq :{}".format(numero))

	for i in range(10 - tam):
		print(' ', end="")

	# ------------- Imprimir a la derecha
	print("\nDer :", end="")
	for i in range(10 - tam):
		print(' ', end="")
	print(numero)

	#--------------  Imprimir al centro

	espacios = (10 - tam) // 2  # // es para division entera

	print("\nCen :", end="")
	for i in range(espacios):
		print(' ', end="")

	print(numero, end="")

	for i in range(espacios):
		print(' ', end="")

	return

# --------------- Main ------------ #

print("\nPrograma 29: Muestra un número en alineación izquierda, derecha y central alineados en ancho 10.\n\n")
numero = input("Ingrese el número: ")

alinearNumero(numero)
