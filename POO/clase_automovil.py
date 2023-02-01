# Crear una clase "Automóvil" con un atributo privado "kilometraje" 
# y un método estático "calcular_consumo_de_combustible" 
# que calcule el consumo de combustible en función de un kilometraje que venga dado como parámetro de entrada. 
# Utilizar un setter y un getter para acceder al kilometraje.

class Automovil():
    
    PRECIO_POR_KILOMETRO = 1.4
    
    def __init__(self, kilometraje: float = 0):
        
        self.kilometraje = kilometraje
        
    @property
    def kilometraje(self):
        return self.__kilometraje
    
    @kilometraje.setter
    def kilometraje(self, nuevo_valor):
        self.__kilometraje = nuevo_valor
        
    @staticmethod
    def calcular_consumo_de_combustible(kilometraje: int):
        return Automovil.PRECIO_POR_KILOMETRO * kilometraje
    
    
fiat = Automovil(300000)
#print(fiat.kilometraje)
print(Automovil.calcular_consumo_de_combustible(fiat.kilometraje))