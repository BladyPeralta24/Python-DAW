# Escriba una clase "Pila" LIFO (Last In First Out) que tenga un atributo de lista de elementos y los métodos 
# "apilar" (para agregar un elemento a la pila), 
# "desapilar" (para quitar el último elemento agregado) y 
# "tamano" (para devolver el número de elementos en la pila). 
# Sobrecargue el operador "+" para que pueda sumar dos pilas y devolver una nueva pila que contenga todos los elementos de ambas pilas juntas.

class Pila():
    
    def __init__(self, lista_lifo = []):
        
        self.lista_lifo = lista_lifo
        
        
        
    def apliar(self, elemento):
        """ agrega un elemento a la pila """
        self.lista_lifo.append(elemento)
        
    
    def desapilar(self):
        """ quita el ultimo elemento agregado """
        self.lista_lifo.pop()
    
    def tamanho(self):
        """ Muestra el tamaño de la pila """
        return len(self.lista_lifo)
    
    def __add__(self, other):
        """ Suma dos pilas para que devuelva otra pila de ambas pilas juntas """
        return self.lista_lifo + other.lista_lifo
    
    
    def __str__(self):
        resultado = ""
        for elemento in self.lista_lifo:
            
            resultado += f"+-----+\n|  {elemento}  |\n"
            
        return resultado
    


lista1 = Pila([1,2,3,4,5])
lista2 = Pila([5,4,3,2,1])


lista1.apliar(6)
lista1.apliar(7)
lista1.apliar(8)
print(lista1.tamanho())


lista2.desapilar()
print(lista2.tamanho())

print(lista1 + lista2)

print("\n-----LISTA LIFO-----\n",lista1)
print("\n-----LISTA LIFO-----\n",lista2)