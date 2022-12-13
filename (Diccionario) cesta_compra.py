# Escribir un programa que cree un diccionario simulando una cesta de la compra. 
# El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. 
# Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato

###  Lista de la compra     ###
###  Artículo 1	    Precio  ###
###  Artículo 2	    Precio  ###
###  Artículo 3	    Precio  ###
###  …	…                   ###
###  Total	        Coste   ### 


# TODO: Terminar en casa el programa
cesta ={}
articulo = "-"
while articulo != "N":
    articulo = input("Introduce un articulo a la cesta: ")
    precio = float(input("Introduce el coste del artículo: "))
    lista = cesta.setdefault(articulo,precio)
    print(cesta)
    articulo = input("¿Desas introducir más valores? (S/N): ")
    if articulo == "S" or articulo == "s":
        print("\n\n")
    else:
        print("Fin del programa")
        
print(cesta)

##  Ejercicio resuelto por compañero  ##

# cesta_compra   = {}
# contador_salir = 0
# i = 0
# contador_salir = input("Indique cuantos productos desea aÃ±adir: ")
# while i < int(contador_salir):
#     producto       = input("Introduzca el producto que desea: ")
#     precio         = input("Ahora el precio del producto: ")
#     cesta_compra[producto] = precio
#     i += 1
# coste_total = 0
# print('\nLista de la compra:\n')
# for producto, precio in cesta_compra.items():
#     print(producto.title(),':',precio,'euros')
#     coste_total += float(precio)
# print('Total : ',coste_total,'euros\n')
