#Programa 39: Intercambia coma y punto en una cadena. 
def reemplazar(cadena):

	nva = ""
	for i in range(len(cadena)):
		if(cadena[i] == ','):
			nva += '.'
		elif(cadena[i] == '.'):
			nva += ','
		else:
			nva += cadena[i]

	return nva

# -------------- Main ------------

print("\nPrograma 39: Intercambia coma y punto en una cadena.\n\n")
cadena = input("Ingrese la cadena: ")

cadena = reemplazar(cadena)

print(cadena)