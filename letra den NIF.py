letrasDNI = "TRWAGMYFPDXBNJZSQVHLCKE"
# digamos que el usuario introduce el siguiente DNI -> 78848952F
# Queremos verificar si el DNI introducido es valido o no

dni = str(input("Introduce tu dni por favor: "))
dni = dni.upper()
letra = 0
dniNumero = dni[0:8]

if len(dniNumero) == 8:
    letra = int(dniNumero) % 23
else:
    print("El DNI introducido no es valido")
    
if dni[-1] == letrasDNI[letra]:
    print ("El DNI introducido es valido")
else:
    print("El DNI introducido no es válido")