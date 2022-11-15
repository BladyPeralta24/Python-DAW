#letrasDNI = "TRWAGMYFPDXBNJZSQVHLCKE"
# digamos que el usuario introduce el siguiente DNI -> 78848952F
# Queremos verificar si el DNI introducido es valido o no

#dni = input("Introduce tu dni por favor: ")
#dni = dni.upper()
#letra = 0
#dniNumero = dni[0:8]
#
#if len(dniNumero) == 8:
#    letra = int(dniNumero) % 23
#    
#    if dni[-1] == letrasDNI[letra]:
#        print ("El DNI introducido es valido")
#    else:
#        print("El DNI introducido no es válido")
#        
#    
#else:
#    print("El DNI introducido no es valido")
    

#caso 2
validNIF = 'TRWAGMYFPDXBNJZSQVHLCKE'

nif = input("Introduza un NIF válido: ")
nif = nif.upper()
while not nif[0:-1].isnumeric():
    nif = input("Introduza un NIF válido: ")

dni = int(nif[0:-1])

posLetra = dni % 23
if validNIF[posLetra] == nif[-1]:
    print("Has insertado un NIF válido")
else:
    print("El NIF insertado, es inválido")
    



