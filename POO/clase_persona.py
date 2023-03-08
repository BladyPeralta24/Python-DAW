class Persona():
    
    def __init__(self, nombre, primer_apellido, segundo_apellido, edad: int, nif):
        
        self.nombre = nombre
        self.primer_apellido = primer_apellido
        self.segundo_apellido = segundo_apellido
        self.edad = edad
        self.nif = nif
        
        
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo_valor):
        if isinstance(nuevo_valor, str):
            self.__nombre = nuevo_valor
        else:
            print("ERROR. El valor del nombre no es válido")
            exit
            
    @property
    def primer_apellido(self):
        return self.__primer_apellido
    
    @primer_apellido.setter
    def primer_apellido(self, nuevo_valor):
        if isinstance(nuevo_valor, str):
            self.__primer_apellido = nuevo_valor
        else:
            print("ERROR. El valor del primer apellido no es válido")
            exit
            
            
    @property
    def segundo_apellido(self):
        return self.__segundo_apellido
    
    @segundo_apellido.setter
    def segundo_apellido(self, nuevo_valor):
        if isinstance(nuevo_valor, str):
            self.__segundo_apellido = nuevo_valor
        else:
            print("ERROR. El valor del segundo apellido no es válido")
            exit
            
    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, nuevo_valor):
        if isinstance(nuevo_valor, int) and nuevo_valor >= 0 and nuevo_valor <= 150:
            self.__edad = nuevo_valor
        else:
            print("ERROR. El valor de la edad no es válido\n")
            exit
            
            
    @property
    def nif(self):
        return self.__nif
    
    def validarNIF(self, dni_nif):
        letra_nif = dni_nif[-1:].upper()
        dni = int(dni_nif[0:8])
        letra = dni % 23
        comprobacion = "TRWAGMYFPDXBNJZSQVHLCKE"
        
        if comprobacion[letra] == letra_nif:
            return True
        else:
            return False
    
    @nif.setter
    def nif(self, nuevo_valor):
        if self.validarNIF(nuevo_valor):
            self.__nif = nuevo_valor
        else:
            print("El formato del dni no es válido\n\n")
            exit
            
            
            
            
            
    def __str__(self):
        return f'Nombre: {self.__nombre}\nPrimer Apellido: {self.__primer_apellido}\nSegundo apellido: {self.__segundo_apellido}\nEdad: {self.__edad}\nNIF: {self.__nif}'
            
            
            
# prueba = Persona('Manuel', 'Vargas', 'Sosa', 24, '78848952F')

# print(prueba.nif)






    