class DivisionPorCeroError(Exception):
    pass

class EntradaNoValidaError(Exception):
    pass


class Calculadora():

    @staticmethod
    def sumar(sumando1, sumando2):
        if not isinstance(sumando1, int) and not isinstance(sumando2, int):
            raise EntradaNoValidaError("debes de introducir un dato numerico")
        else:
            return sumando1 + sumando2
    
    @staticmethod
    def restar(minuendo, sustraendo):
        return minuendo - sustraendo
    
    @staticmethod
    def multiplicar(multiplicando, multiplicador):
        return multiplicando * multiplicador
    
    @staticmethod
    def dividir(dividendo, divisor):
        return dividendo / divisor
    


try:
    calculo1 = Calculadora()

    print(calculo1.sumar(3,"g"))
    
except EntradaNoValidaError as e:
    print("Error al introducir un dato no numerico." + e)