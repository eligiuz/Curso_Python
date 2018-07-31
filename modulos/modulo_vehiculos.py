#-- Herencia

class Vehiculos():

    def __init__(self,marca,modelo):
        
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False

    def arrancar(self):
        
        self.enmarcha=True

    def acelerar(self):
        
        self.acelera=True

    def frenar(self):
        
        sel.frena=True

    def estado(self):
        
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ",self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrena: ", self.frena)

#-- Para heredar (sintaxis)

class Furgoneta(Vehiculos):

    def carga(self,cargar):
        self.cargado=cargar
        if (self.cargado):
            return "La furgoneta está cargada"
        else:
            return "La furgoneta no está cargada"


class Moto(Vehiculos):
    hcaballito=""
    def caballito(self):
        self.hcaballito="Voy haciendo el caballito"
    
    #-- Se puede sobreescribir métodos

    def estado(self):
        
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ",self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrena: ", self.frena, "\n", self.hcaballito)

class VElectricos(Vehiculos):
    
    def __init__(self,marca,modelo):

        super().__init__(marca,modelo)

        self.autonomia=100

    def cragarEnergia(self):

        self.cargando=True
