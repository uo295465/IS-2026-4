from . import bienvenido

@bienvenido.route('/')
def inicio():
    return "Hola, bienvenido a la aplicación Amigos"
    ss