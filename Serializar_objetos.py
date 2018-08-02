# Crear fichero binario con un objeto adentro
import pickle


class Vehiculo():

    def __init__(self, marca, modelo):

        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):

        self.enmarcha = True

    def acelerar(self):

        self.acelera = True

    def frenar(self):

        self.frena = True

    def estado(self):

        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrena: ", self.frena)


coche1 = Vehiculo("Mazda", "MX5")

coche2 = Vehiculo("Seat", "Leon")

coche3 = Vehiculo("Renault", "Megane")

coches = [coche1, coche2, coche3]

fichero = open("losCoches", "wb")

pickle.dump(coches, fichero)

fichero.close()

del (fichero)

# ----------------------------------------
# Leer un fichero binario que contiene un objeto

ficheroApertura = open("losCoches", "rb")

misCoches = pickle.load(ficheroApertura)
ficheroApertura.close()

for c in misCoches:

    print(c.estado())
# Para poder realizar cada proceso en diferentes archivos se debe pasar al segundo archivo la clase ya que si no nos maracria error porque el fichero solo contienen los datos del objeto no su descripción
