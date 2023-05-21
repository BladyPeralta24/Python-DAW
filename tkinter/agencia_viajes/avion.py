

class Avion():
    
    
    modelos = {
          'Airbus 319' : 1
         ,'Airbus 320' : 250
         ,'Airbus 321' : 260
         ,'Boeing 737' : 450
         ,'Boeing 747' : 460
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
        return Avion.modelos.get(self.__modelo)
        
            
            
# print(Avion.tipos)