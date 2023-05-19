

class Avion():
    
    
    tipos_aviones = ['Boeing 747', 'Boeing 737','Airbus a380']
    
    modelos = {
         tipos_aviones[0] : 700
        ,tipos_aviones[1] : 800
        ,tipos_aviones[2] : 900
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