#Programa 34: Cuenta los caracteres repetidos en una cadena. 

def freqCaracteres(cadena):

	simbolos = []

	for i in range(256):
		simbolos.append(0);


	for i in range(len(cadena)):
		pos = ord(cadena[i])
		simbolos[pos] += 1

	for i in range(256):
		if(simbolos[i] > 1):
			var = chr(i)
			print('{} {}'.format(var, simbolos[i]))

	return


# -------------- Main ----------- #

print("\nPrograma 34: Cuenta los caracteres repetidos en una cadena.\n\n")

cadena = input("Ingrese la cadena: ")

freqCaracteres(cadena)