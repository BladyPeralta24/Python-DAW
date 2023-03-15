""" 
Agenda de contactos [Evaluación]
Crea una clase llamada Persona, que tenga las siguientes atributos:
Nombre
Primer apellido
Segundo apellido
NIF
Edad

Luego crea una clase Contacto, que herede de Persona y añada las siguientes caraceterísticas:
Dirección
Teléfono Fijo
Teléfono Móvil
E-mail

Por último, realizar una clase Agenda la cuál deberá mostrar un menú con las siguientes opciones.
Añadir contacto: Te solicita todos los datos del contacto y lo añade a tu gestión.
Lista de contactos: Contactos ordenados por su nombre alfabéticamente.
Buscar contacto:  Busca contactos por cualquiera de sus parámetros.
Editar contacto: Tendrás que gestionar un menú para editar los parámetros de tu contacto, cualquiera de ellos. 

"""

from validacion import Validacion

class Persona():
    
    def __init__(self, nombre, apellido1, apellido2, nif, edad):
        self.nombre    = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.__nif     = nif
        self.__edad    = edad
        
        
    @property
    def nif(self):
        return self.__nif
    
    
    @nif.setter
    def nif(self, nuevo_nif):
        if self.validar_nif(nuevo_nif):
            self.__nif = nuevo_nif
        else:
            print("[Error] se ha introducido un nif no válido")
            exit

    @staticmethod            
    def validar_nif(nif):
        return Validacion.nif(nif)
    
    
    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, nuevo_edad):
        if self.validar_edad(nuevo_edad):
            self.__edad = nuevo_edad
        else:
            print("[Error] se ha introducido una edad no válida")
            exit
            
    @staticmethod            
    def validar_edad(edad):
        return Validacion.edad(edad)