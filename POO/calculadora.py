class DivisionPorCeroError(Exception):
    pass

class EntradaNoValidaError(Exception):
    pass


class Calculadora():
    
    
    @staticmethod
    def verificarDatos(numero1, numero2):
        if isinstance(numero1, int) and isinstance(numero2, int):
            pass
        else:
            raise EntradaNoValidaError("Debes de introducir datos numéricos")
    
    
    @staticmethod
    def sumar(sumando1, sumando2):
        if not Calculadora.verificarDatos(sumando1, sumando2):
            return sumando1 + sumando2
            
    
    @staticmethod
    def restar(minuendo, sustraendo):
        if not Calculadora.verificarDatos(minuendo, sustraendo):
            return minuendo - sustraendo
    
    @staticmethod
    def multiplicar(multiplicando, multiplicador):
        if not Calculadora.verificarDatos(multiplicando, multiplicador):
            return multiplicando * multiplicador
    
    @staticmethod
    
    def dividir(dividendo, divisor):
        if not Calculadora.verificarDatos(dividendo, divisor) and divisor != 0:
            return dividendo / divisor
        else:
            raise DivisionPorCeroError("No se puede dividir por cero")
        
        

prueba = Calculadora()

try:

    print(prueba.sumar(3,5))
    
except EntradaNoValidaError as e:
    print("Error." , e)
    
try:

    print(prueba.restar(3,5))
    
except EntradaNoValidaError as e:
    print("Error." , e)
    
try:

    print(prueba.multiplicar(3,5))
    
except EntradaNoValidaError as e:
    print("Error." , e)
    
try:

    print(prueba.dividir(3,5))
    
except EntradaNoValidaError as e:
    print("Error." , e)
    
try:

    print(prueba.dividir(3,0))
    
except DivisionPorCeroError as e:
    print("Error." , e)
    