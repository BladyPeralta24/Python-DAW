from clase_contacto import Contacto

class Agenda():
    
    def __init__(self):
        
        self.agenda = {}
    
    
    def anhadir_contacto(self):
        """ Solicitar todos los datos del contacto y lo añade a tu gestion """
        
        nombre = input("Introduce el nombre del contacto: ")
        primer_apellido = input("Introduce el primer apellido del contacto: ")
        segundo_apellido = input("Introduce el segundo apellido del contacto: ")
        edad = int(input('Introduce la edad de la persona: '))
        nif = input('Introduce el dni de la persona: ')
        direccion = input('Introduce la direccion del contacto: ')
        telefono_fijo = input('Introduce un telefono fijo para el contacto:' )
        telefono_movil = input('Introduce un telefono movíl para el contacto: ')
        email = input('Introduce en E-mail para el contacto: ')
        
        while nombre in self.agenda:
            print("El contacto, ya existe en la agenda\n")
            nombre = input("Introduce el nombre del contacto: ")
            
        nuevo_contacto = Contacto(nombre, primer_apellido, segundo_apellido, edad, nif, direccion, telefono_fijo, telefono_movil, email)
        
        self.agenda = {nombre: nuevo_contacto}
        
    def lista_contacto(self):
        """ Contactos ordenados por su nombre alfabéticamente """
        lista_ordenada = sorted(self.agenda.items())
        
        for nombre, contacto in lista_ordenada:
            print(contacto.nombre, contacto)
    
    def buscar_contacto(self):
        """ Buscar contactos por cualquiera de sus parámetros """
        
        busqueda = input("Introduce el valor del campo a buscar: ")
        
        encontrado = {}
        
        for nombre, contacto in self.agenda.items():
            
            if busqueda in nombre:
                encontrado[nombre] = contacto
                
            if busqueda in contacto.primer_apellido:
                encontrado[nombre] = contacto
                
            if busqueda in contacto.nif:
                encontrado[nombre] = contacto
                
            if busqueda in contacto.email:
                encontrado[nombre] = contacto
                
            if busqueda in contacto.segundo_apellido:
                encontrado[nombre] = contacto
                
            if busqueda in contacto.edad:
                encontrado[nombre] = contacto
                
            if busqueda in contacto.direccion:
                encontrado[nombre] = contacto
                
            if busqueda in contacto.telefono_fijo:
                encontrado[nombre] = contacto
                
            if busqueda in contacto.telefono_movil:
                encontrado[nombre] = contacto
                
            
            return encontrado
    
    def editar_contacto(self):
        """ Gestionar un menú para editar los parámetros del contacto, cualquiera de ellas """
        
        contacto_a_editar = input("Introduce el valor del contacto a editar: ")
        
        while not(contacto_a_editar in self.agenda):
            print('El contacto, no esta en la agenda.\n')
            contacto_a_editar = input('Introduzca el valor del contacto a editar: ')
            
        campo_a_editar = input("Introduzca el valor del campo a editar:\n[N] editar nombre\n[A]Editar primer apellido\n[E]Editar Email\n[SA] Editar segundo apellido\n[TF] Editar telefono fijo\n[TM] Editar telefono móvil\n[D] Editar direccion\n: ")
        while not(campo_a_editar in ['N', 'A', 'E']):
            print('El campo no se encuentra disponible.')
            campo_a_editar = input("Introduzca el valor del campo a editar:\n[N] editar nombre\n[A]Editar primer apellido\n[E]Editar Email")

        contacto_seleccionado = self.agenda[contacto_a_editar]
        
        if campo_a_editar == 'N':
            contacto_seleccionado.nombre = input('Introduce el nombre del contacto: ')
            
        if campo_a_editar == 'A':
            contacto_seleccionado.primer_apellido = input('Introduce el primer apellido del contacto: ')
            
        if campo_a_editar == 'E':
            contacto_seleccionado.email = input('Introduce el email del contacto: ')
    
    
    
# print(""" -- Menú de Agenda --
# Elija una de estas opciones:
# ***********************************
# * 1. Añadir contacto              *
# * 2. Lista de contactos           *
# * 3. Busqueda de contacto         *
# * 4. Editar contacto              *
# ***********************************      
#       
# """)

agenda = Agenda()

agenda.anhadir_contacto()

print(agenda.editar_contacto())