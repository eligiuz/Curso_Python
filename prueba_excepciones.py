# -*- coding: latin_1 -*-

def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2
	
#-- Realizar una excepci�n
def divide(num1,num2):	

# Coloco try
	try:	
		return num1/num2

# Coloco el except	
	except ZeroDivisionError:
		print("No se puede dividir entre 0")
		return "Operaci�n err�nea"

# Si quiero resolver el problema de tener que poner solo numeros
while True:
	
	try:
		op1=(int(input("Introduce el primer n�mero: ")))

		op2=(int(input("Introduce el segundo n�mero: ")))

		break

	except ValueError:
		print("Los valores introducidos no son correctos. Intentalo de nuevo")

operacion=input("Introduce la operaci�n a realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
	print(suma(op1,op2))

elif operacion=="resta":
	print(resta(op1,op2))

elif operacion=="multiplica":
	print(multiplica(op1,op2))

elif operacion=="divide":
	print(divide(op1,op2))

else:
	print ("Operaci�n no contemplada")


print("Operaci�n ejecutada. Continuaci�n de ejec�ci�n del programa ")