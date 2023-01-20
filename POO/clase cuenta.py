from persona import Persona

class Cuenta():
    def __init__(self, titular = Persona() , cantidad: float = 0.0):
        
        self.titular = titular
        self.cantidad = cantidad
        
    
    @property
    def cantidad(self):
        return self.__cantidad
    
    @cantidad.setter
    def cantidad (self, nuevo_valor):
        if isinstance(nuevo_valor, float) and nuevo_valor >= 0.0:
            self.__cantidad = nuevo_valor
        else:
            print("ERROR. La cantidad insertada no es válido")
            

    def mostrar(self):
        return f"Titular: \n{self.titular.mostrar()}\nCantidad: {self.__cantidad}€\n"
    
    
    def ingresar(self, cantidad_ingresada):
        
        if cantidad_ingresada > 0.0:
            self.__cantidad += cantidad_ingresada
            
        return f"Has ingresado: {cantidad_ingresada}€"
    
    
        
    def retirar(self, cantidad_retirada):
        if cantidad_retirada > 0.0:
            
            self.__cantidad -= cantidad_retirada
            
        return f"Has retirado: {cantidad_retirada}€"
    
    
titular1 = Cuenta()

titular1.cantidad = 500.0
titular1.titular.nombre = "Bladimir"
titular1.titular.edad = 24
titular1.titular.dni = "78848952F"
print(titular1.mostrar())


titular1.ingresar(200)
print(titular1.mostrar())

titular1.retirar(800)
print(titular1.mostrar())


titular2 = Cuenta(Persona ("Junior", 23, '78819396Y'), 100.0)
print(titular2.mostrar())
