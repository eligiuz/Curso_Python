class Persona():

    def __init__(self,nombre,edad,Lugar_residencia):
        
        self.nombre=nombre
        self.edad=edad
        self.lugar_residencia=Lugar_residencia

    def descripcion(self):
        
        print("Nombre: ", self.nombre, " Edad: ", self.edad, " Residencia: ", self.lugar_residencia)

class Empleado(Persona):

    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):

        #-- siper() se utiliza pra poder pasar los parametros del padre

        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)

        self.salario=salario

        self.antiguedad=antiguedad

    def descripcion(self):

        super().descripcion()
        
        print(" Salario: ", self.salario, "Antigüedad: ", self.antiguedad)


Manuel=Empleado(1500,15,"Manuel",55,"Colombia")

Manuel.descripcion()

#-- isinstance() nos dice dce quien esta instanciado el objeto

print(isinstance(Manuel, Persona))
