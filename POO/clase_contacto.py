from clase_persona import Persona

class Contacto(Persona):
    
    def __init__(self, nombre, primer_apellido, segundo_apellido, edad, nif, direccion, telefono_fijo, telefono_movil, email):
        super().__init__(nombre, primer_apellido, segundo_apellido, edad, nif)
        
        self.direccion = direccion
        self.telefono_fijo = telefono_fijo
        self.telefono_movil = telefono_movil
        self.email = email
        
        
    
    @property
    def direccion(self):
        return self.__direccion
    
    @direccion.setter
    def direccion(self, nuevo_valor):
        if isinstance(nuevo_valor, str):
            self.__direccion = nuevo_valor
        else:
            print ("ERROR. El valor de la direccion no es válida\n\n")
            
            
    @property
    def telefono_fijo(self):
        return self.__telefono_fijo
    
    @telefono_fijo.setter
    def telefono_fijo(self, nuevo_valor):
        if isinstance(nuevo_valor, str) and len(nuevo_valor) == 9:
            self.__telefono_fijo = nuevo_valor
        else:
            print ("ERROR. El valor del telefono fijo no es válida\n\n")
            
    
    @property
    def telefono_movil(self):
        return self.__telefono_movil
    
    @telefono_movil.setter
    def telefono_movil(self, nuevo_valor):
        if isinstance(nuevo_valor, str) and len(nuevo_valor) == 9:
            self.__telefono_movil = nuevo_valor
        else:
            print ("ERROR. El valor del telefono móvil no es válida\n\n")
            
    @property
    def email(self):
        return self.__email
    
    def validarEmail(self, correo):
        if correo.find("@") > 0:
            posArroba = correo.find("@")
            if correo.find(".", posArroba, -1) < (len(correo) -1) and correo.find(".", posArroba, -1) > posArroba and 1 < correo.find(".", posArroba, -1) - posArroba:
                return True
    
    @email.setter
    def email(self, nuevo_valor):
        
        if self.validarEmail(nuevo_valor):
            self.__email = nuevo_valor
        else:
            print("ERROR. El valor del e-mail no es válido")
            
            
    
# prueba = Contacto("Manule", "Vargas", "Sosa", 24, "78848952F", "Calle los marmoles, 25", "828782258", "636253080", "manuelvargas@gmail.com")
# print(prueba.email)

