from clase_poligono import Poligono

class Rectangulo(Poligono):
    
    def __init__(self, lado_corto: int, lado_largo: int):
        super().__init__(__class__.__name__, 4)
        
        self.lado_corto = lado_corto
        self.lado_largo = lado_largo
        
    def area(self):
        
        return f'El area del rectangulo es: {self.lado_corto * self.lado_largo}'