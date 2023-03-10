from clase_contacto import Contacto

"""crear funciones de validar nif y email para la clase"""

def validarNIF (nif: str):
    ValidarNIF = 'TRWAGMYFPDXBNJZSQVHLCKE'
    nif = nif.upper()
    if not nif[0:-1].isnumeric():
        return ("Has introducido mal el NIF. Por favor introduce de nuevo el NIF: ")
        
    dni = int(nif[0:-1])
    
    posLetra = dni % 23
    if ValidarNIF[posLetra] == nif[-1]:
        return True
    else:
        return False


def validarEmail(correo):
    posArroba = int(0)
    emailValido = False
    
    if not emailValido:
        if correo.find("@") > 0:
            posArroba = correo.find("@")
            if correo.find(".", posArroba, -1) < (len(correo) -1) and correo.find(".", posArroba, -1) > posArroba and 1 < correo.find(".", posArroba, -1) - posArroba:
                emailValido = True
    
    return emailValido






class Agenda():
    
    def __init__(self):
        
        self.agenda = {}
    
    
    def anhadir_contacto(self):
        """ Solicitar todos los datos del contacto y lo añade a tu gestion """
        
        nombre = input("Introduce el nombre del contacto: ")
        Contacto.nombre = nombre
        
        primer_apellido = input("Introduce el primer apellido del contacto: ")
        Contacto.primer_apellido = primer_apellido
        
        segundo_apellido = input("Introduce el segundo apellido del contacto: ")
        Contacto.segundo_apellido = segundo_apellido
        
        edad = int(input('Introduce la edad de la persona: '))
        Contacto.edad = edad
        
        nif = input('Introduce el dni de la persona: ')
        while not validarNIF(nif):
            nif = input("Introduce un NIF válido")
        Contacto.nif = nif
        
        direccion = input('Introduce la direccion del contacto: ')
        Contacto.direccion = direccion
        
        telefono_fijo = input('Introduce un telefono fijo para el contacto: ' )
        Contacto.telefono_fijo = telefono_fijo
        
        telefono_movil = input('Introduce un telefono movíl para el contacto: ')
        Contacto.telefono_movil = telefono_movil
        
        email = input('Introduce en E-mail para el contacto: ')
        while not validarEmail(email):
            email = input("Introduce un email válido: ")
        Contacto.email = email
        
        while nombre in self.agenda:
            print("El contacto, ya existe en la agenda\n")
            nombre = input("Introduce el nombre del contacto: ")
        
            
        nuevo_contacto = Contacto(nombre, primer_apellido, segundo_apellido, edad, nif, direccion, telefono_fijo, telefono_movil, email)
        
        self.agenda.setdefault(nuevo_contacto.nombre, nuevo_contacto)
        
    def lista_contacto(self):
        """ Contactos ordenados por su nombre alfabéticamente """
        print("Lista de contactos ordenada alfabeticamente:\n")
        lista_ordenada = sorted(self.agenda.items())
        
        for nombre, nuevo_contacto in lista_ordenada:
            print(nuevo_contacto.nombre, nuevo_contacto)
    
    def buscar_contacto(self):
        """ Buscar contactos por cualquiera de sus parámetros """
        parametro = input("Introduce un parametro del usuario que deseas buscar: ")
        for nombre, Contacto in self.agenda.items():
            if parametro in Contacto.nombre:
                print (Contacto.nombre, Contacto)
            
            if parametro in Contacto.primer_apellido:
                print (nombre, Contacto)
            
            if parametro in Contacto.segundo_apellido:
                print (nombre, Contacto)
            
            if parametro in str(Contacto.edad):
                print (nombre, Contacto)
            
            if parametro in Contacto.direccion:
                print (nombre, Contacto)
            
            if parametro in Contacto.telefono_fijo:
                print (nombre, Contacto)
            
            if parametro in Contacto.telefono_movil:
                print (nombre, Contacto)
            
            if parametro in Contacto.nif:
                print (nombre, Contacto)
            
            if parametro in Contacto.email:
                print (nombre, Contacto)
        
    
    def editar_contacto(self):
        """ Gestionar un menú para editar los parámetros del contacto, cualquiera de ellas """
        
        contacto_editar = input("Introduce el nombre del contacto que quieras editar: ")
        if contacto_editar in self.agenda.keys():
            clave = input("Elije la opcion a editar: Nombre - Primer apellido - Segundo Apellido - Edad - NIF - Direccion - Telefono fijo - Telefono movil - Email\n: ")
            if clave.lower() == 'nombre' or clave.lower() == "Primer apellido" or clave.lower() == "Segundo apellido" or clave.lower() == "edad" or clave.lower() == "nif" or clave.lower() == "direccion" or clave.lower() == "telefono fijo" or clave.lower() == "telefono movil" or clave.lower() == "email":
                
                nuevo_valor = input("Introduce el valor del campo: ")

                for nombre, contacto in self.agenda.items():
                    if contacto_editar == nombre:
                        
                        if clave.lower() == "nombre":
                            contacto.nombre = nuevo_valor

                        if clave.lower() == "primer apellido":
                            contacto.primer_apellido = nuevo_valor

                        if clave.lower() == "Segundo apellido":
                            contacto.segundo_apellido = nuevo_valor

                        if clave.lower() == "nif":
                            while not validarNIF(nuevo_valor):
                                clave = input("Introduzca un NIF valido: ")
                            contacto.nif = nuevo_valor

                        if clave.lower() == "email":
                            while not validarEmail(nuevo_valor):
                                clave = input("Introduzca un Email válido: ")
                            contacto.email = nuevo_valor

                        if clave.lower() == "edad":
                            contacto.edad = int(nuevo_valor)

                        if clave.lower() == "direccion":
                            contacto.direccion = nuevo_valor

                        if clave.lower() == "telefono fijo":
                            contacto.telefono_fijo = nuevo_valor

                        if clave.lower() == "telefono movil":
                            contacto.telefono_movil = nuevo_valor
                            
                print ("El contacto se ha actualizado correctamente.\n")
            else:
                
                print('Error. Este campo no existe.\n')
        else:
            print('Error, este contacto no existe.\n')
    
    
    
agenda = Agenda()


opcion = ""

while opcion != 5:
    
    print("""
+--------- Menú de Agenda --------+
***********************************
* 1. Añadir contacto              *
* 2. Lista de contactos           *
* 3. Busqueda de contacto         *
* 4. Editar contacto              *
* 5. Salir                        *
***********************************
+---------------------------------+        
""")
    opcion = int(input('Elije la opcion que deseas realizar: '))
    
    if opcion == 1:
        agenda.anhadir_contacto()
    
    if opcion == 2:
        print(agenda.lista_contacto())
        
    if opcion == 3:
        print(agenda.buscar_contacto())
        
    if opcion == 4:
        agenda.editar_contacto()
        
print("\nFin del Programa. Hasta luego\n")