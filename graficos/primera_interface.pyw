# Importamos la librería para crear ventanas de Tk
from tkinter import *

# Le asignamos a una variable la raiz de las ventanas
raiz = Tk()
# Le ponemos un tiutlo a la ventana
raiz.title("Ventana de pruebas")
# si se le pasa resizable con los parametros True o False se controla el modificat manualmente el alto y el ancho; endonde el primer parametro es weigrh y el segundo es heigh.
# raiz.resizable(True, False)
# Para agregar un icono a la ventana
raiz.iconbitmap("bombilla3.icns")
# Con geometry() se le puede dar un tamaño definido a la ventana en cuanto abre. Aunque la raiz siempre toma el tamaño de lo que contiene
# raiz.geometry("650x350")
# Podemos por ejemplo cambiar el color de la ventana con config()
raiz.config(bg="blue")
# Creamos el Frame
miFrame = Frame()
# Empacamos le frame dentro de la ventana
miFrame.pack()
# le ponemos un color de fondo al frame
miFrame.config(bg="red")
# le damos un tamaño especifico al frame
miFrame.config(width="650", heigh="350")

miFrame.config(bd="35")

miFrame.config(relief="sunken")

miFrame.config(cursor="pirate")

# Iniciamos la ventana para mostrarla colocandola en un bucle
raiz.mainloop()
