from viaje import Viaje
from avion import Avion

import os
from tkinter import *
from tkinter import ttk, font
from tkinter import filedialog as fd


#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# name: __main__.py (Python 3.x).
# description:  Gestión de una agencia de viajes
# purpose:  Gestión de una agencia de viajes
# author: Bladimir
#
#------------------------------------------------------------
'''AgenciaDeViajes: Gestión de una agencia de viajes '''

__title__= 'Agencia de Viajes'
__date__=''
__version__='0.0.1'
__license__='GNU GPLv3'


class AgenciaDeViajes():
    '''Clase Agencia de Viajes'''
    # Declarar metodo constructor de la aplicacion
    def __init__(self, iconos):
        ''' Definir ventana de la aplicacion, menu, submenus, 
        menu contextual, barra de herramientas, barra de estado 
        y atajos del teclado '''
        
        self.iconos = iconos
        
        self.raiz = Tk()
        
        self.raiz.title("Agencia de Viajes" + __version__) # Titulo
        
        self.icono1 = PhotoImage(file=self.iconos[0]) # icono app
        self.raiz.iconphoto(self.raiz, self.icono1) # Asigna icono app
        
        self.raiz.option_add('*Font', 'Helvetica 12') # Fuente predeterminada
        self.raiz.otion_add('*tearOff', False) # Deshabilita submenus flotantes
        
        self.raiz.minsize(400,300) # Establece tamaño minimo ventana
        
        
        
        
        

























































# opciones = """ 
# Inserte una de las siguientes opciones disponibles:

# [I]nsertar un nuevo viaje.
# [C]omprar un billete.
# [S]alir del programa.
# """


# opcion = input(opciones)



# while opcion != 'S':
    
#     if opcion == 'I':
        
#         avion_cargado = False
        
#         opciones_aviones = "Seleccione, un avión de la lista: " + Avion.representacion()
#         viaje = Viaje()        
        
#         while not avion_cargado:
        
#             try:

                
#                 if not viaje.origen:
#                     viaje.origen  = input("Inserte el origen del viaje: ")
                
#                 if not viaje.destino:
#                     viaje.destino = input("Inserte el destino del viaje: ")
                
#                 if not viaje.avion:              
#                     viaje.avion = input(opciones_aviones)
                    
                    
#                 if not viaje.precio:
#                     viaje.precio = float(input("Inserte un precio de billete. "))
                
                
#                 avion_cargado = True
            
#             except Exception as err:
#                 print(err[1], end= "")
                
#         viaje.guardar()
                
        
        
            
        
        
        
#     elif opcion == 'C':
#         pass
    
#     opcion = input("Desea realizar otra operación:\n" + opciones)