#Programa13: copia 4 veces los ultimos dos caracteres de una cadena

def copiaCuatroVeces(cadena):
	nva = ""
	pos = len(cadena) - 1

	for i in range(4):
		nva += cadena[pos - 1 ] + cadena[pos]

	return nva

# ----------- main --------------------

print("\nPrograma13: Crea una cadena nueva con 4 veces los últimos dos caracteres de la cadena\n\n")

cadena = input("Ingrese la cedena: ")

cadena = copiaCuatroVeces(cadena)

print(cadena)
