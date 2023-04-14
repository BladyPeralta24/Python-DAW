import re



def validarTelefono(telefono):
    
    telefonoValido = False
    
    if not re.findall("^\+.+[0-9]{0,1}\s(.+[0-9]{0,1})\s.+[0-9]",telefono):
        return telefonoValido
    else:
        return not telefonoValido
    
    
    
    
# +XXE(XX)EFFFFFFF

# E = Espacio Opcional
# FFFFFFFF = Numeros o guiones
# Ejemplo: +52 (55) 1234-5678

# print(re.findall("\+.+[0-9]{2}\s(.+[0-9]{2})\s.+[0-9]{4}-.+[0-9]{4}","+52 (55) 1234-5678"))

print(re.findall('^\+.[0-9]{0,1}\s\(.+[0-9]{0,1}\)$',"+52 (55)"))