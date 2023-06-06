## Crear dos funciones, una para validar el NIF y otra para validar un email ##

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
    



correo = input("Introduce tu correo electrónico: ")
nif = input("Introduce un NIF válido: ")
print(validar_NIF(nif))
print(validar_email(correo))