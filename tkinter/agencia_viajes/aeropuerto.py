
class Aeropuerto():
    
    listado = ['Lanzarote', 'Gran Canaria', 'Tenerife', 'Madrid', 'Barcelona', 'Fuerteventura', 'El Hierro', 'La Gomera', 'La Palma']
    
    def __init__(self, sede):
        self.__sede = sede
        
        
    @property
    def sede(self):
        return self.__sede
    
    @sede.setter
    def sede (self, nuevo_valor):
        
        if nuevo_valor in Aeropuerto.listado:
            self.__sede = nuevo_valor
        else:
            raise Exception('sede', 'La sede introducida no se encuentra en nuestro listado')