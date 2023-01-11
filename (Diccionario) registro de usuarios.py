# Cree un programa que registre en una base de datos creada con un diccionario los siguientes parámetros:

# - Nombre de usuario
# - Apellidos
# - Dirección
# - NIF
# - E-mail (puede ser más de uno)
# - Teléfono (puede ser más de uno)

#  Luego, con esa base de datos, permite la búsqueda de usuarios por cualquiera de sus datos. 
#  Una vez localizado muestra toda la información del usuario.

# Realiza la validación del NIF y del E-mail con las funciones anteriores.

# Estructura del Diccionario:#
#usuario = {
#    nif : {
#        "nombre"     : ""
#        "apellidos"  : ""
#        "direccion"  : ""
#        "email"      : ""
#        "telefono"   : ""
#    }
#}
# Luego, con esa base de datos, permite la búsqueda de usuarios por cualquiera de sus datos. Una vez localizado muestra toda la información del usuario.

# Realiza la validación del NIF y del E-mail con las funciones anteriores.

def validar_NIF (nif: str):
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
    

def validar_email (correo):
    posArroba = int(0)
    emailValido = False
    
    if not emailValido:
        if correo.find("@") > 0:
            posArroba = correo.find("@")
            if correo.find(".", posArroba, -1) < (len(correo) -1) and correo.find(".", posArroba, -1) > posArroba and 1 < correo.find(".", posArroba, -1) - posArroba:
                emailValido = True
    
    return emailValido


usuario = {}
salir = False
while not salir:
    listaTelefono = []
    listaEmails = []
    nombre = input("Introduce tu nombre: ")
    
    apellidos = input("Introduce tus apellidos: ")
    
    nif = input("introduce tu DNI: ")
    if not validar_NIF(nif):
        while not validar_NIF(nif):
            nif = input("ERROR. Vuelva a introducir el DNI valido: ")
            
    direccion = input("Introduce tu dirección: ")
    
    email = input("Introduce tu e-mail: ")
    if not validar_email(email):
        while not validar_email(email):
            email = input("ERROR. Vuelva a introducir el email valido: ")
            
    emailExtra = input("¿Desea introducir más emails?(S/N): ")
    while emailExtra == "S" or emailExtra == "s":
        listaEmails.append(email)
        email = input("Introduce otro email: ")
        emailExtra = input("¿Desea introducir más emails?(S/N): ")
    listaEmails.append(email)        
            
            
            
    telefono = input("Introduce tu numero de teléfono: ")
    numeroExtra = input("¿Desea introducir más numero de telefono?(S/N): ")
    while numeroExtra == "S" or numeroExtra == "s":
        listaTelefono.append(telefono)
        telefono = input("Introduce otro numero de telefono: ")
        numeroExtra = input("¿Desea introducir más numero de telefono?(S/N): ")
    listaTelefono.append(telefono)
            
    datos = {
        "nombre"     :  nombre.title()
        ,"apellidos" :  apellidos.title()
        ,"direccion" :  direccion
        ,"email"     :  listaEmails
        ,"telefono"  :  listaTelefono
    }
    usuario[nif.upper()] = datos
    for nif, datos in usuario.items():
        print(nif.upper() ,':', datos, '\n')
        
        
        
    salir = input("¿Deseas continuar?(S/N): ")
    if salir == "S" or salir == "s":
        salir = False
    elif salir == "N" or salir == "n":
        salir = True
        
        
print("Listado final: \n")
print (usuario)




# # Ejercicio hecho por el profesor
# """
# [Diccionario] Registro de usuarios
# Cree un programa que registre en una base de datos creada con un diccionario los siguientes 
# parámetros:

# Nombre de usuario
# Apellidos
# Dirección
# NIF
# E-mail (puede ser más de uno)
# Teléfono (puede ser más de uno)
# Luego, con esa base de datos, permite la búsqueda de usuarios por cualquiera de sus datos. 
# Una vez localizado muestra toda la información del usuario.

# Realiza la validación del NIF y del E-mail con las funciones anteriores.
# """

