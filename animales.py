animales = ["Perro", "Gato", "Elefante", "JSirafa"]
salir = False

while not salir:
    insert_animal = input("Inserte un animal en la lista: ")
    if insert_animal[-1] == "s":
        insert_animal = insert_animal[0:-1]
        
    insert_animal = insert_animal.title()
    
    if insert_animal in animales:
        print("El animal insertado ya está en la lista")
    else:
        animales.append(insert_animal)
    print(animales)
    
    #Preguntar al usuario si quiere salir
    fin = input("¿Vas a introducir mas datos?(S/N): ")
    if fin == "S" or fin == "s":
        salir = False
    elif fin == "N" or fin == "n":
        salir = True


animales.remove("Perro")
animales.remove("Gato")   

print(animales)

##  Solucion del profe  ##
#animales = ["Perro", "Gato", "Elefante", "Jirafa"]
#
#
#animal = '-'
#
#while animal != '':
#    animal = input("Inserte un animal, o inserta vacío para terminar: \n")
#    
#    animal = animal.title()
#    
#    if animal != '':
#        if animal[-1] == 's':
#            animal = animal[0:-1]
#               
#        if animal not in animales:
#            animales.append(animal)
#        
#        
#animales.remove("Perro")
#animales.remove("Gato")
#
#
#print(animales)