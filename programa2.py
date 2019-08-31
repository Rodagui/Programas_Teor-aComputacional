#Programa 2: Cuenta la frecuencia de los caracteres en una cadena.
def freqCaracteres(cadena):
	
	simbolos = []

	for i in range(256):
		simbolos.append(0);

	for i in range(len(cadena)):

		pos = ord(cadena[i]) 	#ord(var) pasa el simbolo a su codigo ascii
		simbolos[pos] += 1

	print('simbolo  frecuencia')
	for i in range(256):
		if(simbolos[i] > 0):
			var = chr(i)		#chr(23) pasa el valor ascii al simbolo
			print('  {}         {}'.format(var, simbolos[i]))

	return 


#------------------ Main ------------------#

print("\nPrograma 2: Cuenta la frecuencia de los caracteres en una cadena.\n\n")

cadena = input('Ingrese la cadena:  ')

#cuenta la frecuencia de los caracteres en una cadena
freqCaracteres(cadena)