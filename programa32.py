#Programa 32: Invierte palabras en una cadena.

def inviertePalabras(cadena):
	oracion = ""

	palabras = cadena.split()

	for i in range(len(palabras)):
		palabras[i] = palabras[i][::-1]
		oracion += palabras[i]
		oracion += ' '

	return oracion

# ----------------- Main ---------------

print('\nPrograma 32: Invierte palabras en una cadena.\n\n')

cadena = input("Ingrese cadena: ")

cadena = inviertePalabras(cadena)

print(cadena)