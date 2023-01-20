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
            return "Es legal"
        else:
            return "No es legal"    
            
            


persona1 = Persona()
persona1.nombre = 'Bladimir'
persona1.edad = 24
persona1.dni = '78848952F'
#print(persona1.mostrar())
#print(persona1.esMayorDeEdad())







# ejercicio hecho por el profesor.

# from documento import Documento

# class Persona():
    
#     def __init__(self, nombre: str = '', edad: int = 18, nif: str = ''):
#         self.nombre = nombre
#         self.edad   = edad
#         self.nif    = nif
        
        
        
#     @property
#     def nif(self):
#         return "NIF: " + self.__nif
    
    
#     @nif.setter
#     def nif(self, nuevo_valor):
        
#         doc = Documento()
        
#         if doc.nif_valido(nuevo_valor):
#             self.__nif = nuevo_valor
#         else:
#             print("[ERROR] el NIF insertado no es válido")
#             exit()
    
#     @property
#     def edad(self):
#         return self.__edad
    
#     @edad.setter
#     def edad(self, nuevo_valor):
        
#         if isinstance(nuevo_valor, int) and nuevo_valor >= 0 and nuevo_valor <= 120:
#             self.__edad = nuevo_valor
#         else:
#             print("[ERROR] la edad insertada no es válido")
#             exit()
            
            
#     def mostrar(self):
#         return f"Nombre: {self.nombre} Edad: {self.__edad} {self.nif} "
    
    
#     def es_mayor_de_edad(self):       
#         return self.__edad >= 18
    
# andres = Persona("Andrés",22,"78551004R")

# print(andres.mostrar())


# #print(andres.nif)



# meter esta clase en otro documento
# class Documento():
    
#     def __init__(self) -> None:
#         pass


#     def nif_valido(self, nif):
#         letrasDNI = 'TRWAGMYFPDXBNJZSQVHLCKE'
#         if len(nif) == 9:
#             dni = nif[0:-1]
#             if dni.isnumeric():
#                 posLetra = int(dni)%23
#                 if nif[-1].upper() == letrasDNI[posLetra]:
#                     return True

#         return False    