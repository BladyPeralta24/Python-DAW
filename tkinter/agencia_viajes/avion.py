

class Avion():
    
    
    modelos = {
         'Boeing 747' : 700
        ,'Boeing 737' : 800
        ,'Airbus a380' : 900
    }
    
    def __init__(self, modelo):
        
        self.modelo = modelo
        
    @property
    def modelo(self):
        return self.__modelo
    
    @modelo.setter
    def modelo(self, nuevo_valor):
        if nuevo_valor in Avion.modelos:
            self.__modelo = nuevo_valor
        else:
            raise Exception('modelo', 'El modelo del avion no se encuentra en el listado.')
    
    @property
    def capacidad(self):
        return Avion.get(self.__modelo)
        
            
            
# print(Avion.tipos)