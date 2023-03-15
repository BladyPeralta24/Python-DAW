""" 
Luego crea una clase Contacto, que herede de Persona y añada las siguientes caraceterísticas:
Dirección
Teléfono Fijo
Teléfono Móvil
E-mail
"""


from persona import Persona
from validacion import Validacion


class Contacto(Persona):
    
    def __init__(self, nombre='', apellido1='', apellido2='', nif='', edad=0, direccion='', telefono_fijo='', telefono_movil='', email=''):
        super().__init__(nombre, apellido1, apellido2, nif, edad)
        
        self.direccion        = direccion
        self.__telefono_fijo  = telefono_fijo
        self.__telefono_movil = telefono_movil
        self.__email          = email
        
    @property
    def telefono_fijo(self):
        return self.__telefono_fijo
    
    @telefono_fijo.setter
    def telefono_fijo(self, nuevo_telefono_fijo):
        if self.validar_telefono_fijo(nuevo_telefono_fijo):
            self.__telefono_fijo = nuevo_telefono_fijo
        else:
            print("[Error] se ha introducido un Telefono Fijo no válido")
            exit
            
    @staticmethod            
    def validar_telefono_fijo(telefono_fijo : str):
        return Validacion.telefono(telefono_fijo) and telefono_fijo[0] in ("8","9")
    
    
    @property
    def telefono_movil(self):
        return self.__telefono_movil
    
    @telefono_movil.setter
    def telefono_movil(self, nuevo_telefono_movil):
        if self.validar_telefono_movil(nuevo_telefono_movil):
            self.__telefono_movil = nuevo_telefono_movil
        else:
            print("[Error] se ha introducido un Telefono movil no válido")
            exit
            
    @staticmethod            
    def validar_telefono_movil(telefono_movil : str):
        return Validacion.telefono(telefono_movil) and telefono_movil[0] in ("6","7")
    
    
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, nuevo_email):
        if self.validar_email(nuevo_email):
            self.__email = nuevo_email
        else:
            print("[Error] se ha introducido un E-mail no válido")
            exit
            
    @staticmethod            
    def validar_email(email : str):
        return Validacion.email(email)
    
    
    def __repr__(self):
        return self.nombre + ' '+ self.apellido1 + ' ' + self.apellido2
    
    
    def datos(self):
        return self.nombre + ' '+ self.apellido1 + ' ' + self.apellido2 + ' ' + self.nif + ' ' + self.edad + ' ' + self.direccion + ' ' + self.telefono_fijo  + ' ' + self.telefono_movil + ' ' + self.email
        
    
#contacto = Contacto("Andrés", "Calamaro", "","78551004R", 22,"asfdasfd", "919919919", "626626626", "andres@gmail.com")



#print(contacto)