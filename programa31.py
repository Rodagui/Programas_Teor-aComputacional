#Programa 31: Cuenta las ocurrencias de una subcadena en una cadena. 

def cuentaSubcadenas(cadena, subcadena):
	
	veces = 0
	indice = 0

	while(indice != -1):
		
		indice = cadena.find(subcadena, indice)
		
		if(indice != -1):
			veces += 1
			indice += 1


	return veces

# -------------- Main ----------------#

print("\nPrograma 31: Cuenta las ocurrencias de una subcadena en una cadena. \n\n")

cadena = input("Ingrese la cadena: ")
subcadena = input("Ingrese la subcadena: ")

veces = cuentaSubcadenas(cadena, subcadena)

print("\nLa subcadena '{}' aparece {} veces en la cadena".format(subcadena, veces))