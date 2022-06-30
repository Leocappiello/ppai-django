class Caracteristica:
    def __init__ (self, nombre, descripcion):
        self.__nombre = nombre
        self.__descripcion= descripcion

    def mostrarCaracteristica(self):
        return self.__nombre