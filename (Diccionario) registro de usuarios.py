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
        
    
    