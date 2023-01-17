class Pizza():
    def __init__(self, tamanho):
        self.__ingredientes = ['salsa de tomate', 'queso', 'oregano']
        self.tamanho = tamanho
        
        
    def agregar_ingrediente(self, ingrediente):
        
        self.__ingredientes.append(ingrediente)
        
    def quitar_ingrediente(self, ingrediente):
        
        if ingrediente in self.__ingredientes:
            
            self.__ingredientes.remove(ingrediente)
    
    
    def mostrar_informacion(self):
        
        return (f'Ingredientes: {self.__ingredientes}, tamaño de la pizza, {self.tamanho}')
    

pizza1 = Pizza('mediana')

pizza1.agregar_ingrediente('jamon')
print(pizza1.mostrar_informacion())

pizza1.quitar_ingrediente('oregano')
print(pizza1.mostrar_informacion())

