# # importar el modulo io
# from io import open
# # Utilizo la función open() sobre una variable  para abrir el archivo y le paso 2 variables; la primera es el nombre y la segunda es una "w" para abrirlo en forma escritura
# archivo_texto = open("archivo", "w")

# frase = "Estupendo día para estudiar Python \n el miércoles"
# # Utilizo write para pasarle lo que se escribio en la variable frase
# archivo_texto.write(frase)
# # Utilizo close() para cerrar mi archivo
# archivo_texto.close()
# -----------------------------------------------
# # importar el modulo io
# from io import open
# # Utilizo la función open() sobre una variable  para abrir el archivo y le paso 2 variables; la primera es el nombre y la segunda es una "r" para abrirlo en forma lectura
# archivo_texto = open("archivo", "r")

# # Utilizo "read" para leer el archivo y lo almaceno en una variable "texto". Puedo utilizar readlines() para leer una linea del archivo
# texto = archivo_texto.read()
# # Utilizo close() para cerrar mi archivo
# archivo_texto.close()

# print(texto)
# -----------------------------------------------
# # importar el modulo io
# from io import open
# # Utilizo la función open() sobre una variable  para abrir el archivo y le paso 2 variables; la primera es el nombre y la segunda es una "r" para abrirlo en forma lectura
# archivo_texto = open("archivo", "r")
# # Utilizo readlines() para que me guarde cada línea de texto como una lista
# lineas_texto = archivo_texto.readlines()

# archivo_texto.close()

# print(lineas_texto[1])
# -----------------------------------------------
# # importar el modulo io
# from io import open
# # Utilizo la función open() sobre una variable  para abrir el archivo y le paso 2 variables; la primera es el nombre y la segunda es una "a" para agregar al archivo
# archivo_texto = open("archivo", "a")

# archivo_texto.write("\n siempre es buena ocasión para estudiar Python")

# archivo_texto.close()
# -----------------------------------------------
# # importar el modulo io
# from io import open

# archivo_texto = open("archivo", "r")
# # Si al metodo read() le paso un número me hara la lectura desde el inicio hasta el caracter que indique el número
# print(archivo_texto.read(11))
# # Con seek() le pasamos un numero y lo que hace es colocar el puntero en la posición que le dentro del texto
# archivo_texto.seek(11)

# print(archivo_texto.read())

# archivo_texto.close()
# -----------------------------------------------
# importar el modulo io
from io import open

archivo_texto = open("archivo2.txt", "r+")  # Lectura y escritura

# print(archivo_texto.readlines())

# archivo_texto.write("Comienzo de texto")

lista_texto = archivo_texto.readlines()

lista_texto[1] = " Esta líena a sido incluida desde el exterior \n"

archivo_texto.seek(0)

archivo_texto.writelines(lista_texto)

archivo_texto.close()
