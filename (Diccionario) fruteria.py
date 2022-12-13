# Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, 
# pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. 
# Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

#   Fruta	Precio
#   Plátano	1.35
#   Manzana	0.80
#   Pera	0.85
#   Naranja	0.70

fruteria = {'Plátano': 1.35,
            'Manzana': 0.80,
            'Pera'   : 0.85,
            'Naranja': 0.70}

print(fruteria)
# TODO: Terminar la parte de introducir valores de la fruta
# TODO: TErminar si la fruta está en el diccionario
# TODO: Terminar el calculo del precio de la fruta por los kilos que quiere el usuario
fruta = input("Elige una fruta de la lista: ")
if fruta in fruteria:
    kilos = float(input("¿Cuantos kilos quieres de "+ fruta +" ?: "))
    print(kilos)
    
resultado = kilos * fruteria[fruta]

print (resultado)
    
    
    
# Iterar diccionario #
#diccionario = {
#     "España"      : "Madrid"
#    ,"Alemania"    : "Berlín"
#    ,"Suiza"       : "Berna"
#    ,"Reino Unido" : "Londres"
#}
#
#
#for pais, capital in diccionario.items():
#    print(pais, capital)