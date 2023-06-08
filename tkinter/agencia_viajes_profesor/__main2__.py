import ast
from cgitb import text
import json
from textwrap import indent
from viaje import Viaje
from aeropuerto import Aeropuerto
from avion import Avion
from billete import Billete

from functools import partial
from tkinter import filedialog as fd
from bbdd import Query

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# name: __main__.py (Python 3.x).
# description:  Gestión de una agencia de viajes
# purpose:  Gestión de una agencia de viajes
# author: juanra
#
#------------------------------------------------------------
'''AgenciaDeViajes: Gestión de una agencia de viajes '''

__title__= 'Agencia de Viajes'
__date__ = ''
__version__ = '0.0.1'
__license__ = 'GNU GPLv3'

import os
from tkinter import *
from tkinter import ttk, font, messagebox

class AgenciaDeViajes():

    posx_y = 50
    def __init__(self, iconos):
        ''' Definir ventana de la aplicación, menú, submenús,
        menú contextual, barra de herramientas, barra de
        estado y atajos del teclado '''
        # INICIALIZAR VARIABLES
        self.iconos = iconos
        # DEFINIR VENTANA DE LA APLICACIÓN:
        self.raiz = Tk()
        # ESTABLECER PROPIEDADES DE LA VENTANA DE APLICACIÓN:
        self.raiz.title("Agencia de Viajes: El corte Francés " + __version__) # Título

        self.icono1= PhotoImage(file=self.iconos[0]) # Icono app
        self.raiz.iconphoto(self.raiz, self.icono1) # Asigna icono app

        self.raiz.option_add("*Font", "Helvetica 12") # Fuente predeterminada
        self.raiz.option_add('*tearOff', False) # Deshabilita submenús flotantes

        #self.raiz.attributes('-fullscreen', True) # Maximiza ventana completa
        self.raiz.minsize(400,300) # Establece tamaño minimo ventana
        # ESTABLECER ESTILO FUENTE PARA ALGUNOS WIDGETS:

        self.fuente = font.Font(weight='normal') # normal, bold, etc...
        # DECLARAR VARIABLES PARA OPCIONES PREDETERMINADAS:
        self.nombre    = StringVar(value="")
        self.apellido1 = StringVar(value="")
        self.apellido2 = StringVar(value="")
        self.viaje     = StringVar(value="")
        self.origen    = StringVar(value="")
        self.destino   = StringVar(value="")
        self.avion     = StringVar(value="")
        self.filtro    = StringVar(value="")


        self.viajes = self.leer_viajes()


        barramenu = Menu(self.raiz)
        self.raiz['menu'] = barramenu
        
        # DEFINIR SUBMENÚS 'Sesiones', 'Opciones' y 'Ayuda':

        icono2 = PhotoImage(file=self.iconos[1])
        icono3 = PhotoImage(file=self.iconos[2])
        icono4 = PhotoImage(file=self.iconos[3])
        icono5 = PhotoImage(file=self.iconos[4])

        barramenu.add_command(
             label       = 'Alta' 
            ,command     = self.alta_billete
            ,underline   = 0
            ,accelerator = "Ctrl+a"
            ,image       = icono2
            ,compound    = LEFT
        )

        barramenu.add_command(
             label       = 'Listado' 
            ,command     = self.listado_viajes
            ,underline   = 0
            ,accelerator = "Ctrl+l"
            ,image       = icono3
            ,compound    = LEFT
        )

        #barramenu.add_command(
        #     label       = 'Carga' 
        #    ,command     = self.carga_externa
        #    ,underline   = 0
        #    ,accelerator = "Ctrl+c"
        #    ,image       = icono4
        #    ,compound    = LEFT
        #)

        barramenu.add_command(
             label       = 'Nuevo Viaje' 
            ,command     = self.nuevo_viaje
            ,underline   = 0
            ,accelerator = "Ctrl+n"
            ,image       = icono5
            ,compound    = LEFT
        )

        #Creamos el frame donde vamos a colocar el Alta y el Listado de viajes
        self.frame = Frame(self.raiz)  
   
        self.frame.config(bg="lightblue")     

        self.frame.config(width=400,height=300) 
        self.frame.pack(side=TOP)   


        # DECLARAR TECLAS DE ACCESO RAPIDO:
        self.raiz.bind("<Control-a>", lambda event: self.alta_billete())
        self.raiz.bind("<Control-l>", lambda event: self.listado_viajes())
        #self.raiz.bind("<Control-c>", lambda event: self.carga_externa())

        self.raiz.mainloop()


    def nuevo_viaje(self):
        self.destruir_frames()

        etiqueta_origen   = ttk.Label(self.frame, text="Origen:"  ,justify="left",width=40,padding=[10]) 
        etiqueta_destino  = ttk.Label(self.frame, text="Destino:" ,justify="left",width=40,padding=[10]) 
        etiqueta_avion    = ttk.Label(self.frame, text="Avión:"   ,justify="left",width=40,padding=[10])        


        select_origen   = OptionMenu(self.frame, self.origen,*Aeropuerto.listado)
        select_destino  = OptionMenu(self.frame, self.destino,*Aeropuerto.listado)
        select_avion    = OptionMenu(self.frame, self.avion,*Avion.modelos.keys())
        guardar         = ttk.Button(self.frame, text="Guardar", command=self.guardar_viaje)


        etiqueta_origen.pack(side=TOP,fill=BOTH, expand=True, padx=5, pady=5)   
        select_origen.pack(side=TOP,fill=BOTH, expand=True, padx=5, pady=5)   

        etiqueta_destino.pack(side=TOP,fill=BOTH, expand=True, padx=5, pady=5)
        select_destino.pack(side=TOP,fill=BOTH, expand=True, padx=5, pady=5)   

        etiqueta_avion.pack(side=TOP,fill=BOTH, expand=True, padx=5, pady=5)   
        select_avion.pack(side=TOP,fill=BOTH, expand=True, padx=5, pady=5)   

        guardar.pack(side=TOP,fill=BOTH, expand=True, padx=5, pady=5)  


    def guardar_viaje(self):

        texto_errores = ''

        if not self.origen.get():
            texto_errores = " - No se ha especificado un Origen.\n"

        if not self.destino.get():
            texto_errores += " - No se ha especificado un Destino.\n"

        if not self.avion.get():
            texto_errores += " - No se ha especificado un Avión.\n"

        if self.origen.get() and self.origen.get() == self.destino.get():
            texto_errores += " - Origen no puede ser igual a Destino.\n"


        if self.viajes.get(self.origen.get()+'-'+self.destino.get()):
            texto_errores += " - El viaje ya se encuentra en nuestra BBDD.\n"

        if texto_errores:
            messagebox.showerror('Hay errores en el formulario',texto_errores)
        else:
            viaje = Viaje(Aeropuerto(self.origen.get()),Aeropuerto(self.destino.get()), Avion(self.avion.get()))


            self.viajes[self.origen.get()+'-'+self.destino.get()] = viaje

            self.guardar_fichero()
            messagebox.showinfo('Exito',"Viaje creado con éxito")





    def alta_billete(self):
        self.destruir_frames()
        
        etiqueta_viajes    = ttk.Label(self.frame, text="Viajes:"    ,justify="left",width=40,padding=[10]) 
        etiqueta_nombre    = ttk.Label(self.frame, text="Nombre:"    ,justify="left",width=40,padding=[10]) 
        etiqueta_apellido1 = ttk.Label(self.frame, text="Primer Apellido:" ,justify="left",width=40,padding=[10])        
        etiqueta_apellido2 = ttk.Label(self.frame, text="Segundo Apellido:" ,justify="left",width=40,padding=[10])        

        opciones = self.viajes.keys()

        select_viajes = OptionMenu(self.frame, self.viaje,*opciones)
        nombre    = ttk.Entry(self.frame, justify="left", textvariable=self.nombre)   
        apellido1 = ttk.Entry(self.frame, justify="left", textvariable=self.apellido1)   
        apellido2 = ttk.Entry(self.frame, justify="left", textvariable=self.apellido2)   

        guardar = ttk.Button(self.frame, text="Guardar", command=self.guardar_billete)



        etiqueta_viajes.pack(side=TOP,fill=BOTH, expand=True, padx=5, pady=5)   
        select_viajes.pack(side=TOP,fill=BOTH, expand=True, padx=5, pady=5)   

        etiqueta_nombre.pack(side=TOP,fill=BOTH, expand=True, padx=5, pady=5)   
        nombre.pack(side=TOP,fill=BOTH, expand=True, padx=5, pady=5)   

        etiqueta_apellido1.pack(side=TOP,fill=BOTH, expand=True, padx=5, pady=5)
        apellido1.pack(side=TOP,fill=BOTH, expand=True, padx=5, pady=5)   

        etiqueta_apellido2.pack(side=TOP,fill=BOTH, expand=True, padx=5, pady=5)
        apellido2.pack(side=TOP,fill=BOTH, expand=True, padx=5, pady=5)   

        guardar.pack(side=TOP,fill=BOTH, expand=True, padx=5, pady=5)   


    def guardar_billete(self):
        errores = False

        texto_errores = ''

        nuevo_billete = Billete()


        try:
            nuevo_billete.viaje = self.viaje.get()
        except:
            errores = True
            texto_errores += " - No se ha seleccionado ningún viaje\n"
        else:
            viaje_seleccionado = self.viajes.get(nuevo_billete.viaje) 

        try:
            nuevo_billete.nombre = self.nombre.get()
        except:
            errores = True
            texto_errores += " - No se ha escrito ningún nombre\n"

        try:
            nuevo_billete.apellido1 = self.apellido1.get()
        except:
            errores = True
            texto_errores += " - No se ha insertado ningún apellido 1\n"

        
        nuevo_billete.apellido2 = self.apellido2.get()
        
        try:
            viaje_seleccionado.billetes_comprados = nuevo_billete
        except:
            errores = True
            texto_errores += " - Hay algún problema con la capacidad del avión"


        if errores:
            messagebox.showerror('Hay errores en el formulario',texto_errores)
        else:
            try:
                nuevo_billete.guardar()
                messagebox.showinfo('Operación realizada con éxito',"Se ha introducido el billete en la BBDD")
            except:
                messagebox.showerror('Hay errores en el formulario'," -  Ya existe el billete en la BBDD")


    


    def leer_viajes(self):
        #f = open(ruta)

        #texto = f.read()

        #dict_viajes = ast.literal_eval(texto)


        viajes = {}

        datos_viajes = Query.ejec("SELECT a_origen.sede AS sede_origen, a_destino.sede AS sede_destino, aviones.modelo AS modelo,v.id AS id_viaje FROM viajes AS v LEFT JOIN aeropuertos AS a_origen  ON (  a_origen.id = v.id_origen) LEFT JOIN aeropuertos AS a_destino ON (  a_destino.id = v.id_destino ) LEFT JOIN aviones                  ON (  aviones.id  = v.id_avion)")



        for dato_viaje in datos_viajes:

            viaje = Viaje(Aeropuerto(dato_viaje[0]),Aeropuerto(dato_viaje[1]), Avion(dato_viaje[2]))
            print(dato_viaje)

            datos_billetes = Query.ejec(f"SELECT nombre, apellido1, apellido2 FROM billetes WHERE id_viaje = '{dato_viaje[3]}'")

            for dato_billete in datos_billetes:
                carga_billete = Billete()

                carga_billete.nombre    = dato_billete[0]
                carga_billete.apellido1 = dato_billete[1]
                carga_billete.apellido2 = dato_billete[2]

                viaje.billetes_comprados = carga_billete


            key = viaje.origen.sede + '-'+ viaje.destino.sede
        
            viajes[key] = viaje

        #exit
