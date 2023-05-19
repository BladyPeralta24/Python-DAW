# import os
# import ast
# from viaje import Viaje
# from aeropuerto import Aeropuerto
# from billete import Billete
# from avion import Avion

# ruta = os.path.dirname(__file__) + os.sep + 'bbdd' + os.sep + 'viajes.json'

# f = open(ruta)
# texto = f.read()
# dict_viajes = ast.literal_eval(texto)

# viajes = {}

# for key in dict_viajes:
#     viaje = Viaje(Aeropuerto(dict_viajes[key]['origen']), Aeropuerto(dict_viajes[key]['destino']), Avion(dict_viajes[key]['avion']))
#     for nbillete in dict_viajes[key]['billetes_comprados']:
#         billete = dict_viajes[key]['billetes_comprados'][nbillete]
        
#         carga_billete = Billete()
#         carga_billete.nombre = billete.get('nombre')
#         carga_billete.apellido1 = billete.get('apellido1')
#         carga_billete.apellido2 = billete.get('apellido2')
#         carga_billete.viaje = billete.get('viaje')
        
#         viaje.billetes_comprados = carga_billete
    
#     viajes[key] = viaje

# print(viajes)

import os
import ast
import json
from viaje import Viaje
from aeropuerto import Aeropuerto
from billete import Billete
from avion import Avion

ruta = os.path.dirname(__file__) + os.sep + 'bbdd' + os.sep + 'viajes.json'

f = open(ruta)
texto = f.read()
dict_viajes = ast.literal_eval(texto)

viajes = {}

for key in dict_viajes:
    viaje = Viaje(Aeropuerto(dict_viajes[key]['origen']), Aeropuerto(dict_viajes[key]['destino']), Avion(dict_viajes[key]['avion']))
    for nbillete in dict_viajes[key]['billetes_comprados']:
        billete = dict_viajes[key]['billetes_comprados'][nbillete]
        
        carga_billete = Billete()
        carga_billete.nombre = billete.get('nombre')
        carga_billete.apellido1 = billete.get('apellido1')
        carga_billete.apellido2 = billete.get('apellido2')
        carga_billete.viaje = billete.get('viaje')
        
        viaje.billetes_comprados = carga_billete
    
    viajes[key] = viaje

# Introducir nuevos datos
nuevo_viaje = Viaje(Aeropuerto('Lanzarote'), Aeropuerto('Gran Canaria'), Avion('Boeing 747'))
nuevo_billete = Billete()
nuevo_billete.nombre = 'Juan'
nuevo_billete.apellido1 = 'Pérez'
nuevo_billete.viaje = 'Lanzarote-Gran Canaria'

nuevo_viaje.billetes_comprados = nuevo_billete
viajes['nuevo'] = nuevo_viaje

# Guardar en el archivo viajes.json
with open('viajes.json', 'w') as archivo:
    json.dump(viajes, archivo)

        