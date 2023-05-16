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
    
    ventana = 0
    posx_y = 0
    
    '''Clase Agencia de Viajes'''
    # Declarar metodo constructor de la aplicacion
    def __init__(self, img_carpeta, iconos):
        ''' Definir ventana de la aplicacion, menu, submenus, 
        menu contextual, barra de herramientas, barra de estado 
        y atajos del teclado '''
        
        
        self.img_carpeta = img_carpeta
        self.iconos = iconos
        
        self.raiz = Tk()
        
        self.raiz.title("Agencia de Viajes" + __version__) # Titulo
        
        self.icono1 = PhotoImage(file=self.iconos[0]) # icono app
        self.raiz.iconphoto(self.raiz, self.icono1) # Asigna icono app
        
        self.raiz.option_add('*Font', 'Helvetica 12') # Fuente predeterminada
        self.raiz.option_add('*tearOff', False) # Deshabilita submenus flotantes
        
        self.raiz.minsize(400,300) # Establece tamaño minimo ventana
        
        self.fuente = font.Font(weight='normal')
        
        """
        Declarar variables para opciones predeterminadas:
        (Estos valores se podrian leer de un archivo de 
        configuración)
        """
        self.nombre = StringVar(value="")
        self.apellido1 = StringVar(value="")
        self.apellido2 = StringVar(value="")
        self.viaje = StringVar(value="")
        self.origen = StringVar(value="")
        self.destino = StringVar(value="")
        self.avion = StringVar(value="")
        self.filtro = StringVar(value="")
        
        self.viajes = self.leer_viajes()
        
        # Barra de Estado
        self.estado = IntVar()
        self.estado.set(1) # mostrar Barra de Estado
        
        # Definir barra de menu de la aplicacion:
        barramenu = Menu(self.raiz)
        self.raiz['menu'] = barramenu
        
        # Definir submenus
        icono2 = PhotoImage(file=self.iconos[1])
        icono3 = PhotoImage(file=self.iconos[2])
        icono4 = PhotoImage(file=self.iconos[3])
        icono5 = PhotoImage(file=self.iconos[4])
        
        barramenu.add_command(
             label        = 'Alta'
            ,command      = self.alta_billete
            ,underline    = 0
            ,accelerator  = "Ctrl+a"
            ,image        = icono2
            ,compound     = LEFT
        )
        
        barramenu.add_command(
             label        = 'Listado'
            ,command      = self.listado_viajes
            ,underline    = 0
            ,accelerator  = "Ctrl+l"
            ,image        = icono3
            ,compound     = LEFT
        )
        
        barramenu.add_command(
             label        = 'Cargar'
            ,command      = self.carga_externa
            ,underline    = 0
            ,accelerator  = "Ctrl+c"
            ,image        = icono4
            ,compound     = LEFT
        )
        
        barramenu.add_command(
             label        = 'Salir'
            ,command      = self.salir
            ,underline    = 0
            ,accelerator  = "Ctrl+s"
            ,image        = icono5
            ,compound     = LEFT
        )
        
        # Creamos el frame donde vamos a colocar el Alta y el listado de viajes
        self.frame = Frame(self.raiz)
        
        self.frame.config(width=400, height=300)
        self.frame.pack(side=TOP)
        
        # Declarar teclas de acceso rapido:
        self.raiz.bind("<Control-a>", lambda event: self.alta_billete())
        self.raiz.bind("<Control-l>", lambda event: self.listado_viajes())
        self.raiz.bind("<Control-c>", lambda event: self.carga_externa())
        self.raiz.bind("<Control-s>", lambda event: self.salir())
        
        self.raiz.mainloop()
        
    def leer_viajes(self):
        # f = open(ruta)
        
        # text = f.read()
        
        # dict_viajes = ast.literal_eval(texto)
        
        pass
        
    def alta_billete(self):
        
        # Introducir datos del Usuario
        self.destruir_frames()
        
        # opciones = self.viajes.keys()
        
        etiqueta_alta = ttk.Label(self.frame, text='alta billetes')
        
        select_viaje = OptionMenu(self.frame, self.viaje)
        
        etiqueta_viajes = ttk.Label(self.frame, text='Viajes:', justify='left', width=40, padding=[10])
        
        etiqueta_nombre = ttk.Label(self.frame, text='Nombre', justify='left', width=40, padding=[10])
        
        nombre = ttk.Entry(self.frame, justify='left', textvariable=self.nombre)
        
        etiqueta_apellido1 = ttk.Label (self.frame, text='Primer Apellido', justify='left', width=40, padding=[10])
        
        apellido1 = ttk.Entry(self.frame, justify='left', textvariable=self.apellido1)
        
        etiqueta_apellido2 = ttk.Label (self.frame, text='Segundo Apellido', justify='left', width=40, padding=[10])
        
        apellido2 = ttk.Entry(self.frame, justify='left', textvariable=self.apellido2)
        
        
        
        etiqueta_alta.pack(side=TOP)
        select_viaje.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
        
        etiqueta_viajes.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
        
        etiqueta_nombre.pack(side=TOP, fill=BOTH, padx=10, pady=5)
        nombre.pack(side=TOP, fill=X,padx=10, pady=5)
        
        etiqueta_apellido1.pack(side=TOP, fill=BOTH,padx=10, pady=5)
        apellido1.pack(side=TOP, fill=X, padx=10, pady=5)
        
        etiqueta_apellido2.pack(side=TOP, fill=BOTH,padx=10, pady=5 )
        apellido2.pack(side=TOP, fill=X, padx=10, pady=5)
    
    def listado_viajes(self):
        self.destruir_frames()
        
        etiqueta_lista = ttk.Label(self.frame, text='Listado de viajes:', justify='left', width=40, padding=[10])
        etiqueta_lista.pack(side=TOP)
    
    def carga_externa(self):
        self.destruir_frames()
        
        etiqueta_carga = ttk.Label(self.frame, text='Cargar viajes:', justify='left', width=40, padding=[10])
        etiqueta_carga.pack(side=TOP)
    
    # def f_salir(self):
    #     '''Salir de la aplicacion'''
    #     self.raiz.destroy()
        
    def salir(self):
        # Implementar una ventana salir para salir para 
        # preguntar al cliente si esta seguro de salir de
        # la aplicacion.
        self.destruir_frames()
        self.abrir_ventana()
        
        etiqueta_salir = ttk.Label(self.frame, text='Si quiere salir, vuelva pulsar el boton salir.', justify='left', width=40, padding=[10])
        etiqueta_salir.pack(side=TOP)
        
    def destruir_frames(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
            
    def abrir_ventana(self):
        
        self.ventana = Toplevel()
        # AgenciaDeViajes.ventana += 1
        # AgenciaDeViajes.posx_y += 50
        
        # tamypos = '200x100+' + str(AgenciaDeViajes.posx_y) + '+' + str(AgenciaDeViajes.posx_y)
        self.ventana.geometry()
        self.ventana.resizable(0,0)
        self.ventana.title('Salir')
        
        etiqueta_salir_ventana = ttk.Label(self.ventana, text='¿Seguro que quieres salir de la aplicación?', justify='left', width=40, padding=[10])
        etiqueta_salir_ventana.pack(side=TOP)
        
        boton_si = ttk.Button(self.ventana, text='si', command=self.raiz.destroy)
        boton_si.pack(side=LEFT, padx=5, pady=5)
        
        boton_no = ttk.Button(self.ventana, text='no', command=self.ventana.destroy)
        boton_no.pack(side=RIGHT, padx=5, pady=5)
        
        self.ventana.transient(master=self.raiz)
        
        self.ventana.grab_set()
        self.raiz.wait_window(self.ventana)
        
        
# Funciones de la aplicacion

def fun_verificar_iconos(iconos):
    """ 
    Verificar existencia de iconos
    iconos -- Lista de iconos
    """
    for icono in iconos:
        if not os.path.exists(icono):
            print('Icono no encontrado: ', icono)
            return(1)
        return(0)

def main():
    """ Iniciar aplicacion """
    app_carpeta = os.getcwd()
    
    print("La ruta de la carpeta esta en: ", app_carpeta)
    
    img_carpeta = app_carpeta + os.sep + 'tkinter/agencia_viajes/imagenes' + os.sep
    
    # declarar y verificar iconos de la aplicacion:
    iconos = (
         img_carpeta + "icono-app.png"
        ,img_carpeta + "alta.png"
        ,img_carpeta + "listado.png"
        ,img_carpeta + "cargar.png"
        ,img_carpeta + "salir32x32.png"
    )
    
    error1 = fun_verificar_iconos(iconos)
    
    if not error1:
        mi_app = AgenciaDeViajes(img_carpeta, iconos)
    return(0)

if __name__ == '__main__':
    main()
        

























































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