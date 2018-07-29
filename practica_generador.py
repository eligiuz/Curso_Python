#-- Extraen valores de una función y se almacenan en objetos iterables ( que se pueden recorrer) --
#-- Se Almacenan de uno en uno. Cada vez que se almacena un valor, el generador permanece en un estado pausado hasta que se solicita el siguiente. "Suspensión de estado" --

# # Sintaxis

# def generaPares(limite):
#     num=1

#     while num<limite:

#         yield num*2

#         num=num+1

# devuelvePares=generaPares(10)

# for i in devuelvePares:
#     print(i)

#-- Imprime los tres primeros elementos

def generaPares(limite):
    num=1

    while num<limite:

        yield num*2

        num=num+1

devuelvePares=generaPares(10)

print(next(devuelvePares))

print("Aquí pordría ir más código...")

print(next(devuelvePares))

print("Aquí pordría ir más código...")

print(next(devuelvePares))
