from clase_coleccion import Coleccion

class LIFO(Coleccion):
    
    def __init__(self, lista = []):
        super().__init__()
        
        self.lista = lista
        
        
    def estaVacio(self):
       return self.lista == []
    
    
    def extraer(self):
        return f'el elemento {self.lista.pop()} se ha eliminado'
    
    
    def primero(self):
        return self.lista[0]
    
    
    
    def anhadir(self, elemento):
        self.lista.append(elemento)
        if elemento in self.lista:
            return True
        else:
            return False
    
    
    def ultimo(self):
        return self.lista[-1]
    
    
lista_lifo = LIFO([])

print(lista_lifo.estaVacio())
lista_lifo.anhadir(1)
lista_lifo.anhadir(2)
lista_lifo.anhadir(3)
lista_lifo.anhadir(4)
lista_lifo.anhadir(5)
print(lista_lifo.estaVacio())
print(lista_lifo.primero())
print(lista_lifo.ultimo(), "\n")


print(lista_lifo.extraer())
print(lista_lifo.primero())
print(lista_lifo.ultimo())









# from coleccion import *


# class LIFO(Coleccion):
    
#     def __init__(self):
#         self.coleccion = []
        
        
#     def estaVacia(self):
        
#         """
#         if len(self.coleccion) == 0 :
#             return True
#         else:
#             return False
#         """
#         return len(self.coleccion) == 0
    
    
#     def extraer(self):       
        
        
#         return self.coleccion.pop(0)
    
    
#     def primero(self):
#         return self.coleccion[0]
    
#     def anhadir(self, elemento_nuevo):
#         self.coleccion.append(elemento_nuevo)
        
#         return True
    
#     def ultimo(self):
#         return self.coleccion[-1]