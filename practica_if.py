print("Programa de evaluacion de notas de alumnos")

nota_alumno=input("Introduce la nota del alumno: ")
#input() nos sirve para poder recibir un dato de la consola


def evaluacion(nota):
    valoracion="aprobado"
    #Sintaxis de if
    # > mayor que
    # < menor que
    # == igualque
    # >= mayor igual
    # <= menor igual
    # != diferente
    if nota<5:
        valoracion="suspenso"
    return valoracion
#int() nos sirve para convertir lo que esta adentro en un numero entero
print(evaluacion(int(nota_alumno)))