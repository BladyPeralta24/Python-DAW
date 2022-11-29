#Crea un programa que solicite al usuario los distintos módulos/asignaturas que esté cursando.
#
#El programa, después de almacenar en una lista todos los módulos/asignaturas, 
#deberá recorrer la lista preguntando qué nota ha sacado en ese determinado módulo/asignatura.
#
#Por último, nos devolverá la nota media de los módulos.

modulo = []
notas = []
salir = False
while not salir:
    
    asignatura = int(input("¿Cuantas asignaturas está cursando?: "))
    
    # introduccion de las asignaturas para el usuario
    i = 0
    while i < asignatura: 
        if asignatura > 0:
            for i in range(asignatura):
                nombre_asignatura = input("Introduce la asignatura que está cursando: ")
                modulo.append(nombre_asignatura)
                asignatura -= 1
        
        i += 1
        
    print (modulo)
    
    
    #Introducir las notas de cada asignatura para un alumno
    suma_nota = 0
    for i in range(len(modulo)):
        nota_mod = input("Introduce la nota de " + modulo[i] + " : ")
        notas.append(nota_mod)
        print ("La nota de " + modulo[asignatura] + ", es de: "+ nota_mod)
        suma_nota += int(nota_mod)
        asignatura -= 1
        i += 1
        
    print (notas)
    
    # Sacar la nota media de los modulos insertados
    nota_media = suma_nota / int(len(notas))
    
    print("La nota media de los modulos es: " + str(nota_media))
        
        
    # Salir del programa si el usuario quiere    
    fin = input("¿Vas a introducir mas datos?(S/N): ")
    if fin == "S" or fin == "s":
        salir = False
    elif fin == "N" or fin == "n":
        salir = True
                                          
print (modulo)
print (notas)
print (nota_media)














# TODO:Implementacion del codigo para pruebas.
##modulo = []
##for i in [0, 1, 2]:
##    asignatura = input("añade una asignatura a la lista: ")
##    modulo.append(asignatura)
##    i += 1
##print(modulo)
##
##notas = []
##i = 0
##for i in [0, 1, 2]:
##    nota_mod = input("Introduce la nota de " + modulo[i] + " : ")
##    notas.append(nota_mod)
##    print("La nota de " + modulo[i] + ", es de: "+ nota_mod)
##    i += 1
##print (notas)
##
##nota_media = int(int(notas[0]) + int(notas[1]) + int(notas[2])) / int(len(notas))
##
##print ("La nota media del curso es: " + str(nota_media))





##  Solucion del profe  ##
#modulo = '-'
#
#listaModulos = []
#
#
#while modulo != "":
#    
#    modulo = input("Inserta un módulo o deja vacío para continuar:\n")   
#    
#    if modulo != '':
#        listaModulos.append(modulo)
#    
#    
##notas = 0
##for modulo in listaModulos:
##    
##    notas += float(input("Inserta la nota que has sacado en " + modulo + ":\n"))
#
#totalNotas = 0
#totalModulos=0
#for modulo in listaModulos:
#    
#    nota = float(input("Inserta la nota que has sacado en " + modulo + ":\n"))
#    
#    totalNotas = totalNotas + nota
#    totalModulos += 1
#    
#
#print("La nota media de todos los modulos es igual a " +  str(totalNotas/totalModulos) )
    
    