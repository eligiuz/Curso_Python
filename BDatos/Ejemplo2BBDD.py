import sqlite3

miConexion = sqlite3.connect("GestionProductos")

miCursor = miConexion.cursor()

# miCursor.execute('''
#     CREATE TABLE productos (
#     id integer PRIMARY KEY AUTOINCREMENT,
#     nombre_articulo varchar(50) UNIQUE,
#     precio integer,
#     seccion varchar(20))
#     ''')

# productos = [
#     ("pelota", 20, "juguetería"),
#     ("pantalón", 15, "confección"),
#     ("destornillador", 25, "ferretería"),
#     ("jarrón", 45, "cerámica")
# ]

# miCursor.executemany("INSERT INTO productos VALUES (NULL,?,?,?)", productos)

# miCursor.execute("SELECT * FROM productos WHERE seccion = 'confección'")

# miCursor.execute("UPDATE productos SET precio=35 WHERE nombre_articulo='pelota'")

miCursor.execute("DELETE FROM productos WHERE id = 5")

productos = miCursor.fetchall()

print(productos)

miConexion.commit()

miConexion.close()
