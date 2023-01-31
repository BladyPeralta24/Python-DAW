from clase_poligono import Poligono

class Rectangulo(Poligono):
    
    def __init__(self, nombre, lado, lado_corto: int, lado_largo: int):
        super().__init__(nombre, lado)
        
        self.lado_corto = lado_corto
        self.lado_largo = lado_largo
        
    def area(self):
        if self.lado == 4:
            return f'El area del rectangulo es: {self.lado_corto * self.lado_largo}'
        else:
            return 'No se puede calcular el area'