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
        print("Estoy dando permiso")
        return self.__dni
    
    def validarNIF(self, nif):
        letra_nif = nif[-1:].upper()
        dni = int(nif[0:8])
        letra = dni % 23
        comprobacion = "TRWAGMYFPDXBNJZSQVHLCKE"
        
        if comprobacion[letra] == letra_nif:
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
    
    def esMayorDeEdad(self):
        if self.__edad >= 18:
            return "Es mayor de edad"
        else:
            return "Es menor de edad"    
            
            


persona1 = Persona()
persona1.nombre = 'Bladimir'
persona1.edad = 24
persona1.dni = '78848952F'
print(persona1.mostrar())
print(persona1.esMayorDeEdad())