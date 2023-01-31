from clase_poligono import Poligono
from clase_triangulo import Triangulo
from clase_rectangulo import Rectangulo


triangulo1 = Triangulo('Triangulo', 3, 3, 4)
print(triangulo1.area())

rectangulo1 = Rectangulo('Rectangulo', 4, 6, 5)
print(rectangulo1.area())


def datos_de_poligono(poligono: Poligono):
    return f'Area: {poligono.area()}\nNombre del poligono: {poligono.nombre}'

print(datos_de_poligono(triangulo1))
print(datos_de_poligono(rectangulo1))