# Crea un programa que solicite los datos de una Persona: Nombre, apellido1, apellido2, email, nif, dirección, código postal.

# La gestión de estos datos, la debe realizar de la forma más acorde posible a los conceptos que has aprendido hasta ahora.

# Cada persona creada, deberá guardar un registro en un fichero llamado personas.txt

# Modifica el programa anterior, para poder buscar a una persona por alguno de sus datos y mostrarlos en pantalla.
import re

class Persona():
    def __init__(self):
        self.nombre         = ""
        self.apellido1      = ""
        self.apellido2      = ""
        self.__email        = ""
        self.__nif          = ""
        self.direccion      = ""
        self.codigo_postal  = ""
        
    @property
    def email(self):
        return self.__email
    
    def validar_email(self, correo):
        
        emailValido = False

        if not re.findall('.+[@].+\..[a-z]{1,2}$', correo):
            return emailValido
        else:
            return not emailValido
    
    @email.setter
    def email(self, nuevo_valor):
        if self.validar_email(nuevo_valor):
            self.__email = nuevo_valor
        else:
            raise ValueError("Error. E-mail no valido")
            
    @property
    def nif(self):
        return self.__nif
    
    def validar_nif(self, nif):
        letra_nif = nif[-1:].upper()
        dni = int(nif[0:8])
        letra = dni % 23
        comprobacion = "TRWAGMYFPDXBNJZSQVHLCKE"
        
        if comprobacion[letra] == letra_nif:
            return True
        else:
            return False
    
    @nif.setter
    def nif(self, nuevo_valor):
        if self.validar_nif(nuevo_valor):
            self.__nif = nuevo_valor
        else:
            raise ValueError("ERROR. NIF no valido")
            
            
    # def __str__(self):
    #     """Para comporbar que los datos esten funcionando"""
    #     return f"{self.nombre}\n{self.apellido1}\n{self.apellido2}\n{self.__email}\n{self.__nif}\n{self.direccion}\n{self.codigo_postal}"
    
    
persona1 = Persona()
menu = False

while not menu:
    nombre = input("introduce tu nombre: ")
    persona1.nombre = nombre
    
    apellido1 = input("Introduce el primer apellido: ")
    persona1.apellido1 = apellido1
    
    apellido2 = input("Introduce el segundo apellido: ")
    persona1.apellido2 = apellido2
    
    email = input("Introduce tu correo electronico: ")
    persona1.email = email
    
    nif = input("Introduce tu DNI: ")
    persona1.nif = nif
    
    direccion = input("Introduce una direccion: ")
    persona1.direccion = direccion
    
    codigo_postal = input("Introduce un codigo postal: ")
    persona1.codigo_postal = codigo_postal
    
    
    menu = input("Desaeas continuar introduciendo mas datos(s/n): ")
    if menu == "s":
        menu = False
    elif menu == "n":
        menu = True
        


"""En esta parte se tiene que poner la ruta donde guardar el fichero persona.txt"""
fichero = open("/home/bladimir/Escritorio/persona.txt", mode="a")

fichero.writelines(["\nNombre: ", persona1.nombre, "\nApellidos: ", persona1.apellido1," ",persona1.apellido2, "\nEmail: ", persona1.email, "\nNIF: ", persona1.email, "\nDireccion: ", persona1.direccion, "\nCodigo Postal: ", persona1.codigo_postal, "\n"])

fichero.close()
    
    
    
    
    
# persona1 = Persona("Bladimir", "Peralta", "Herrera", "bperaltaherrera@gmail.com", "78848952F", "Calle los dolores, 24", "35500")
# persona2 = Persona("Maria", "De la O", "Riquelme", "mariadelaoriquelme@hotmail.com", "78836163Y", "Calle mondongo, 03", "25024")




# fichero = open("/home/bladimir/Escritorio/persona.txt", mode="a")

# fichero.writelines(["\nNombre: ", persona1.nombre, "\nApellidos: ", persona1.apellido1," ",persona1.apellido2, "\nEmail: ", persona1.email, "\nNIF: ", persona1.email, "\nDireccion: ", persona1.direccion, "\nCodigo Postal: ", persona1.codigo_postal, "\n"])
# fichero.writelines(["\nNombre: ", persona2.nombre, "\nApellidos: ", persona2.apellido1," ",persona2.apellido2, "\nEmail: ", persona2.email, "\nNIF: ", persona2.email, "\nDireccion: ", persona2.direccion, "\nCodigo Postal: ", persona2.codigo_postal, "\n"])

# fichero.close()





