#Programa 3: Obtiene una cadena hecha de los dos primeros y los dos útlimos caracteres de una cadena dada. 
#			  Regresa la cadena vacía si la longitud de la cadena original es menor que dos.

def obtenerPalabra(cadena):
	
	nva = ""
	tam =  len(cadena)
	if( tam >= 2):
		for i in range(2):
			nva += cadena[i]

		nva += cadena[tam - 2] + cadena[tam - 1]

	return nva


#------------------ Main ------------------#

print("\nPrograma 3: Obtiene una cadena hecha de los dos primeros y los dos útlimos caracteres de una cadena dada. \nRegresa la cadena vacía si la longitud de la cadena original es menor que dos.\n\n")

cadena = input('Ingrese la cadena:  ')

cadena = obtenerPalabra(cadena)

print(cadena)