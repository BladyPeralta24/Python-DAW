# Escriba una clase "Fraccion" que tenga un numerador y un denominador. 
# Sobrecargue los operadores "+" , "-", "*" , "/" , "==", "!=" para que puedan sumar, restar, multiplicar, dividir 
# y comparar dos fracciones y devolver una nueva fracción que represente el resultado.
import math

class Fraccion():
    
    def __init__(self, numerador, denominador):
        
        mcd = math.gcd(numerador, denominador)
        
        self.numerador = int(numerador / mcd)
        self.denominador = int(denominador / mcd)
        
    
    
    
    
    def __add__(self, other):
        
        numerador = self.numerador * other.denominador + other.numerador * self.denominador
        denominador = self.denominador * other.denominador
        
        return Fraccion(numerador, denominador)
    
    def __sub__(self, other):
        numerador = self.numerador * other.denominador - self.denominador * other.numerador
        denominador = self.denominador * other.denominador
        
        return Fraccion(numerador, denominador)
    
    def __mul__(self, other):
        
        numerador = self.numerador * other.numerador
        denominador = self.denominador * other.denominador
        return Fraccion(numerador, denominador)
    
    def __truediv__(self, other):
        numerador = self.numerador * other.denominador
        denominador = self.denominador * other.numerador 
        return Fraccion(numerador, denominador)
    
    def __eq__(self, other):
        
        return self.numerador == other.numerador and self.denominador == other.denominador
    
    def __ne__(self, other):
        
        return self.numerador != other.numerador or self.denominador != other.denominador
        
    
    
    def __str__(self):
        
        return f'{self.numerador}\n-\n{self.denominador}\n'
    
    
    
fraccion1 = Fraccion(12,4)
fraccion2 = Fraccion(5,4)


# print(fraccion1)
# print(fraccion2)

print(fraccion1 + fraccion2)
print(fraccion1 - fraccion2)
print(fraccion1 * fraccion2)
print(fraccion1 / fraccion2)
print(fraccion1 == fraccion2)
print(fraccion1 != fraccion2)





# Ejercicio hecho por el profe

# class Fraccion():
#     def __init__(self,numerador: int, denominador: int):
#         mcd = math.gcd(numerador,denominador)
        
        
#         self.numerador =  int(numerador / mcd)
#         self.denominador =  int(denominador / mcd)


#     def __str__(self):
#         return str(self.numerador) + "\n-\n" + str(self.denominador)
    
    
#     def __add__(self, fraccion2):
#         numerador   = self.numerador * fraccion2.denominador + fraccion2.numerador * self.denominador
#         denominador = self.denominador * fraccion2.denominador
        
#         return Fraccion(numerador, denominador)
    
#     def __sub__(self, fraccion2):
#         numerador   = self.numerador * fraccion2.denominador - fraccion2.numerador * self.denominador
#         denominador = self.denominador * fraccion2.denominador
        
#         return Fraccion(numerador, denominador)
    
    
#     def __mul__(self, fraccion2);
#         numerador   = self.numerador * fraccion2.numerador
#         denominador = self.denominador * fraccion2.denominador
        
#         return Fraccion(numerador, denominador)
    
#     def __truediv__(self, fraccion2);
#         numerador   = self.numerador * fraccion2.denominador
#         denominador = self.denominador * fraccion2.numerador
        
#         return Fraccion(numerador, denominador)
    
    
#     def __eq__(self, fraccion2):
        
#         return self.numerador == fraccion2.numerador and self.denominador == fraccion2.denominador
    
    
#     def __ne__(self, fraccion2):
        
#         return self.numerador != fraccion2.numerador or self.denominador != fraccion2.denominador
    
# fraccion1 = Fraccion(2,4)
# fraccion2 = Fraccion(1,4)
# fraccion3 = Fraccion(1,4)