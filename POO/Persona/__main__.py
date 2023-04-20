

from persona import Persona

opciones = """
###################################################################################
#Bienvenidos a la gestión de Personas, pulse la tecla que desee para continuar:   #
#                                                                                 #
#[I]nsertar Personas                                                              #
#[B]uscar Personas                                                                #
#[S]alir del Programa                                                             #
###################################################################################
"""


opcion = input(opciones)


while opcion.upper() != 'S':
    
    if opcion.upper() == 'I':
    
        persona = Persona()
        
        
        persona_finalizada = False
        
        while not persona_finalizada:
        
            try:
                
                
                if not persona.nombre:
                    persona.nombre = input("Inserte un nombre válido para la persona: ")
                
                if not persona.apellido1:
                    persona.apellido1 = input(f"Inserte el primer apellido de {persona.nombre}: ")
                
                if not persona.apellido2:
                    persona.apellido2 = input(f"Inserte el segundo apellido de {persona.nombre}: ")
                    
                if not persona.nif:
                    persona.nif = input(f"Inserte el NIF de {persona.nombre}: ")
                
                if not persona.email:
                    persona.email = input(f"Inserte el E-mail de {persona.nombre}: ")
                    
                if not persona.direccion:
                    persona.direccion = input(f"Inserta la dirección de {persona.nombre}: ")
                    
                if not persona.codigo_postal:
                    persona.codigo_postal = input(f"Inserta la código postal de {persona.nombre}: ")
                    
                    
                print("Datos insertados correctamente.")    
                persona.guardar()
                
                persona_finalizada = True
                
            except Exception as err:    
                print(err.args[1], end="")
    
    
    
    elif opcion.upper() == 'B':
        
        # parametro = input("Introduce un parámetro para localizar a la persona: ")
        
        # encontrados = Persona.buscar(parametro)
        # print(encontrados)
        pass
        
        
    
    opcion = input(opciones)