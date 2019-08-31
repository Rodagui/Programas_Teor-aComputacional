#Porgrama 21: Agrega un prefijo a todas las líneas de una cadena multilínea.

#------------------ Main ------------------#

print("\nPorgrama 21: Agrega un prefijo a todas las líneas de una cadena multilínea.\n\n")

prefijo = input("Ingrese el prefijo: ")
lineas = int(input("Ingrese la cantidad de lineas: "))

lista = []

for i in range(lineas):
	lista.append(input('linea: '))
	lista[i] = prefijo + lista[i]

for i in range(lineas):
	print(lista[i])
