
## Prueba para meterlo en Github ##
#Caso 1
#print("Bienvenido a la calculadora de python")
#operacion = input("Introduce uno de estos signos para calcular: (+, -, *, /): ")
#if operacion == "+":
#    numero_1 = float(input("Introduce el primer numero: "))
#    numero_2 = float(input("Introduce el segundo numero: "))
#    print("El resultado de la suma es: ", numero_1 + numero_2)
#    
#elif operacion == "-":
#    numero_1 = float(input("Introduce el primer numero: "))
#    numero_2 = float(input("Introduce el segundo numero: "))
#    print("El resultado de la suma es: ", numero_1 - numero_2)
#    
#elif operacion == "*":
#    numero_1 = float(input("Introduce el primer numero: "))
#    numero_2 = float(input("Introduce el segundo numero: "))
#    print("El resultado de la suma es: ", numero_1 * numero_2)
#    
#elif operacion == "/":
#    numero_1 = float(input("Introduce el primer numero: "))
#    numero_2 = float(input("Introduce el segundo numero: "))
#    print("El resultado de la suma es: ", numero_1 // numero_2)
#    
#else:
#    print ("ERROR. no has floatroducido los signos correctos")
    

#Caso 2
salir = False
while salir != True:
    print("""
      ####################################################
      #      BIENVENIDO A LA CALCULADORA DE PYTHON       #
      ####################################################
      Inserte la operacion que va a realizar:
      1: suma (+)
      2: resta (-)
      3: multiplicacion (*)
      4: Division (/)
      5: Salir (s)
      """, end="")
    operacion = input()
    if operacion == '1' or operacion == '2' or operacion == '3' or operacion == '4' or operacion == '5' or operacion == '+' or operacion == '-' or operacion == '*' or operacion == '/' or operacion == 's':
        if operacion == '1' or operacion == '+':
            sumando_1 = float(input("Introduce el primer sumando: "))
            sumando_2 = float(input("Introduce el segundo sumando: "))
            print("El resultado de la suma es: ", str(sumando_1 + sumando_2))
        elif operacion == '2' or operacion == '-':
            minuendo = float(input("Introduce el minuendo: "))
            sustraendo = float(input("Introduce el sustraendo: "))
            print("El resultado de la resta es: ", str(minuendo - sustraendo))
        elif operacion == '3' or operacion == '*':
            multiplicador_1 = float(input("Introduce el primer multiplicador: "))
            multiplicador_2 = float(input("Introduce el segundo multiplicador: "))
            print("El resultado de la multiplicacion es: ", str(multiplicador_1 * multiplicador_2))
        elif operacion == '4' or operacion == '/':
            dividendo = float(input("Introduce el dividendo: "))
            divisor = float(input("Introduce el divisor: "))
            print("El resultado de la division es: ", str(dividendo // divisor))
        elif operacion == '5'or operacion == 's':
            print("fin de la calculadora. Adios")
            salir = True
    else:
        print("ERROR. No has floatroducido la operacion válida. ")
    