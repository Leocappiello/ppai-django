from Model.Caracteristica import Caracteristica

class CaracteristicaRecurso:
    def __init__ (self, valor, caracteristica):
        self.__valor = valor
        self.__caracteristica = caracteristica

    def mostrarCaracteristicaRecurso(self):
        return self.__caracteristica