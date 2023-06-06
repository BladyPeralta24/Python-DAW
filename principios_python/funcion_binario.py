"""Funcion invertir (Cadena texto)
    Entero i = 0;
    Entero caracter = 0;
    Cadena resultadoInvertido = "";

    Mientras i < texto.tamanho entonces
        caracter = binario[i];
        resultadoInvertido = caracter + resultadoInvertido;
        i++;
    Fin Mientras

    devolver resultadoInvertido;
Fin Funcion

Funcion convertirBinario(Entero numero)
    Entero binario;
    Entero i = 0;
    Entero resultado = 1;

    Mientras i < numero hacer
        binario = numero % 2;
        resultado = Cadena(resultado) + Cadena(binario);
        i ++;
    Fin Mientras

    invertir(resultado);

    devolver resultado;
Fin Funcion

    """


def invertir (texto):
    i = 0
    resultado = ""
    
    while i < len(texto):
        letra = texto[i]
        resultado = str(letra) + str(resultado)
        i += 1
        
    return resultado



def convertirBinario(numero):
    i = 0
    resultado = ""
    
    while i < int(numero) :
        binario = int(numero) % 2
        numero = int(numero) / 2
        resultado = str(resultado) + str(binario)
    
    return invertir(resultado)





print("Introduce un numero para convertir a binario: ")

numero = input()

print(convertirBinario(numero))




        
        