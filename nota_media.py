#Crea un programa que solicite al usuario los distintos módulos/asignaturas que esté cursando.
#
#El programa, después de almacenar en una lista todos los módulos/asignaturas, 
#deberá recorrer la lista preguntando qué nota ha sacado en ese determinado módulo/asignatura.
#
#Por último, nos devolverá la nota media de los módulos.

asignatura = []
nota = []
alumno = []
salir = False

while not salir:
    nombre_apellidos = input("Inserte el nombre y apellidos del alumno/a:\n")
    alumno.append(nombre_apellidos)
    
    numero_asignatura = int(input("¿Cuantas asignaturas está cursando?: "))
    
    i = 0
    while i < numero_asignatura: 
        if numero_asignatura > 0:
            for asignaturas in range(numero_asignatura):
                nombre_asignatura = input("Introduce la asignatura que está cursando: ")
                asignatura.append(nombre_asignatura)
                numero_asignatura -= 1
        
        i += 1
                
    salir = True

                                
                
                
                
                
print (alumno)
print (asignatura)