# Escriba una clase "Fecha" que tenga un año, mes y día. 
# Sobrecargue los operadores "<" , ">=", "<=" y ">" 
# para que puedan comparar dos fechas y determinar cuál es anterior o posterior a la otra. 


class Fecha():
    
    def __init__(self, dia, mes, anho):
        
        self.dia = dia
        self.mes = mes
        self.anho = anho
        
        
        
    @property
    def dia(self):
        return self.__dia
    
    @dia.setter
    def dia(self, nuevo_valor):
        if isinstance(nuevo_valor, int):
            self.__dia = nuevo_valor
     
    @property
    def mes(self):
        return self.__mes
    
    @mes.setter
    def mes(self, nuevo_valor):
      if isinstance(nuevo_valor, int):
          self.__mes = nuevo_valor
            
    @property
    def anho(self):
        return self.__anho
    
    @anho.setter
    def anho(self, nuevo_valor):
        if isinstance(nuevo_valor, int):
            self.__anho = nuevo_valor
        
        
            
            
    def __lt__(self, other):
        anho = str(self.__anho).zfill(2)
        mes = str(self.__mes).zfill(2)
        dia = str(self.__dia).zfill(2)
        
        return (anho + mes + dia) < (str(other.__anho).zfill(2) + str(other.__mes).zfill(2) + str(other.__dia).zfill(2))
    
    
    def __le__(self, other):
        
        anho = str(self.__anho).zfill(2)
        mes = str(self.__mes).zfill(2)
        dia = str(self.__dia).zfill(2)
        
        return (anho + mes + dia) <= (str(other.__anho).zfill(2) + str(other.__mes).zfill(2) + str(other.__dia).zfill(2))
    
    
    def __ge__(self, other):
        
        anho = str(self.__anho).zfill(2)
        mes = str(self.__mes).zfill(2)
        dia = str(self.__dia).zfill(2)
        
        return (anho + mes + dia) >= (str(other.__anho).zfill(2) + str(other.__mes).zfill(2) + str(other.__dia).zfill(2))
    
    
    def __gt__(self, other):
        
        anho = str(self.__anho).zfill(2)
        mes = str(self.__mes).zfill(2)
        dia = str(self.__dia).zfill(2)
        
        return (anho + mes + dia) > (str(other.__anho).zfill(2) + str(other.__mes).zfill(2) + str(other.__dia).zfill(2))
    
    
    
    def __str__(self):
        anho = str(self.__anho).zfill(2)
        mes = str(self.__mes).zfill(2)
        dia = str(self.__dia).zfill(2)
        return f'{anho + mes + dia}'
    
    
    
    
fecha1 = Fecha(12, 4, 2023)
fecha2 = Fecha(12, 4, 2023)


print(fecha1)
print(fecha1 > fecha2)
print(fecha1 >= fecha2)
print(fecha1 <= fecha2)
print(fecha1 < fecha2)







# Tarea hecha por el profe
# class Fecha():
    
#     def __init__(self, anho : int, mes : int, dia : int):
        
#         self.anho = anho
#         self.mes  = mes
#         self.dia  = dia
        
#         """
#         print("2".zfill(2))
#         print(f'{2:02}')
#         """
        
#         #AAAAMMDD
#         self.fecha_numero = int(str(self.anho) + str(self.mes).zfill(2) + str(self.dia).zfill(2))

        
        
#     def __lt__(self, other): # <
#         return self.fecha_numero < other.fecha_numero
    
#     def __le__(self, other): # <=
#         return self.fecha_numero <= other.fecha_numero
    
#     def __gt__(self, other): # >
#         return self.fecha_numero > other.fecha_numero
    
#     def __ge__(self, other): # >=
#         return self.fecha_numero >= other.fecha_numero
    
# fecha1 = Fecha(2023,2,10)
# fecha2 = Fecha(2024,2,10)



        
# if fecha1 <= fecha2:
#     print("fecha1 es menor que fecha2")
        
        
        