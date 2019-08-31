#Programa 30: Coloca tres números en el rango (0,256) en una cadena hexadecimal que inicie con '#' (Formato RGB de Python TkInter).
def letra(num):

	if(num < 10):
		return str(num)

	if(num == 10):
		return 'a'
	
	if(num == 11):
		return 'b'

	if(num == 12):
		return 'c'

	if(num == 13):
		return 'd'

	if(num == 14):
		return 'e'

	if(num == 14):
		return 'f'

def pasaHexadecimal(numero):

	aux = ""
	cadena = ""

	while(numero > 0):
		res = numero % 16

		aux = letra(res)

		cadena += aux

		numero = numero // 16

	cadena = cadena[::-1]

	return cadena

# ------------- Main -----------------#

print("\nPrograma 30: Coloca tres números en el rango (0,256) en una cadena hexadecimal que inicie con '#'\n\n")
num1 = int(input("Num 1: "))
num2 = int(input("Num 2: "))
num3 = int(input("Num 3: "))

hexa1 = pasaHexadecimal(num1)
hexa2 = pasaHexadecimal(num2)
hexa3 = pasaHexadecimal(num3)

print("({}, {}, {}) -> #{}{}{}".format(num1, num2, num3, hexa1, hexa2, hexa3))