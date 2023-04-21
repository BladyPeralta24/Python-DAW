# Crea un programa que guarde en un fichero de texto, los viajes disponibles para poder vender a sus clientes:
# Los datos a solicitar serán:
# - Origen
# - Destino
# - Billetes Comprados
# - Capacidad Avión
# - Avión (Boeing 747, Boeing 737, Airbus a380)
# - Precio

# El programa debe permitir realizar una reserva a nombre de una persona y quedar almacenada esta.

# from viaje import Viaje
# from avion import Avion
from persona import Persona

import ast
import json


class AgenciaViajes():
    
    archivo_datos = 'home/bladimir/Escritorio/python/POO/Persona/info_viaje.json'
    
    def guardar(self):
        
        file = open(AgenciaViajes.archivo_datos, 'r')
        
        contenido = file.read()
        
        datos_viaje = ast.literal_eval(contenido)
        
        file.close()
        
        vuelos = {}
        key = {}
        
        vuelos["Origen"] = self.origen
        vuelos["Destino"] = self.destino
        vuelos["Capacidad de avion"] = self.capacidad
        vuelos["Precio"] = self.precio
        vuelos["Billetes comprados"] = self.billetes_comprados
        
        key[self.origen," - ",self.destino] = vuelos
        
        file = open(AgenciaViajes.archivo_datos, "w")
        
        datos_viaje[key] = vars(self)
        
        file.write(json.dumps(datos_viaje))
        
        
        
        # file = open(AgenciaViajes.archivo_datos, 'w')
        
        # datos_viaje[(self.origen, self.destino)] = vars(self)
        
        # file.write(json.dumps(datos_viaje))
    
    def __init__(self, origen = "", destino = "", precio = "", capacidad = ""):
        
        self.origen             = origen
        self.destino            = destino
        self.precio             = precio
        self.capacidad          = capacidad
        self.billetes_comprados = self.Persona.guardar()
        
        
        
        
        
        
        
        
        
        
        
        
        

prueba = AgenciaViajes()

prueba.origen = "Lanzarote"
prueba.destino = "Madrid"
prueba.precio = "75€"
prueba.capacidad = 300

print(prueba.guardar())