#
#
        #for key in dict_viajes:
        #    viaje = Viaje(Aeropuerto(dict_viajes[key]['origen']),Aeropuerto(dict_viajes[key]['destino']), Avion(dict_viajes[key]['avion']))
#
        #    for nbillete in dict_viajes[key]['billetes_comprados']:
        #        billete = dict_viajes[key]['billetes_comprados'][nbillete]
#
        #        carga_billete = Billete()
        #        carga_billete.nombre    = billete.get('nombre')
        #        carga_billete.apellidos = billete.get('apellidos')
        #        carga_billete.viaje     = billete.get('viaje')
#
        #        viaje.billetes_comprados = carga_billete
#
        #    viajes[key] = viaje

        print(viajes)

        return viajes

    def listado_viajes(self):
        self.destruir_frames()
        etiqueta_listado    = ttk.Label(self.frame, text="Filtro:"   ,justify="left",width=40,padding=[10]) 
        

        filtro  = ttk.Entry(self.frame, justify="left", textvariable=self.filtro)
        filtrar = ttk.Button(self.frame, text="Filtrar", command=self.filtrar)

        

        

        etiqueta_listado.pack  (side=TOP,fill=BOTH, expand=True, padx=5, pady=5)   
        filtro.pack            (side=TOP,fill=BOTH, expand=True, padx=5, pady=5)   
        filtrar.pack           (side=TOP,fill=BOTH, expand=True, padx=5, pady=5)   
        

        #self.frame_viajes = Frame(self.frame)  
        #self.frame_viajes.pack(side=TOP)
        # crear un treeview de viajes
        self.viaje = ttk.Treeview(self.frame, columns=('origen','destino','avion'))
        self.viaje.heading('#0', text='Viaje')
        self.viaje.heading('origen', text='Origen')
        self.viaje.heading('destino', text='Destino')
        self.viaje.heading('avion', text='Avion')
        self.viaje.pack(side=TOP,fill=BOTH, expand=True, padx=5, pady=5)
        self.viaje.pack()




        self.info_filtrar()

        
        
        #self.texto_listado.configure(justify="left")



    def info_billetes(self,viaje):

        dialogo = Toplevel()

        AgenciaDeViajes.posx_y += 50 
        tamypos = '400x300+'+str(AgenciaDeViajes.posx_y)+ '+'+ str(AgenciaDeViajes.posx_y)
        
        #dialogo.geometry(tamypos)
        self.scrollbar = ttk.Scrollbar(dialogo)
        self.scrollbar.pack(side="right", fill="y")

        self.treeview = ttk.Treeview(dialogo, columns=('nombre', 'apellidos') , yscrollcommand=self.scrollbar.set)

        self.treeview.heading("#0"        , text="Viaje")
        self.treeview.heading("nombre"    , text="Nombre")
        self.treeview.heading("apellidos" , text="Apellidos")

        for billete in viaje.billetes_comprados:
             self.treeview.insert(
                 ""
                 ,END
                 ,text= billete.viaje
                 ,values=(billete.nombre,billete.apellidos)
                  
             )
        
        self.treeview.bind("<<TreeviewSelect>>", self.item_selected)

        self.scrollbar.config(command=self.treeview.yview)



        self.treeview.pack()

        # texto_info_billetes = ''
        # for billete in viaje.billetes_comprados:
        #     texto_info_billetes += str(billete)

        # text = Text(dialogo)
        # text.pack()

        # text.insert("1.0", texto_info_billetes)


        dialogo.mainloop()


    def item_selected(self, event):
        item_selected = self.treeview.selection()[0]
        print(self.treeview.item(item_selected))

        

    def info_filtrar(self, texto_filtrado= ''):
        billetes = {}

        for key_viajes in self.viajes:

            contenido_viajes = str(self.viajes[key_viajes])

            

            if texto_filtrado == '' or texto_filtrado in contenido_viajes.lower():

                text_listado_viajes = str(self.viajes[key_viajes])

                labelframe    = LabelFrame(self.frame_viajes, text=key_viajes)
                texto_listado = Label(labelframe, text=text_listado_viajes, anchor="w",justify="left")

                billetes = ttk.Button(labelframe, text="Info Billetes", command=partial(self.info_billetes, self.viajes[key_viajes]))

                labelframe.pack        (side=TOP,fill=BOTH, expand=True, padx=5, pady=5)   
                texto_listado.pack(side=LEFT,fill=BOTH, expand=True, padx=5, pady=5)   
                billetes.pack(side=LEFT,fill=BOTH, expand=True, padx=5, pady=5)   


    def filtrar(self):
        self.destruir_frame_viajes()

        self.info_filtrar(self.filtro.get().lower())
