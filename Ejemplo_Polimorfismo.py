class Coche():

    def desplazamiento(self):
        print("Me desplazo utilizando cuatro ruedas")

class Moto():

    def desplazamiento(self):
        print("Me desplazo utilizando dos ruedas")

class Camion():

    def desplazamiento(self):
        print("Me desplazo utilizando seis ruedas")

#-- Este metodo me ayuda en el polimorfismo
def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()

#Cambiando la instancia en miVehiculo puedo controlar el tipo que yo quiero que se ejecute

miVehiculo=Coche()
#miVehiculo=Moto()
#miVehiculo=Camion()

desplazamientoVehiculo(miVehiculo)