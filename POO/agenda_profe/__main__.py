

from agenda import Agenda
from contacto import Contacto


agenda = Agenda()

texto_bienvenida = """ 
    
    Bienvendios a tu Agenda,
    especifica que opción desea realizar:
    
    [A]ñadir un contacto
    [L]istar la Agenda de Contactos
    [B]uscar contacto por parámetro
    [E]ditar un contacto
    [S]alir del programa               
"""

opcion = input(texto_bienvenida)

while opcion != 'S':
    if opcion == 'A':
        
        nuevo_contacto = Contacto()
        
        nuevo_contacto.nombre = input("Introduce un nombre: ")
        nuevo_contacto.apellido1 = input("Introduce el primer apellido: ")
        nuevo_contacto.apellido2 = input("Introduce el segundo apellido: ")
        
        #Validación NIF
        nif = input("Introduce un NIF válido: ")
        while not nuevo_contacto.validar_nif(nif):
            nif = input("Error en el NIF, introduce un NIF válido: ")
        nuevo_contacto.nif = nif
        
        #Validación EDAD
        edad = input("Introduce una edad válido: ")
        while not nuevo_contacto.validar_edad(edad):
            edad = input("Error en la edad, introduce una edad válida: ")
        nuevo_contacto.edad = edad
        
        nuevo_contacto.direccion = input("Introduce la dirección del contacto: ")
        
        #Validación Teléfono Fijo
        telefono_fijo = input("Introduce un Teléfono Fijo válido: ")
        while not nuevo_contacto.validar_telefono_fijo(telefono_fijo):
            telefono_fijo = input("Error en el Teléfono Fijo, introduce un Teléfono Fijo válido: ")
        nuevo_contacto.telefono_fijo = telefono_fijo
        
        #Validación Teléfono Móvil
        telefono_movil = input("Introduce un Teléfono Móvil válido: ")
        while not nuevo_contacto.validar_telefono_movil(telefono_movil):
            telefono_movil = input("Error en el Teléfono Móvil, introduce un Teléfono Móvil válido: ")
        nuevo_contacto.telefono_movil = telefono_movil
        
        #Validación E-mail
        email = input("Introduce un E-mail válido: ")
        while not nuevo_contacto.validar_email(email):
            email = input("Error en el E-mail, introduce un E-mail válido: ")
        nuevo_contacto.email = email
        
        
        agenda.anhadir_contacto(nuevo_contacto)
    
    elif opcion == 'L':
        
        lista_contactos = agenda.listado_contactos()    
        
        i = 1
        for contacto in lista_contactos:
            print(f"#{str(i)} " + str(contacto) + "\n")
            i += 1
    
    
    elif opcion == 'B':
        parametro = input("Introduce un parámetro para localizar a un contacto")
        encontrados = agenda.buscar_contacto(parametro)
        print(encontrados)
        
    elif opcion == 'E':
        
        nif = input("Introduce el NIF del contacto a Editar")
        
        opcion_a_editar = input("""
            Indica que opción deseas editar:
            
            1: [N]ombre
            2: [A]pelllido 1
            3: A[P]ellido 2                        
            4: N[I]F 
            5: [E]dad
            6: [D]irección
            7: [T]eléfon Fijo
            8: Te[L]éfono Móvil
            9: E[M]ail                                
        """)
        
        contacto_a_editar = agenda.lista_contactos[nif]
        
        if opcion_a_editar in('1','N'):
            contacto_a_editar.nombre = input("Introduce un nombre nuevo: ")
            
        if opcion_a_editar in('2','A'):
            contacto_a_editar.apellido1 = input("Introduce un primer apellido nuevo: ")
    
    opcion = input(texto_bienvenida)
    