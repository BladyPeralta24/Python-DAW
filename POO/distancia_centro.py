import math

lista = [(3, 4), (1, 2), (6, 8), (0, 1)]

lista_ordenada = sorted(lista, key= lambda coordenada : math.sqrt(coordenada[0]**2 + coordenada[1]**2))

print(lista_ordenada)



        
        