# ###############################################
# #      Función para validar E-mail            #
# ###############################################
# def email_valido(email):
#    return (email.count("@")==1) and ( email[-3:]==".es" or email[-4:]==".com") and (email.find(".es") > (email.find("@")+1) or  email.find(".com") > email.find("@")+1)
 
# ##########################################
# #      Función para validar NIF          #
# ##########################################
# def nif_valido(nif):
 
#    if len(nif) == 9 and nif != '':
#        letra = nif[-1:].upper()
#        dni = int(nif[0:8])
#        restoLetra = dni % 23
#        comprobacion = "TRWAGMYFPDXBNJZSQVHLCKE"
 
#        return comprobacion[restoLetra] == letra #buscar un elemento en una cadena mediante una posicion

 
#    return False

# ###############################################
# #      Función para validar Teléfono          #
# ###############################################
# def telefono_valido(telefono):
#     return len(telefono)== 9 and telefono.isnumeric()



# #print("Elige la opción adecuada:\n[I] Insertar un nuevo usuario.\n[B] Buscar un elemento en el diccionario.[M] Mostrar el diccionario.[T] Terminar el programa.")



# opcion = ""

# usuarios = {}


# while opcion != 'T':
    
#     if opcion == 'I':
        
#         usuario = {}
        
#         nombre_usuario = input("Inserta el nombre del nuevo usuario: \n")       
#         apellidos = input("Inserta los apellidos de " + nombre_usuario + "\n")
#         direccion = input("Inserta la direccion de " + nombre_usuario + "\n")
        
        
#         nif = input("Inserta el NIF de " + nombre_usuario + "\n")
        
#         while not nif_valido(nif):
#             nif = input("Error al insertar el NIF, inserta el NIF de " + nombre_usuario+ "\n")
        
        
#         email = "1"
        
#         emails = {}
        
#         i = 1
#         while email != '':
            
#             email = input("Inserta E-mail número {}: "+ "\n".format(i))
            
#             if email_valido(email):
#                 emails[i] = email
#                 i += 1
                
                
#         telefono = "1"
#         telefonos = {}
#         i = 1
        
#         while telefono != '':
#             telefono = input("Inserta el telefono número {}: "+ "\n".format(i))
            
#             if telefono_valido(telefono):
#                 telefonos[i] = telefono
#                 i += 1
                
                
#         usuario['nombre'] = nombre_usuario
#         usuario['apellidos'] = apellidos
#         usuario['direccion'] = direccion
#         usuario['nif'] = nif
#         usuario['emails'] = emails
#         usuario['telefonos'] = telefonos
        
                
#         usuarios[nif] = usuario
        
        
#     elif opcion == 'B':
#         palabra_a_buscar = input("Inserta el texto por el cual desea realizar la búsqueda"+ "\n")
        
#         UsuariosEncontrados = {}
#         for nif, usuario in usuarios.items():
            
#             if palabra_a_buscar in nif:
#                 UsuariosEncontrados[nif] = usuario
                
#             for clave, valor in usuario.items():
                
#                 if clave != 'emails' and clave != 'telefonos':
#                     if palabra_a_buscar in valor:
#                         UsuariosEncontrados[nif] = usuario
#                 else:
#                     if clave == 'emails':
#                         for numero_email, email in valor.items():
#                             if palabra_a_buscar in email:
#                                 UsuariosEncontrados[nif] = usuario
#                     else:
#                         for iterador, telefono in valor.items():
#                             if palabra_a_buscar in telefono:
#                                 UsuariosEncontrados[nif] = usuario

                
        
#         print(UsuariosEncontrados)
        
        
#     elif opcion == 'M':
#         print(usuarios)
    
    
    
#     opcion = input("Elige la opción adecuada:\n[I] Insertar un nuevo usuario.\n[B] Buscar un elemento en el diccionario.\n[M] Mostrar el diccionario.\n[T] Terminar el programa.\n")
#     opcion = opcion.upper()
    
    
# print("El programa ha finalizado")








