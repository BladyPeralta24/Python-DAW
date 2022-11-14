### Prueba para meterlo en Github ###

inicio = int(input("Introduce el primer numero para la sucesion de fibonacci: "))
fin = int(input("Introduce el segundo numero mayor al primero: "))
while fin < inicio:
    fin = input("Introduce el segundo numero mayor al primero ")
    
print("Los numeros "+ str(inicio)+ " y "+ str(fin)+ ", estan bien introducidos")

fibonacci_1 = int(inicio)
print (str(fibonacci_1), end=", ")
fibonacci_2 = int(inicio + 1)
print (str(fibonacci_2), end=", ")
aux = 0

while aux < fin:
    aux = int(fibonacci_1 + fibonacci_2)
    fibonacci_1 = int(fibonacci_2)
    fibonacci_2 = aux
    if aux <= fin:
        print (str(aux), end=", . ")
        