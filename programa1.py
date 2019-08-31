#Programa 1: Calcula la longitud de una cadena

def obtenerLongitud(cadena):
	
	longitud = len(cadena)
	
	return longitud

#------------------ Main ------------------#
print("\nPrograma 1: Calcula la longitud de una cadena\n\n")

cadena = input('Ingrese la cadena:  ')

#cuenta la longitus de una cadena
print('Longitud: {}'.format(obtenerLongitud(cadena)))