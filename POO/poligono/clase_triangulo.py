from clase_poligono import Poligono

class Triangulo(Poligono):
    
    def __init__(self, base: int, altura: int):
        super().__init__(__class__.__name__, 3)
        
        self.base = base
        self.altura = altura
        
    def area(self):
        
        return f'El area del triangulo es: {self.base * self.altura / 2}'
    