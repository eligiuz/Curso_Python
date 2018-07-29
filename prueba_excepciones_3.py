#-- Utilizar para lanzar execepciones propias
#Los tiposdeerror deben ser los definidos

# def evaluaEdad(edad):

#     if edad<0:
#         # raise tipodeerror("mensaje")
#         raise TypeError("No se permiten edades negativas")

#     if edad<20:
#         return "Eres muy joven"
#     elif edad<40:
#         return "Eres joven"
#     elif edad<65:
#         return "Eres maduro"
#     elif edad<100:
#         return "Cuídate"

# print(evaluaEdad(15))

#-- Captura de la excepción propia por medio de raise

import math

def calculaRaiz(num1):
    
    if num1<0:
        raise ValueError("El número no puede ser negativo")
    else:
        return math.sqrt(num1)

op1=(int(input("Introduce un número: ")))

try:
    print(calculaRaiz(op1))

#-- Con as puedo ponerle nomnbre a la excepción
except ValueError as ErrorDeNumeroNegativo:

    print(ErrorDeNumeroNegativo)

print("Programa terminado")