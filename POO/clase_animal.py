class Animal():
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nuevo_valor):
        if isinstance(nuevo_valor, str):
            self.__nombre = nuevo_valor
        else:
            print("ERROR. El valor del nombre no es valido")
            
    @property
    def especie(self):
        return self.__especie
    @especie.setter
    def especie(self, nuevo_valor):
        if isinstance(nuevo_valor, str):
            self.__especie = nuevo_valor
        else:
            print("ERROR. El valor de la especie no es valido")
            
    @property
    def edad(self):
        return self.__edad
    @edad.setter
    def edad(self, nuevo_valor):
        if isinstance(nuevo_valor, int):
            self.__edad = nuevo_valor
        else:
            print("ERROR. El valor de la edad no es valido")
            
    def comunicarse(self):
        if self.__edad > 1:
            return f'El/La {self.__nombre} se está comunicando'
        else:
            return f'El/La {self.__nombre} es un recien nacido'
        
        
    def mostrar(self):
        return f'Nombre: {self.__nombre}\nEspecie: {self.__especie}\nEdad: {str(self.__edad)}'
        
        
    
    
class Ave(Animal):
    def __init__(self, nombre, especie, edad, alas):
        super().__init__(nombre, especie, edad)
        self.alas = alas
        
    @property
    def alas(self):
        return self.__alas
    @alas.setter
    def alas(self, nuevo_valor):
        if isinstance(nuevo_valor, int):
            self.__alas = nuevo_valor
        else:
            print("ERROR. El valor de las alas no es valido\n")
            
    def volar(self):
        if self.__alas == 2:
            return f'El/La {self.nombre} esta volando'
        else:
            return f'El/La {self.nombre} no está volando. Es un recien nacido'
    def mostrar(self):
        return super().mostrar()+'\nAlas: '+ str(self.__alas)
    
    
class Pajaro(Ave):
    
    def __init__(self, nombre, especie, edad, alas, pico):
        super().__init__(nombre, especie, edad, alas)
        self.pico = pico
        
    @property
    def pico(self):
        return self.__pico
    @pico.setter
    def pico(self, nuevo_valor):
        if isinstance(nuevo_valor, bool):
            self.__pico = nuevo_valor
        else:
            print("ERROR. El valor del pico no es valido")
            
    def picotear(self):
        if self.__pico == True:
            return f'El/La {self.nombre} está picoteando'
        else:
            return f'El/La {self.nombre} pajaro no está picoteando'
        
    def mostrar(self):
        return super().mostrar() +'\nPico: '+ str(self.__pico)+'\n'
    







golondrina = Pajaro('Golondrina', 'Hirundo', 2, 2, True)

print(golondrina.mostrar())
print(golondrina.comunicarse())
print(golondrina.volar())
print(golondrina.picotear()+'\n')

ruisenior = Pajaro('Ruiseñor', 'Luscinia', 3, 1, False)

print(ruisenior.mostrar())
print(ruisenior.comunicarse())
print(ruisenior.volar())
print(ruisenior.picotear()+'\n')

canario = Pajaro('Canario', 'Serinus canaria', 0, 0, False)

print(canario.mostrar())
print(canario.comunicarse())
print(canario.volar())
print(canario.picotear()+'\n')