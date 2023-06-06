# TODO: Crea una función llamada "contar_palabras" que tome como argumento una cadena de texto 
# y devuelva un diccionario con las palabras como clave y su frecuencia como valor.

# TODO: Utiliza la función "contar_palabras" para contar las palabras en el siguiente texto: 
# "El perro corre en el parque. El gato maulla en el tejado."

# TODO: Imprime el diccionario resultante en un formato legible para el usuario.

# TODO: Crea una segunda función llamada "ordenar_palabras" que tome el diccionario de la función "contar_palabras" 
# y devuelva una lista de tuplas ordenadas de manera descendente por frecuencia de aparición de las palabras.

# TODO: Utiliza la función "ordenar_palabras" para ordenar las palabras del texto anterior y muestra el resultado.

# Ejemplo de salida:
# {'El': 2, 'perro': 1, 'corre': 1, 'en': 2, 'el': 2, 'parque.': 1, 'gato': 1, 'maulla': 1, 'tejado.': 1} 
# [('el', 2), ('en', 2), ('El', 2), ('perro', 1), ('corre', 1), ('parque.', 1), ('gato', 1), ('maulla', 1), ('tejado.', 1)]

# TODO: Comprueba el tiempo de ejecución de tu ejercicio realizando una prueba de rendimiento. Se creará un ránking con el resto de la clase sobre el programa más eficiente. 


def contar_palabras(texto):
    dic = {}
    palabra = ""
    for i in range(len(texto)):
        if not texto.find(""):
            palabra += texto[i]
            clave = palabra
            
        
    return texto

# ej: El gato maulla en el tejado

cadena = "El gato maulla en el tejado"

print(contar_palabras(cadena))