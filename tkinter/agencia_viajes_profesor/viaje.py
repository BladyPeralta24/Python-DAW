from bbdd import Query

from aeropuerto import Aeropuerto
from avion import Avion
from billete import Billete

class Viaje():
    
    
    def __init__(self, origen: Aeropuerto, destino: Aeropuerto, avion: Avion):
        self.__origen  = origen
        self.__destino = destino
        self.__avion   = avion
        self.__billetes_comprados = []
        
    @property
    def origen(self):
        return self.__origen
        
    @origen.setter
    def origen(self, nuevo_origen):
        if not nuevo_origen:
            raise Exception('origen', 'No se ha insertado un origen. ')
        else:
            self.__origen = nuevo_origen
            
    @property
    def destino(self):
        return self.__destino
        
    @destino.setter
    def destino(self, nuevo_destino):
        if not nuevo_destino:
            raise Exception('destino', 'No se ha insertado un destino. ')
        else:
            self.__destino = nuevo_destino
        
    @property
    def avion(self):
        return self.__avion
        
    @avion.setter
    def avion(self, nuevo_avion):
        self.__avion = nuevo_avion
        
    @property
    def billetes_comprados(self):
        return self.__billetes_comprados
    
    @billetes_comprados.setter
    def billetes_comprados(self, nuevo_billete: Billete):
        
        if len(self.__billetes_comprados) >= self.__avion.capacidad:
            raise Exception('billetes_comprados', "- Se ha superado el límite de billetes posibles.\n")
        else:
            self.__billetes_comprados.append(nuevo_billete)
            
            

    def diccionario(self):
        
        diccionario = {}
        
        billetes_comprados = {}
        
        
        i = 1
        for billete in self.__billetes_comprados:          
           
            billetes_comprados[i] = billete.diccionario()
            i += 1
            
        diccionario[self.__origen.sede +'-'+ self.__destino.sede] = {
            
             "origen"  : self.__origen.sede
            ,"destino" : self.__destino.sede
            ,"avion"   : self.__avion.modelo
            ,"billetes_comprados" : billetes_comprados
        }

        return diccionario
    
    def guardar(self):
        id_origen  = self.__origen.id()
        id_destino = self.__destino.id()
        id_avion   = self.__avion.id()
        
        datos_avion = Query.ejec(f'select id_viaje from viajes where id_avion = "{id_avion}" and id_origen = "{id_origen}" and id_destino = "{id_destino}" ')
        
        if not datos_avion:
            Query.ejec(f"insert into viajes (id_origen, id_destino, id_avion) values('{id_origen}', '{id_destino}', '{id_avion}')")
        else:
            raise Exception('viajes', 'El viaje ya se encuentra dado de alta')
        
        
    
    def __str__(self):
        return f"Origen: {self.__origen.sede} Destino: {self.__destino.sede} Avion: {self.__avion.modelo} Capacidad: {self.__avion.capacidad}"
    
    

# viaje = Viaje(Aeropuerto('Las Palmas'),Aeropuerto('Londres'), Avion('Boeing737'))


# viaje.guardar()