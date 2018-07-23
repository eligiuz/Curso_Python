#-- Utilizados con for y while
#-- continue: Salta las instrucciones que se encuentren bajo y va ala siguiente vuelta del bucle


#-- Sintaxis
# for letra in "Python":

#     if letra=="h":
#         continue

#     print("Viendo la letra: " + letra)

# #-- Uso de continue busca las letras de un texto --
# nombre="Pildoras Informaticas"

# contador=0

# for i in nombre:
#     if i==" ":
#         continue
#     contador+=1

# print(contador)

#-- pass: sale del bucle y devuelve null

# while True:
#     pass

#-- else: 

email=input("Introduce tu email por favor: ")

for i in email:
    
    if i=="@":
        arroba=True

        break;
else:
    arroba=False

print(arroba)
