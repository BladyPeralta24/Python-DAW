
from bbdd import Query

class Aeropuerto():
    
    
    listado = ['Lanzarote', 'Gran Canaria', 'Fuerteventura', 'Tenerife', 'La Palma', 'La Gomera', 'El Hierro']
    
    
    def __init__(self, sede):
        
        if sede:
            if len(self.listado) == 0:
                print("Cargando listado de BBDD...")
                datos = Query.ejec("select * from aeropuertos;")
                for aeropuerto in datos:
                    self.listado.append(aeropuerto[1])
                    
            aeropuerto = Query.ejec("select * from aeropuerto where sede = '"+ sede +"';")
            
            self.sede = aeropuerto[0][1]
    
    
    @property
    def sede(self):
        return self.__sede
    
    @sede.setter
    def sede(self, nueva_sede):
        if nueva_sede in Aeropuerto.listado:
            self.__sede = nueva_sede
        else:
            raise Exception('sede', 'La sede introducida no se encuentra en nuestro listado')
        
    @staticmethod
    def nueva_sede(nueva_sede):
        
        bandera = False
        
        if not (nueva_sede in Aeropuerto.listado):
            Aeropuerto.listado.append(nueva_sede)
            Query.ejec("insert into aeropuerto (sede) values('"+ nueva_sede +"');")
            bandera = True
            
        return bandera
    
    def id(self):
        aeropuerto = Query.ejec("select id_aeropuerto from aeropuerto where sede = '"+ self.sede +"';")
        
        return aeropuerto[0][0]