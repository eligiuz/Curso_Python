from tkinter import *


raiz = Tk()
# Creamos un frame y lo colocamos dentro de l aventana
miFrame = Frame(raiz, width=1200, heigh=600)
miFrame.pack()

minombre = StringVar()

# Asignamos  auna variable el cuadro de texto que estara dentro del frame
cuadroNombre = Entry(miFrame, textvariable=minombre)
cuadroNombre.grid(row=0, column=1, padx=10, pady=10)
cuadroNombre.config(fg="red", justify="center")

cuadroPass = Entry(miFrame)
cuadroPass.grid(row=1, column=1, padx=10, pady=10)
cuadroPass.config(show="*")

cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row=2, column=1, padx=10, pady=10)

cuadroDireccion = Entry(miFrame)
cuadroDireccion.grid(row=3, column=1, padx=10, pady=10)
# Agregamos una ventana de texto con Text() l eponemos que pertenece a un frame y le damos un tamaño dentrod e ese frame.
textoComentario = Text(miFrame, width=16, height=5)
textoComentario.grid(row=4, column=1, padx=10, pady=10)
# --------  USO DE SCROLLBAR
# Para agregar el scroll bar se le asigna a una variable la función Scrollbar() diciendo a quien pertenece  y con command() se le dice en donde debe de estar y com se movera x horizontal y vertical
scrollVert = Scrollbar(miFrame, command=textoComentario.yview)
# Se coloca sticky para adaptar al tamaño de la ventana de texto
scrollVert.grid(row=4, column=2, sticky="nsew")
# Utilizo config() y yscrollcommand(nombredelscroll.set) para controlar el movimiento del cursos
textoComentario.config(yscrollcommand=scrollVert.set)
# --------  USO DE SCROLLBAR

# sticky alinea el texto a la orinetaión que le mencione. El padx o pady se utiliza para dar padding
nombreLabel = Label(miFrame, text="Nombre:")
nombreLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

apellidoLabel = Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

direccionLabel = Label(miFrame, text="Direccion:")
direccionLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

passLabel = Label(miFrame, text="Password:")
passLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

comentariosLabel = Label(miFrame, text="Comentarios:")
comentariosLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

# ------ AGREGAR BOTON

# Funcion que unicamente asigna nuestro nombre a una variable que sera desplegada en la caja de nombre
def codigoBoton():

    minombre.set("Eligio")


# Se crea el boton y con command se le dice que debe estar asociado a la funcion codigoboton
botonEnvio = Button(raiz, text="Enviar", command=codigoBoton)

botonEnvio.pack()


raiz.mainloop()
