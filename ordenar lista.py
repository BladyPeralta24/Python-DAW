lista_numeros = []
insert_numero = 0
while insert_numero != "":
    insert_numero = input("Inserte un numero entero para la lista. Para parar pulsa Enter: ")

    if insert_numero != "": #and insert_numero.isnumeric():
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