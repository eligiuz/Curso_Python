from tkinter import *


raiz = Tk()
# Creamos un frame y lo colocamos dentro de l aventana
miFrame = Frame(raiz, width=1200, heigh=600)
miFrame.pack()

# Asignamos  auna variable el cuadro de texto que estara dentro del frame
cuadroNombre = Entry(miFrame)
cuadroNombre.grid(row=0, column=1, padx=10, pady=10)
cuadroNombre.config(fg="red", justify="center")

cuadroPass = Entry(miFrame)
cuadroPass.grid(row=1, column=1, padx=10, pady=10)
cuadroPass.config(show="*")

cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row=2, column=1, padx=10, pady=10)

cuadroDireccion = Entry(miFrame)
cuadroDireccion.grid(row=3, column=1, padx=10, pady=10)

# sticky alinea el texto a la orinetaión que le mencione. El padx o pady se utiliza para dar padding
nombreLabel = Label(miFrame, text="Nombre:")
nombreLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

apellidoLabel = Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

direccionLabel = Label(miFrame, text="Direccion de casa:")
direccionLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

passLabel = Label(miFrame, text="Password:")
passLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

raiz.mainloop()
