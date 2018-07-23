# edad=-7

# if 0<edad<100:
#     print("Edad es correcta")
# else:
#     print("Edad incorrecta")
#-------------------------------------------

# salario_presidente=int(input("Introduce salario presidente "))
## concatenación de texto y numero convertido a string
# print("Salario presidente: " + str(salario_presidente))

# salario_director=int(input("Introduce salario director "))
## concatenación de texto y numero convertido a string
# print("Salario director: " + str(salario_director))

# salario_jefe_area=int(input("Introduce salario Jefe de Área "))
## concatenación de texto y numero convertido a string
# print("Salario Jefe de Área: " + str(salario_jefe_area))

# salario_administrativo=int(input("Introduce salario administrativo "))
## concatenación de texto y numero convertido a string
# print("Salario administrativo: " + str(salario_administrativo))

# if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
#     print("Todo funciona correctamente")
# else:
#     print('Algo falla en la empresa')
#---------------------------------------------------
##--- PROGRAMA DE BECAS ---##

# print("Programa de becas 2017")
# distancia_escuela=int(input("Introduce la distancia a la escuela en Km "))
# print(distancia_escuela)

# numero_hermanos=int(input("Introduce el número de hermanos en el centro "))
# print(numero_hermanos)

# salario_familiar=int(input("Introduce salario anual bruto "))

# if distancia_escuela>40 and numero_hermanos>2 or salario_familiar<=20000:
#     print("Tiene derecho a beca")
# else:
#     print("No tiene derecho a beca")

##------------------------------------------------

#Uso del operador in

print("Asiganturas optativas año 2017")
print("Asignaturas optativasInformática gráfica - Pruebas de software - Usabilidad y accesibilidad")
opcion=input("Escribe la asignatura escogida: ")

#lower(): cambia todo el texto a minusculas
#upper(): cambia el texto a mayusculas
asignatura=opcion.lower()

if asignatura in ("informática gráfica", "pruebas de software", "usabilidad y accesibilidad"):
    print("Asignatura elegida " + asignatura)
else:
    print("La asignatura escogida no esta contemplada")