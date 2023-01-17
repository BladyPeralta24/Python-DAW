class Pizza():
    def __init__(self, tamanho):
        self.__ingredientes = []
        self.tamanho = tamanho
        
        
    def agregar_ingrediente(self):
        ingredientes = ''
        ingredientes = input('Introduce un ingrediente a la pizza: ')
        while not ingredientes == '':
            self.__ingredientes.append(ingredientes)
            ingredientes = input('Introduce un ingrediente a la pizza: ')
        
    def quitar_ingrediente(self):
        ingrediente = input('¿Qué ingrediente deseas eliminar?: ')
        while not ingrediente == '':
            if ingrediente in self.__ingredientes:
                self.__ingredientes.remove(ingrediente)
            ingrediente = input('¿Qué ingrediente deseas eliminar?: ')
    
    def mostrar_informacion(self):
        
        return (f'Ingredientes: {self.__ingredientes}, tamaño de la pizza, {self.tamanho}')
    

pizza1 = Pizza('mediana')

pizza1.agregar_ingrediente()
print(pizza1.mostrar_informacion())
pizza1.quitar_ingrediente()
print(pizza1.mostrar_informacion())

