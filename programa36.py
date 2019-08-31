#Programa 36: Comprueba si una cadena contiene todas las letras del alfabeto.

def compruebaAlfabeto(cadena):

	can = True
	cadena =  cadena.lower()

	alfabeto = []

	for i in range(26):
		alfabeto.append(0)

	for i in range(len(cadena)):
		pos = ord(cadena[i]) - 97
		alfabeto[pos] += 1

	for i in range(26):
		if(alfabeto[i] == 0):
			can = False
			break

	return can


# ----------- Main ------------

print('\nPrograma 36: Comprueba si una cadena contiene todas las letras del alfabeto.\n\n')
cadena = input("Ingrese la cadena: ")

if(compruebaAlfabeto(cadena)):
	print("SI Contiene todas las letras del alfabeto")
else:
	print("NO contiene todas las letras")