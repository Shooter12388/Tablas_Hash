import pickle
import os


def escribir(ruta, libro):
    pickle.dump(libro, open(ruta, "wb"))


def leer(ruta):
    return pickle.load(open(ruta, "rb"))


def añadir(ruta, libro):
    if os.path.exists(ruta):
        datos = leer(ruta)
        datos.append(libro)
        escribir(ruta, datos)
    else:
        escribir(ruta, [libro])


def eliminar(ruta, libro):
    if os.path.exists(ruta):
        datos = leer(ruta)
        datos.remove(libro)
        escribir(ruta, datos)
