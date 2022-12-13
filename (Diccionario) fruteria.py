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
while True:
    print("Los valores en nuestra frutería son: ")
    print(fruteria)
    
    fruta = input("Elige una fruta de la lista: ")
    cantidad = float(input("¿Cuantos kilos quieres de "+ fruta +"?: "))
    if fruta.title() in fruteria:
        
        valor = fruteria.get(fruta.title()) * cantidad
        
        print(fruta.title(), "en", cantidad, "cantidades es igual a un precio de: ", valor)
        
    else:
        print("Disculpe, la fruta no se encuentra disponible.")
        
        
    print("\n\n")
    
    
    
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

