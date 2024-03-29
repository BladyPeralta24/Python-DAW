from bbdd import Query

from aeropuerto import Aeropuerto

class Billete():
    
    def __init__(self):
        self.__viaje = ''
        self.__nombre = ''
        self.__apellidos = ''
        
        
    @property
    def viaje(self):
        return self.__viaje
    
    @viaje.setter
    def viaje(self, nuevo_viaje):
        if not nuevo_viaje:
            raise Exception('viaje', 'No se han insertado viajes. ')
        else:
            self.__viaje = nuevo_viaje
            
            
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        if not nuevo_nombre:
            raise Exception('nombre', 'No se ha insertado un nombre. ')
        else:
            self.__nombre = nuevo_nombre

    @property
    def apellidos(self):
        return self.__apellidos
    
    @apellidos.setter
    def apellidos(self, nuevo_apellidos):
        if not nuevo_apellidos:
            raise Exception('apellidos', 'No se ha insertado un apellidos. ')
        else:
            self.__apellidos = nuevo_apellidos
                 
            
    def diccionario(self):
        
        return {
             'viaje'     : self.__viaje
            ,'nombre'    : self.__nombre
            ,'apellidos' : self.__apellidos
        }
        
        
    def guardar(self):
        
        lista_viaje = self.__viaje.split('-')
        
        origen = lista_viaje[0]
        destino = lista_viaje[1]
        
        aeropuerto_origen = Aeropuerto(origen)
        aeropuerto_destino = Aeropuerto(destino)
        
        query_viaje = Query.ejec(f"SELECT id_viaje FROM viaje WHERE id_origen = '{aeropuerto_origen.id()}' and id_destino = '{aeropuerto_destino.id()}'");
        
        id_viaje = query_viaje[0][0]
        
        datos_viaje = Query.ejec(f"SELECT id_billete FROM billete WHERE nombre = '{self.__nombre}' AND apellidos = '{self.__apellidos}' AND id_viaje = '{id_viaje}' ")
        
        if not datos_viaje :
            Query.ejec(f"insert into billete (nombre, apellidos, id_viaje) values ('{self.__nombre}','{self.__apellidos}','{id_viaje}');")
        else:
            raise Exception ('billete', 'El billete ya se encuentra dado de alta')
        
            
            
            
    def __str__(self):
        
        return f"Viaje: {self.__viaje} Nombre: {self.__nombre} Apellidos: {self.__apellidos}"
            
            