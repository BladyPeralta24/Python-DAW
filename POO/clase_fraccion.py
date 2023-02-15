# Escriba una clase "Fraccion" que tenga un numerador y un denominador. 
# Sobrecargue los operadores "+" , "-", "*" , "/" , "==", "!=" para que puedan sumar, restar, multiplicar, dividir 
# y comparar dos fracciones y devolver una nueva fracción que represente el resultado.


class Fraccion():
    
    def __init__(self, numerador, denominador):
        
        self.numerador = numerador
        self.denominador = denominador
        
    
    
    '''
    def maximo_comun_divisor(self, other):
        temporal = 0
        while self.denominador != 0:
            temporal = other.denominador
            other.denominador = self.denominador % other.denominador
            self.denominador = temporal
        return self.denominador
    
    def minimo_comun_multiplo(self, other):
        return (self.denominador + other.denominador) / self.maximo_comun_divisor(self, other)
    '''
    
    
    
    def __add__(self, other):
        
        mcd = other.denominador
        other.denominador = self.denominador % other.denominador
        self.denominador = mcd
        mcm = (self.denominador * other.denominador) / mcd
        
        numerador = (self.numerador / mcm) + (other.numerador / mcm)
        denominador = mcm
        
        return(numerador, denominador)
    
    def __sub__(self, other):
        pass
    
    def __mul__(self, other):
        
        numerador = self.numerador * other.numerador
        denominador = self.denominador * other.denominador
        return Fraccion(numerador, denominador)
    
    def __truediv__(self, other):
        numerador = self.numerador * other.denominador
        denominador = self.denominador * other.numerador 
        return Fraccion(numerador, denominador)
    
    
    def __str__(self):
        
        return f'{self.numerador}/{self.denominador}'
    
    
    
fraccion1 = Fraccion(2,3)
fraccion2 = Fraccion(4,5)


print(fraccion1)
print(fraccion2)

print('La suma de las fracciones es: ', fraccion1 + fraccion2, '\n')
#print('La resta de las fracciones es: ', fraccion1 - fraccion2, '\n')
#print('La multplicacion de las fracciones es: ', fraccion1 * fraccion2, '\n')
#print('La division de las fracciones es: ', fraccion1 / fraccion2, '\n')