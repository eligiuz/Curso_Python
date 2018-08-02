# Declaro la librería
from tkinter import *
# Creo la ventana
root = Tk()
# Creo la variable del frame y lo declaro con los parametros de la variable raiz y el tanaño deseado
miFrame = Frame(root, width=500, height=400)
# Empaco el frame dentro de la ventana raiz
miFrame.pack()
# A una variable la instanciamos con label pasando parametros: nombredelFrame y texto que se quiere mostrar
# miLabel = Label(miFrame, text="Hola alumnos de Python")
# # Colocamos el label en unas coordenadas determinadas
# miLabel.place(x=100, y=200)

# Declaramos la imagen que queremos utilizar dandole el nombre y la ubicaicón del archivo
miImagen = PhotoImage(file="mouse.gif")

# # Si queremos abreviar le codigo
# Label(miFrame, text="Hola alumnos de Python", fg="red", font=("Comic Sans MS", 18)).place(x=100, y=200)

# Para colocar una imagen
Label(miFrame, image=miImagen).place(x=100, y=200)

# Ejecutamos la ventana en un loop
root.mainloop()
