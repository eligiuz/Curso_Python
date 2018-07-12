# -*- coding: latin_1 -*-
miLista=["María","Pepe","Marta", "Antonio"]
#Inserta con append un valor al final de la lista
# miLista.append("Sandra")
#Inserta con insert un valor en la posición antes de la coma
# miLista.insert(2,"Sandra")
#Insertar varios elementos en la lista
# miLista.extend(["Sandra", "Ana","Lucía"])
#Imprime toda la lista
# print(miLista[:])
#Imprime el valor de la posisción que se pnga entre corchetes
# print(miLista[3])
#Imprime la posición del valor que se encuentre entre paréntesis
# print(miLista.index("Antonio"))
#RElimina el elemento que s eencuentra entre paréntesis
# miLista.remove("Marta")
#Coloca true si encuentra el elemento o false si no lo encuentra
# print("Pepe" in miLista)
#Elimina el último elemento de la lista
# miLista.pop()

print(miLista[:])

miLista2=["Sandra","Lucía"]
#Concatena las listas
miLista3=miLista + miLista2

print(miLista3[:])