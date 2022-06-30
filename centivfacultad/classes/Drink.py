class Drink:
    #def __init__(self) -> None:
    #    pass
    def __init__ (self, name):
        self.__name = name # el __ lo privatiza
    def getDetail(self):
        return "la bebida es:" + self.__name

drink = Drink("agua")
print(drink.getDetail())

## herencia
class Beer(Drink):
    def __init__(self, name, brand, alcohol):
        super().__init__(name)
        self.__brand = brand
        self.__alcohol = alcohol
    def getDetail(self): ## sobre escritura
        return "soy un hijo: "

beer1 = Beer("Pale ale", "Minerva", 4.5)
print(beer1.getDetail())

## 