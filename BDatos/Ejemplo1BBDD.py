import sqlite3


miConexion = sqlite3.connect("PrimerBase")

miCursor = miConexion.cursor()

# miCursor.execute("CREATE TABLE productos (nombre_articulo varchar(50), precio integer, seccion varchar(20))")

# miCursor.execute("INSERT INTO productos VALUES ('BALÓN', 15, 'DEPORTES')")

# variosProductos = [

#     ("Camiseta", 10, "Deportes"),
#     ("Jarrón", 10, "Cerámica"),
#     ("Camón", 10, "Juguetería")

# ]

# miCursor.executemany("INSERT INTO productos VALUES (?, ?, ?)", variosProductos)

# Confirmar los cambios

miCursor.execute("SELECT * FROM productos")

variosProductos = miCursor.fetchall()

# print(variosProductos)

for productos in variosProductos:

    print("Nombre artículos:", productos[0], "Sección: ", productos[2])

miConexion.commit()


miConexion.close()
