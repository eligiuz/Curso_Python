# # Para guardar información en un fichero binario-----------
# # se importa la librería pickle para la serialización
# import pickle
# # Creo la lista que quiero guardar
# lista_nombres = ["Pedro", "Ana", "María", "Isabel"]
# # Se utiliza open() para abrir el fichero con dos parametros; "unnombre" y "wb" ya que vamos aescribir un fichero binario
# fichero_binario = open("lista_nombres", "wb")
# # Utilizamos pickle.dump() para volcar la lista en el archivo binario. Le damos dos parametros; una variable con la lista de nombres y una variable con la opción de abrir el fichero
# pickle.dump(lista_nombres, fichero_binario)
# # Cerramos el fichero
# fichero_binario.close()
# # Como ya se ha guardado podemos eliminar la variable del fichero bonario
# del (fichero_binario)

# -----------------------------------------
# Sacar la información de un fichero binario

import pickle
# Se utiliza nuevamente open() con dos parametros "nombredelarchivo" (debe ser el nombre del archivo guardado en la computadora) y "rb" para leer el fichero binario
fichero = open("lista_nombres", "rb")
# Utilizamos pickle con el metodo load y le pasamos como parametro el nombre de l avariable del open
lista = pickle.load(fichero)

print(lista)
