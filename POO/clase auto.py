class Auto():
    def __init__(self, marca, modelo, anho,):
        self.marca = marca
        self.modelo = modelo
        self.anho = anho
        self.__velocidad = 0
        
    # Aumentar la velocidad en 10 unidades
    def acelerar(self):
        self.__velocidad += 10
        print('La velocidad del coche es de ' + str(self.__velocidad) +' Km')
    
    # Disminuir la velocidad en 7 unidades
    def frenar(self):
        self.__velocidad -= 7
        
        if self.__velocidad < 0:
            self.__velocidad = 0
            
        print('La velocidad del coche es de '+ str(self.__velocidad) + ' Km')
        
    # Imprimir los atributos del auto
    def mostrar_informacion(self):
        
        return f'Marca del coche {self.marca}, modelo del coche {self.modelo}, año de salida {self.anho}, velocidad alcanzado {self.__velocidad} Km/h'
        
        
coche1 = Auto('Renault', 'Twingo', 1992)

print(coche1.mostrar_informacion())

coche1.acelerar()
coche1.frenar()




# Ejercicio hecho por el profe
# class Auto():
    
    
#     def __init__(self, marca, modelo, anho):
#         self.marca = marca
#         self.modelo = modelo
#         self.anho = anho
#         self.__velocidad = 0
        
        
#     def acelerar(self):
#         self.__velocidad += 10
        
#     def frenar(self):        
#         self.__velocidad -= 7
        
#         if self.__velocidad < 0:
#             self.__velocidad = 0
        
        
#     def mostrar_informacion(self):
#         return f"El coche marca {self.marca} modelo {self.modelo} del año {self.anho} va a una velocidad de {self.__velocidad} km/h"
    
    
# renault = Auto("Renault", "Twingo", 1993)


# print(renault.mostrar_informacion())

# renault.acelerar()
# renault.acelerar()

# print(renault.mostrar_informacion())

# renault.frenar()

# print(renault.mostrar_informacion())


        