# for i in ["primavera","verano","otoño","invierno"]:
#     print(i)

#-- imprime en una linea con un espacio por pase de for

# for i in ["Pildoras", "Informativas", 3]:
#     print("Hola",end=" ")

#-- Revisa si se encuentra la @ en el email --
# contador=0

# miEmail=input("Introduce tu dirección de email: ")

# for i in miEmail:
#     if (i=="@" or i=="."):
#         contador=contador+1

# if contador==2:
#     print("email es correcto")
# else:
#     print("el email no es correcto")

#-- Range --

# for i in range(5):
#     # f nos sirve para concatenar un string y un número
#     print(f"Valor de la varianle {i}")

# #-- Cuenta a partir del 5 y hasta el 9 ---
# for i in range(5,9):
#     # f nos sirve para concatenar un string y un número
#     print(f"Valor de la varianle {i}")

# #-- Cuenta a partir del 5 hasta el 50 y va brincando de 3 en 3 ---
# for i in range(5,50,3):
#     # f nos sirve para concatenar un string y un número
#     print(f"Valor de la varianle {i}")

#-- Función len() ---
valido=False

email=input("Introduce tu email: ")

for i in range(len(email)):
    if email[i]=="@":
        valido=True

if valido:
    print("Email correcto")
else:
    print("Email incorrecto")
