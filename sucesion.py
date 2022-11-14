
## Prueba para meterlo en Github ##

#inicio = input("Introduce la letra de inicio: ")
#final = input("Introduce la letra de final: ")
#print("")



letra_inicial = input("Introduce el valor Inicial: ")
letra_fin = input("Introduce el valor Final: ")


if letra_inicial == 'a':
    iterador = 1
elif letra_inicial == 'b':
    iterador = 2
elif letra_inicial == 'c':
    iterador = 3
elif letra_inicial == 'd':
    iterador = 4
elif letra_inicial == 'e':
    iterador = 5
elif letra_inicial == 'f':
    iterador = 6
elif letra_inicial == 'g':
    iterador = 7    
    
    
if letra_fin == 'a':
    fin = 1
elif letra_fin == 'b':
    fin = 2
elif letra_fin == 'c':
    fin = 3
elif letra_fin == 'd':
    fin = 4
elif letra_fin == 'e':
    fin = 5
elif letra_fin == 'f':
    fin = 6
elif letra_fin == 'g':
    fin = 7    

while iterador <= fin:
    
    j=1
    
    if iterador == 1:
        letra = 'a'
    elif iterador == 2:
        letra = 'b'
    elif iterador == 3:
        letra = 'c'
    elif iterador == 4:
        letra = 'd'
    elif iterador == 5:
        letra = 'e'
    elif iterador == 6:
        letra = 'f'
    elif iterador == 7:
        letra = 'g'   
        
        
    while(j <= 5):      
        print(str(j) + letra , end="-")
        j += 1
        
    iterador += 1
    
    
        