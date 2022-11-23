## Preguntar al usuario el nombre completo en la consola y mostrar por pantalla ##
## el nombre completo del usuario tres veces: ##
## Una con todas las letras minúsculas ##
## Otra con todas las letras mayúsculas y  ##
## Otra solo con la primera letra del nombre y de los apellidos en mayúscula. ##
## NOTA: El usuario puede introducir su nombre combinando mayusculas y minusculas como quiera ##

#nombre = input("Introduce tu nombre por pantalla: ")
#apellido1 = input("Introduce tu primer apellido: ")
#apellido2 = input("Introduce tu segundo apellido: ")
#print(nombre.lower() + " " + apellido1.lower() + " "+ apellido2.lower())
#print(nombre.upper() + " " + apellido1.upper() + " " + apellido2.upper())
#print(nombre[0].upper() + "" + nombre[1:].lower() + " " + apellido1[0].upper() + "" + apellido1[1:].lower() + " " + apellido2[0].upper() + "" + apellido2[1:].lower())
#print(nombre.capitalize()+ " " + apellido1.capitalize() + " " + apellido2.capitalize())

continuar = False
while not continuar:
    nombre_completo = input("Introduce tu nombre completo: ")
    
    nombre_mayuscula = nombre_completo.upper().strip()
    nombre_minuscula = nombre_completo.lower().strip()
    nombre_completo = nombre_completo.lower().strip()
    
    print(nombre_mayuscula)
    print(nombre_minuscula)
    
    posEspacio = 0
    
    while nombre_completo.find(" ", posEspacio) >= 0:
        posEspacio = nombre_completo.find(" ", posEspacio + 1)
        nombre_completo = nombre_completo[0:posEspacio+1] + nombre_completo[posEspacio + 1].upper() + nombre_completo[posEspacio+2:]
        
    print(nombre_completo)
    salir = input("¿Deseas continuar? (S/N): ")
    if  salir == "n" or  salir == "N":
        continuar = True
    elif salir == "s" or salir == "S":
        print("Continuamos con el programa")

print("Fin del programa")

#nombre = input("Inserte un nombre y apellidos: ")
#nombre = nombre.lower().strip()
#posEspacio = 0
#
#while nombre.find(" ", posEspacio) >= 0:
#    
#    posEspacio = nombre.find(" ", posEspacio + 1)
#
#    nombre = nombre[0:posEspacio+1] + nombre[posEspacio + 1].upper() + nombre[posEspacio+2:]
#    
#print(nombre)