#
        #text_listado_viajes = ''
#
        #for key_viajes in self.viajes:
        #    contenido_viajes = str(self.viajes[key_viajes])
        #    if self.filtro.get().lower() in contenido_viajes.lower():
        #        text_listado_viajes += contenido_viajes + "\n"
#
        #self.texto_listado = Label(self.labelframe, text=text_listado_viajes, anchor="w",justify="left")
        #self.texto_listado.pack(side=TOP,fill=BOTH, expand=True, padx=5, pady=5)   



     #def carga_externa(self):
     #    self.destruir_frames()
     #    etiqueta_carga    = ttk.Label(self.frame, text="Carga Externa:"   ,justify="left",width=40,padding=[10]) 
     #    etiqueta_carga.pack(side=TOP)   
 #
 #
     #    ruta_archivo = fd.askopenfilename(initialdir = "/",title = "Seleccione archivo",filetypes = (("txt files","*.txt"),("todos los archivos","*.*")))
 #
 #
     #    nuevos_viajes = self.leer_viajes(ruta_archivo)
 #
 #
     #    self.viajes.update(nuevos_viajes)
     #    self.guardar_fichero()

    def destruir_frame_viajes(self):
        for widget in self.frame_viajes.winfo_children():
            widget.destroy()

    def destruir_frames(self):
        for widget in self.frame.winfo_children():
            widget.destroy()


    # DECLARAR OTROS MÉTODOS DE LA APLICACIÓN:
  
    
# FUNCIONES DE LA APLICACIÓN
def f_verificar_iconos(iconos):
    ''' Verifica existencia de iconos
    iconos -- Lista de iconos '''
    for icono in iconos:
        if not os.path.exists(icono):
            print('Icono no encontrado:', icono)
            return(1)
        
    return(0)

def main():
    ''' Iniciar aplicación '''
    # INICIALIZAR VARIABLES CON RUTAS
    IMG_DIR = os.path.dirname(__file__) + os.sep + 'imagen' + os.sep

    # DECLARAR Y VERIFICAR ICONOS DE LA APLICACIÓN:
    iconos = (
         IMG_DIR + "plane_icon.png"
        ,IMG_DIR + "alta.png"
        ,IMG_DIR + "listado.png"
        ,IMG_DIR + "carga.png"
        ,IMG_DIR + "nuevo_viaje.png"
    )


    error1 = f_verificar_iconos(iconos)
    if not error1:
        mi_app = AgenciaDeViajes(iconos)

    return(0)
        
        
if __name__ == '__main__':
    main()



