#Programa 40: Cuenta las vocales de un texto dado. 

def cuentaVocales(cadena):

	cadena.lower()

	vocales = []

	for i in range(5):
		vocales.append(0)

	for i in range(len(cadena)):
		
		if(cadena[i] == 'a'):
			vocales[0] += 1
		elif(cadena[i] == 'e'):
			vocales[1] += 1
		elif(cadena[i] == 'i'):
			vocales[2] += 1
		elif(cadena[i] == 'o'):
			vocales[3] += 1
		elif(cadena[i] == 'u'):
			vocales[4] += 1

	print("a {}".format(vocales[0]))
	print("e {}".format(vocales[1]))
	print("i {}".format(vocales[2]))
	print("o {}".format(vocales[3]))
	print("u {}".format(vocales[4]))

	return

#------------- Main -----------

print("\nPrograma 40: Cuenta las vocales de un texto dado.\n\n")
cadena = input("Ingrese la cadena: ")

cuentaVocales(cadena)