animales = ["Perro", "Gato", "Elefante", "Girafa"]
salir = False

while not salir:
    insert_animal = input("Inserte un animal en la lista: ")
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