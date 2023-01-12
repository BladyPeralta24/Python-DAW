# numero = int(input("Introduce un numero por pantalla: "))
# if numero < 100:
#     print("El numero es menor a 100")
# elif numero > 100:
#     print("El numero es mayor a 100")
# else:
#     print("El numero es igual a 100")



def listaNumeroMayor(listaNumeros) -> list:

    i = 0
    while i < len(listaNumeros):
        j = 0
        while j < len(listaNumeros):
            if listaNumeros[i] > listaNumeros[j]:
                aux = listaNumeros[i]
                listaNumeros[i] = listaNumeros[j]
                listaNumeros[j] = aux

            j += 1
        numeroMayor = listaNumeros[0]
        i += 1
        
    if listaNumeros == []:
        return []
    else:
        return numeroMayor

# Casos de prueba

listaNumeros1 = [20,8,56]
listaNumeros2 = []
listaNumeros3 = [-1, -10000, -4]
listaNumeros4 = [100, 100 , 100]
print("Casos de prueba: ")
print(listaNumeroMayor(listaNumeros1))

assert listaNumeroMayor(listaNumeros2) == []
assert listaNumeroMayor(listaNumeros3) == -1
assert listaNumeroMayor(listaNumeros4) == 100