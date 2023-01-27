# Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase CuantaJoven que deriva de la anterior. 
# Cuando se crea esta nueva clase, además del titular y la cantidad se debe guardar una bonificación que estará expresada en tanto por ciento.
# Construye los siguientes métodos para la clase:

# - Un constructor.
# - Los setters y getters para el nuevo atributo.
# - En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad., 
# por lo tanto hay que crear un método esTitularValido() que devuelve verdadero si el titular es mayor de edad pero menor de 25 años y falso en caso contrario.

# - Además la retirada de dinero sólo se podrá hacer si el titular es válido.
# - El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.
# - Piensa los métodos heredados de la clase madre que hay que reescribir.

from persona import Persona
from clase_cuenta import Cuenta

class cuentaJoven(Cuenta):
    def __init__(self, titular=..., cantidad: float = 0, bonificacion : int = 0):
        super().__init__(titular, cantidad)
        
        self.__bonificacion = bonificacion
        
    
    @property
    def bonificacion(self):
        return self.__bonificacion
    
    @bonificacion.setter
    def bonificacion(self, nuevo_valor):
        if isinstance(nuevo_valor, int) and nuevo_valor >= 0 and nuevo_valor <= 100:
            self.__bonificacion = nuevo_valor
        else:
            print("ERROR. El valor de la bonificacion no es valida")
            
    
    def esTitularValido(self):
    
        return self.titular.esMayorDeEdad() and self.titular.edad <= 25
    
    
    def mostrar(self):
        
        return f'Cuenta Joven:\n{super().mostrar()}Bonificacion: {str(self.__bonificacion)}%\n'
    
    def retirar(self, cantidad_retirada):
        if self.esTitularValido():
            return super().retirar(cantidad_retirada)
        else:
            print('No es una cuenta joven. No puedes retirar dinero\n') 
    
    

carlos = cuentaJoven(Persona("Carlos", 24, '78848952F'), 100.0, 15)

print(carlos.esTitularValido())

print(carlos.mostrar())

carlos.retirar(10)

print(carlos.mostrar())

