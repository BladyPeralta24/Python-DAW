class Persona():
    def __init__(self, nombre = "", edad = "", dni = ""):
        self.nombre = nombre
        self.__edad = edad
        self.__dni = dni
        
    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, nuevo_valor):
        if isinstance(nuevo_valor, int):
            self.__edad = nuevo_valor
        else:
            print("El formato de la edad, no es válido")
        
    @property
    def dni(self):
        return self.__dni
    
    def validarNIF(self, nif):
        comprobacion = "TRWAGMYFPDXBNJZSQVHLCKE"
        letra = nif[-1:].upper()
        dni = int(nif[0:8])
        letra = dni % 23
        
        if comprobacion[letra] == letra:
            return True
        else:
            return False

    @dni.setter
    def dni(self, nuevo_valor):
        if self.validarNIF(nuevo_valor):
            self.__dni = nuevo_valor
        else:
            print("El formato del dni no es válido")
            
    def mostrar(self):
        return f'Nombre: {self.nombre}, edad: {self.__edad}, dni: {self.__dni}'
            
            

persona1 = Persona('Junior', 22, '78819396G')
print(persona1.mostrar())