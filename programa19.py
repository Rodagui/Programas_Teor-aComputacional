#Programa 19: Comprueba si una cadena comienza con caracteres especificados.

def compruebaCaracteres(cadena, caracteres):

	cadena = cadena.lower()
	caracteres = caracteres.lower()
	
	siEmpieza = True

	if( len(cadena) < len(caracteres) ):
		return False

	for i in range(len(caracteres)):
		if(caracteres[i] != cadena[i]):
			return False

	return True

#------------------ Main ------------------#

print("\nPrograma 19: Comprueba si una cadena comienza con caracteres especificados.\n\n")

cadena = input("Ingrese la cadena: ")
caracteres = input("Ingrese los caracteres: ")

siEmpieza = compruebaCaracteres(cadena, caracteres)

if(siEmpieza):
	print("Si empieza con esos caracteres")
else:
	print("No empieza")