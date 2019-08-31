#Programa 20: Crea un cifrado de Cesar.

def cifrado(cadena, desplazamiento):

	cadena = cadena.lower()
	nva = ""

	for i in range(len(cadena)):
		if(cadena[i] == ' '):
			nva += ' '
		else:
			pos = ord(cadena[i])

			pos = pos + desplazamiento
			
			if(pos > 122):
				pos = pos - 26

			nva += chr(pos)

	return nva


#------------------ Main ------------------#

print("\nPrograma 20: Crea un cifrado de Cesar.\n\n")

cadena = input("Ingrese la cadena: ")
desplazamiento = int(input("Numero de desplazamientos para el cifrado: "))

cadena = cifrado(cadena, desplazamiento)

print(cadena)
