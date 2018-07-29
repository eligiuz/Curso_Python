# Capturar varias excepciones
def divide():

    try:
    
        op1=(float(input("Introduce el primer número: ")))

        op2=(float(input("Introduce el segundo número: ")))

        print("La división es " + str(op1/op2))

    except ValueError:

        print("El valor introducido es erróneo")
    except ZeroDivisionError:

        print("No se puede dividir entre 0!")

     #-- Puedo colocar finally para ejecutar algo al final del except entre en el o no   
    finally:

        print("Cálculo finalizado")

    #-- Si quiero capturar cualquier excepción sin especificar entonces pongo

    # except:

    #     print("A ocurrido un error")

divide()