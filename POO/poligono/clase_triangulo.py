from clase_poligono import Poligono

class Triangulo(Poligono):
    
    def __init__(self, nombre, lado, base: int, altura: int):
        super().__init__(nombre, lado)
        
        self.base = base
        self.altura = altura
        
    def area(self):
        if self.lado == 3:
            return f'El area del triangulo es: {self.base * self.altura / 2}'
        else:
            return 'No se puede calcular el area'