#-- Sintaxis de while --

# i=1

# while i<=10:
#     print("Ejecución " + str(i))
#     i=i+1

# print("Termino la ejecución")

# #-- Pide la edad comprueba que while es indeterminado --

# edad=int(input("Introduce la edad por favor: "))

# while edad<5 or edad>100:
#     print("has introducido una edad incorrecta. Vuelve a intentarlo")
#     edad=int(input("Introduce la edad por favor: "))
# print("Gracias por colaborar. Puedes pasar")
# print("Edad del aspirante " + str(edad))

#-- Prevee que el codigo no se vuelva infinito --
#-- impoto las funciones matematicas
import math

print("Programa de cálculo de raíz cuadrada")
numero=int(input("Introduce un número por favor: "))

intentos=0

while numero<0:
    print("No se puede hallar la raiz de un número negativo")
    if intentos==2:
        print("Has consumido demasiados intentos. El programa a finalizado")
        break;
    numero=int(input("Introduce un número por favor: "))
    if numero<0:
        intentos=intentos+1

if intentos<2:
    solucion=math.sqrt(numero)
    print("La raíz cuadrada de " + str(numero) + " es " + str(solucion))