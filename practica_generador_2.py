#-- yield from devuelve los subelementso del elementos dentro del generador

def devuelve_ciudades(*ciudades):
    # El asterisco (*) signfica que recibira un numero indeterminado de elememntos en forma de tupla

    for elemento in ciudades:
        #for subElemento in elemento:
            yield from elemento

ciudades_devueltas=devuelve_ciudades("Madrid","Barcelona","Bilbao","Valencia")

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))