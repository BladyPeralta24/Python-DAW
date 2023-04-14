import re


# Crea la expresión regular para validar un email. 
# El email estará construido por:
# texto + @ + texto + . (un punto) + texto (máximo 3 caracteres).


def validar_email (correo):
    emailValido = False
    
    if not re.findall('.+[@].+\..[a-z]{1,2}$', correo):
        return emailValido
    else:
        return not emailValido


# prueba de correo: bladimir.peralta@iescesarmanrique.es
print(validar_email("bladimir.peralta@iescesarmanrique.es"))


#print(re.findall('.+[@].+\..[a-z]{1,2}$', "bladimir.peralta@iescesarmanrique.com"))