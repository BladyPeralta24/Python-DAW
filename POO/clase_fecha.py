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
        anho = str(self.__anho)
        mes = str(self.__mes)
        dia = str(self.__dia)
        
        return (anho + mes + dia) < (other.anho + other.mes + other.dia)
    
    
    def __le__(self, other):
        
        return self.__dia <= other.dia and self.__mes <= other.mes and self.__anho <= other.anho
    
    
    def __ge__(self, other):
        
        return self.__dia >= other.dia and self.__mes >= other.mes and self.__anho >= other.anho
    
    
    def __gt__(self, other):
        
        return self.__dia > other.dia and self.__mes > other.mes and self.__anho > other.anho
    
    
    
    def __str__(self):
        anho = str(self.__anho)
        mes = str(self.__mes)
        dia = str(self.__dia)
        return f'{anho + mes + dia}'
    
    
    
    
fecha1 = Fecha(12, 4, 2023)
fecha2 = Fecha(5, 5, 2023)


print(fecha1)
# print(fecha1 > fecha2)
# print(fecha1 >= fecha2)
# print(fecha1 <= fecha2)
print(fecha1 < fecha2)
            