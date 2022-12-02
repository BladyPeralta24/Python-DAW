# Escriba un programa que permita crear una lista de palabras y que, a continuación muestre las siguientes opciones:
# [C] Contar: Me pide otra cadena, y me dice cuantas veces aparece en la lista
# [M] Modificar: Me pide una cadena, y otra cadena a modificar, y modifica todas alas apariciones de la primera por la segunda en la lista.
# [E] Eliminar: Me pide una cadena, y la elimina de la lista.
# [S] Mostrar: Muestra la lista de cadenas
# [T] Terminar

listaPalabras = []

palabra = 0
while palabra != "":
    palabra = input("Introduce un palabra a la lista: ")
    if palabra != "":
        listaPalabras.append(palabra)



menu = 0
while menu != "":
    
    menu = input('''Bienvenido al menú. Introduce uno de estos comando:
[C] Contar: Me pide otra cadena, y me dice cuantas veces aparece en la lista
[M] Modificar: Me pide una cadena, y otra cadena a modificar, y modifica todas a las apariciones de la primera por la segunda en la lista.
[E] Eliminar: Me pide una cadena, y la elimina de la lista.
[S] Mostrar: Muestra la lista de cadenas
[T] Terminar 
''')
    if menu == "C" or menu == "c":
        palabra = input("introduzca una palabra en la lista: ")
        if palabra != "":
            listaPalabras.append(palabra)
        else:
            print(listaPalabras)
            
        #pedir cuantas veces aparece la palabra en la lista
        print("La palabra " + palabra + ", aparece en la lista: "+ str(listaPalabras.count(palabra)) + " veces.")
        
    elif menu == "M" or menu == "m":
        
        print(listaPalabras)
        palabraModificada = input("Introduce una palabra de la lista para que sea modificada: ")
        palabraAModificar = input("Introduce una palabra para modificar: ")
        
        if palabraModificada in listaPalabras:
            listaPalabras.remove(palabraModificada)
            listaPalabras.append(palabraAModificar)
        else:
            print("ERROR. La palabra que quieres modificar no está en la lista.")
            
        print(listaPalabras)
        
    elif menu == "E" or menu == "e":
        
        print (listaPalabras)
        eliminar = input("elige una palabra que quieras eliminar de la lista: ")
        if eliminar in listaPalabras:
            listaPalabras.remove(eliminar)
        print (listaPalabras)
        
        
    elif menu == "S" or menu == "s":
        
        print(listaPalabras)
        
    elif menu == "T" or menu == "t":
        
        menu = ""
        





# Finalizacion del programa
print("Fin del programa. Adios")


##  opcion del ejercicio hecho por ryan(compañero)  ##
#laLista = []
#
#terminar = False
#
#comandos = ("\nPuede hacer uso de los siguientes comandos.\n[c] Contar(Cuenta las veces que aparece la cadena introducida, el la lista)\n[m] Modificar(Reemplaza la cadena introducida por la que indique si aparece en la lista)\n[E] Eliminar(Elimina la cadena introducida, de la lista)\n[S] Mostrar(Muestra la lista por pantalla)\n[T] Terminar(Termina el programa)\n[h] Ayuda(ver la lista de comandos disponibles)\n")
#print(comandos)
#while not terminar:
#    opcion_recogida = input("Introduce una instruccion o un elemento para agragar a la lista: ")
#    if opcion_recogida == "c":
#        opcion_recogida = input("Indique el elemento que quiere contar en la lista: ")
#        print(laLista.count(opcion_recogida))
#    elif opcion_recogida == "m":
#        opcion_recogida = input("Indique el elemento que quiere modificar: ")
#        if opcion_recogida in laLista:
#            reemplazar = input("Indique la modificaciÃ³n que quiere realizar: ")
#            while opcion_recogida in laLista:
#                pos_elemento = laLista.index(opcion_recogida)
#                laLista.remove(opcion_recogida)
#                laLista.insert(pos_elemento, reemplazar)
#        else: 
#            print("El elemento \"{}\" no esta en la lista".format(opcion_recogida))
#        
#    elif opcion_recogida == "e":
#        opcion_recogida = input("Indique el elemento que quiere eliminar de la lisa: ")
#        if opcion_recogida in laLista:
#            while opcion_recogida in laLista:
#                laLista.remove(opcion_recogida)
#        else:
#            print("El elemento \"{}\" no esta en la lista".format(opcion_recogida))
#            opcion_recogida == ""
#        
#    elif opcion_recogida == "s":
#        print(laLista)
#    elif opcion_recogida == "t":
#        terminar=True
#    elif opcion_recogida == "h":
#        print(comandos)
#    else:
#        if opcion_recogida != "":
#            laLista.append(opcion_recogida)
#        else:
#            print("Error. No puede introducir un elemento vacio")