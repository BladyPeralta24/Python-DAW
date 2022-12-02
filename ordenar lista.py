lista_numeros = []
insert_numero = 0
while insert_numero != "":
    insert_numero = input("Inserte un numero entero para la lista. Para parar pulsa Enter: ")

    if insert_numero != "" and insert_numero.replace('-', '').isnumeric():
        lista_numeros.append(int(insert_numero))
      
print(lista_numeros)

lista_ordenada = lista_numeros.copy()
for i in range(len(lista_ordenada)):
    for j in range(len(lista_ordenada)):
        if lista_ordenada[j] > lista_ordenada[i]:
            aux = lista_ordenada[i]
            lista_ordenada[i] = lista_ordenada[j]
            lista_ordenada[j] = aux
    
print(lista_ordenada)


##  Ejercicio resuelto por el Profesor  ##

""" 
[Listas] Ordenar Lista
Cree un algoritmo que solicite al usuario una lista de números enteros y luego la ordene de menor a mayor. 

**Para la realización del ejercicio, no se permite el uso de funciones de ordenación de elementos.
"""


#numeros_enteros = []
#
#seguir = True
#
#
#while seguir:
#    
#    nuevo_entero = input("Introduzca el siguiente elemento de la lista o deje vacío para finalizar: \n")
#    if nuevo_entero.replace('-','').isnumeric():
#        numeros_enteros.append(int(nuevo_entero))
#    else:
#        seguir = False
#        
#        
#i = 0
#j = 0
#
#
#while i < len(numeros_enteros):
#    j = 0
#    while j < len(numeros_enteros):
#        
#        if numeros_enteros[i] > numeros_enteros[j]:
#            aux = numeros_enteros[i]
#            
#            numeros_enteros[i] = numeros_enteros[j]
#            numeros_enteros[j] = aux
#            
#        
#        
#        j += 1
#    
#    i += 1