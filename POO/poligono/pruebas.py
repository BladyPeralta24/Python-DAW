from clase_poligono import Poligono
from clase_triangulo import Triangulo
from clase_rectangulo import Rectangulo





def datos_de_poligono(poligono: Poligono):
    return f'Area: {poligono.area()}\nNombre del poligono: {poligono.nombre}'

triangulo = Triangulo(3, 4)
rectangulo = Rectangulo(6, 5)

print(datos_de_poligono(triangulo))
print(datos_de_poligono(rectangulo))