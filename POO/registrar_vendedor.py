


def registrar_vendedor(nombre):
    
    aux = 0
    
    def numero_ventas(numero_ventas):
        nonlocal nombre
        nonlocal aux
        aux += numero_ventas
        return str(nombre) + " : " + str(aux)
    
    return numero_ventas

empleado_1 = registrar_vendedor("Laura")
empleado_2 = registrar_vendedor("Carlos")

print(empleado_1(150)) # Laura  : 150
print(empleado_1(300)) # Laura  : 450
print(empleado_2(500)) # Carlos : 500
print(empleado_1(200)) # Laura  : 650
