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


usuario = {}
nif = {}
while True:
    nombre = input("Introduce tu nombre: ")
    apellidos = input("Introduce tus apellidos: ")
    nif = input("introduce tu DNI: ")
    direccion = input("Introduce tu dirección: ")
    mail = input("Introduce tu e-mail: ")
    telefono = input("Introduce tu numero de teléfono: ")
    
    nif = nif.fromkeys(['nombre','apellidos','direccion','email','telefono'],"")
    
    usuario = usuario.fromkeys(nif, {})
    
    print(usuario)
    
    