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

print(titular1.titular.mostrar())




# Ejercicio hecho por el Profesor
""""

Clase Cuenta
Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y 
cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional. Construye 
los siguientes métodos para la clase:

Un constructor, donde los datos pueden estar vacíos.
Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente,
sólo ingresando o retirando dinero.
mostrar(): Muestra los datos de la cuenta.
ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, 
no se hará nada.
retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.


"""

# from includes.persona import Persona

# class Cuenta():
    
    
#     def __init__(self, titular : Persona, cantidad_entrada = 0.0):
#         self.titular = titular #titular es de la clase Persona
#         self.__cantidad = 0
#         self.cantidad = cantidad_entrada
        
        
        
        
#     @property
#     def cantidad(self):
#         return self.__cantidad
        
#     @cantidad.setter
#     def cantidad(self, nuevo_valor):
#         self.__cantidad = self.__cantidad + nuevo_valor
        
        
#     def mostrar(self):
#         return self.titular.mostrar() + " Cantidad: " + str(round(self.__cantidad,2))
    
#     def ingresar(self, cantidad):
#         if cantidad > 0 :
#             self.cantidad = cantidad
            
            
#     def retirar(self, cantidad):
#         self.cantidad = -cantidad
        
        
# cuenta_andres = Cuenta(Persona("Andrés", 22, "78551004R"),20)


# print(cuenta_andres.mostrar())

# cuenta_andres.ingresar(100)

# print(cuenta_andres.mostrar())

# cuenta_andres.ingresar(120.1241834264)

# print(cuenta_andres.mostrar())

# cuenta_andres.retirar(10)
# print(cuenta_andres.mostrar())


# print(cuenta_andres.titular.mostrar())


