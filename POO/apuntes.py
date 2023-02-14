class Vector(object):
    def __init__ (self, x, y):
        self.x = x
        self.y = y
        
    def __add__ (self, v):
        # Sumar dos Vectores
        return Vector (self.x + v.x, self.y + v.y)
    
    def __sub__ (self, v):
        # Restar dos Vectores
        return Vector (self.x - v.x, self.y - v.y)
    
    def __mul__ (self, s):
        # Multiplicar un Vectores por un escalar
        return Vector (self.x * s, self.y * s)
    
    def __repr__ (self):
        # <__main__.Vector instance at 0x01DDDDC8>.
        # Ejemplo para git
        return '<Vector (%f, %f)>' % (self.x, self.y)
    
    
    def __str__(self):
        return f"({self.x},{self.y})"
    
    
coordenada_1 = Vector(5,4)
coordenada_2 = Vector(4,5)





coordenada_suma = coordenada_1 + coordenada_2



print(coordenada_suma)