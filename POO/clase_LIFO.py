
from clase_coleccion import Coleccion

class FIFO(Coleccion):
    
    def __init__(self, lista = []):
        super().__init__()
        
        self.lista = lista
        
    
    def estaVacio(self):
        return self.lista == []
    
    
    def extraer(self):
        return f'el elemento {self.lista.pop(0)} se ha eliminado'
    
    
    
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
    
    
    
lista_fifo = FIFO([])

print(lista_fifo.estaVacio())
lista_fifo.anhadir(1)
lista_fifo.anhadir(2)
lista_fifo.anhadir(3)
lista_fifo.anhadir(4)
lista_fifo.anhadir(5)
print(lista_fifo.estaVacio())
print(lista_fifo.primero())
print(lista_fifo.ultimo(), "\n")


print(lista_fifo.extraer())
print(lista_fifo.primero())
print(lista_fifo.ultimo())