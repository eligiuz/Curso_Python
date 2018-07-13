#Sintaxis
midiccionario={"Alemania":"Berlín","Francia":"Paris", "Reino Unido":"Londres", "España":"Madrid"}
print(midiccionario["España"])
#Agregar mas elementos al diccionario
midiccionario["Italia"]="Lisboa"
print(midiccionario)
#modificar un valor en le dicciconario
midiccionario["Italia"]="Roma"
print(midiccionario)
#elimina un elemento del dicionario
del midiccionario["Reino Unido"]
print(midiccionario)

#Crea diccionario complejo
midiccionario={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "anillos":{"temporadas":[1991,1992,1993,1996,1997,1998]}}
# Imprime las llaves de midiciconario
print(midiccionario.keys())
#imprime los valores guardados
print(midiccionario.values())
#imprime la longitud del diccionario
print(len(midiccionario))
print(midiccionario)