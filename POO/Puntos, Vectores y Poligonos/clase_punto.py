import math


class Punto():
    
    def __init__(self, x = 0, y = 0):
        
        self.x = x
        self.y = y
        
        
    def cuadrante(self):
        if self.x == 0 and self.y == 0:
            return "Punto de origen"
        
        elif self.x == 0 and self.y != 0:
            return "Eje Y"
        
        elif self.x != 0 and self.y == 0:
            return "Eje X"
        
        elif self.x >= 0 and self.y >= 0:
            return "Primer cuadrante"
        
        elif self.x >= 0 and self.y <= 0:
            return "Segundo cuadrante"
        
        elif self.x <= 0 and self.y <= 0:
            return "Tercer Cuadrante"
        
        elif self.x <= 0 and self.y >= 0:
            return "Cuarto Cuadrante"
        
    def vector(self, puntox = 0, puntoy = 0):
        P = int(puntox - self.x)
        Q = int(puntoy - self.y)
        
        return self.vector(P,Q)
        
    def distancia(self, puntox = 0, puntoy = 0):
        P = int((puntox - self.x)**2)
        Q = int((puntoy - self.y)**2)
        
        return math.sqrt(P+Q)
    
        
    def __str__(self):
        return f'({self.x},{self.y})'
    
    

punto1 = Punto(1,2)
punto2 = Punto(4,5)

print(punto1.vector(4,5))