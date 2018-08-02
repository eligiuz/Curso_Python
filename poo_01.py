# -- Sintaxis
# -- Creamos la clase


class Coche():

    # -- El constructor me sirve para decirle a la clase cual es el estado inicial de la clase

    def __init__(self):

        self.__largoChasis = 250
        self.__anchoChasis = 120
        # -- Para encapsular una propiedad se utilizan los dos guiones bajos (__)
        self.__ruedas = 4
        self.__enmarcha = False

    # -- Metodos
    def arrancar(self, arrancamos):
        # -- Lo que hace self es almacenar al objeto como parametro, en el ejemplo el objeto es miCoche; la sintaxis podría leerse como miCoche.enmarcha=True

        self.__enmarcha = arrancamos

        if (self.__enmarcha):
            chequeo = self.__chequeo_interno()

        if (self.__enmarcha and chequeo):
            return "El coche esta en marcha"

        elif(self.__enmarcha and chequeo == False):
            return "Algo a ido mal en el chequeo. No podemos arrancar"

        else:

            return "El coche esta parado"

    def estado(self):
        print("El coche tiene ", self.__ruedas, " ruedas. Un ancho de ", self.__anchoChasis, " y un largo de ", self.__largoChasis)

    # -- Se encapsula (__) el metodo para que no se pueda acceder a dicho metodo fuera de la clase
    def __chequeo_interno(self):
        print("Realizando chequeo interno")
        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "cerradas"

        if (self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas"):

            return True

        else:

            return False


# -- Instanciamos la clase
miCoche = Coche()

print(miCoche.arrancar(True))

miCoche.estado()


print("------------A continuación creamos el segundo objeto ------------------")

miCoche2 = Coche()

print(miCoche2.arrancar(False))
#  # -- Como esta encapsulada podemos ver no se modifica el atributo ruedas
#  miCoche2.ruedas=5

miCoche2.estado()
