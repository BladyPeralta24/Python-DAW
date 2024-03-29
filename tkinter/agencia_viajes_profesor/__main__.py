
import os

import ast

from tkinter import *
from tkinter import ttk, font, messagebox
from aeropuerto import Aeropuerto
from avion import Avion
from billete import Billete
from viaje import Viaje

from tkinter import filedialog as fd

from bbdd import Query
import json

class AgenciaDeViaje():
    
    
    ruta_guardado = os.path.dirname(__file__) + os.sep + 'bbdd' + os.sep + 'viajes.json'
    
    
    def __init__(self,iconos):
        
        self.iconos = iconos
        
        self.raiz = Tk()
        
        self.raiz.title("Agencia de viajes: El corte Francés")
        
        
        self.icono1= PhotoImage(file= self.iconos[0]) #Icono de la app
        
        self.raiz.iconphoto(self.raiz, self.icono1)
        
        self.raiz.option_add("*Font", "Helvetica 12")
        self.raiz.option_add("*tearOff", False)
        
        self.raiz.minsize(400,300)
        
        #self.raiz.attributes('-fullscreen', True)
        
        self.fuente = font.Font(weight='normal')
        
        
        #DECLARAR StringsVars
        
        self.nombre    = StringVar(value="")
        self.apellidos = StringVar(value="")
        self.viaje     = StringVar(value="")
        self.origen    = StringVar(value="")
        self.destino   = StringVar(value="")
        self.avion     = StringVar(value="")
        self.filtro    = StringVar(value="")
        
        
        self.viajes = self.leer_viajes()
        
        barramenu = Menu(self.raiz)
        
        self.raiz['menu'] = barramenu
        
        icono_alta          = PhotoImage(file=self.iconos[1])
        icono_listado       = PhotoImage(file=self.iconos[2])
        icono_carga_externa = PhotoImage(file=self.iconos[3])
        icono_nuevo_viaje = PhotoImage(file=self.iconos[4])
        
        barramenu.add_command(
            label = 'Alta'
            ,command= self.alta_billete
            ,underline= 0
            ,accelerator='Ctrl+a'
            ,image = icono_alta
            ,compound=LEFT
        )
        
        barramenu.add_command(
            label = 'Listado'
            ,command= self.listado_viajes
            ,underline= 0
            ,accelerator='Ctrl+l'
            ,image = icono_listado
            ,compound=LEFT
        )
        
        barramenu.add_command(
            label = 'Carga Externa'
            ,command= self.carga_externa
            ,underline= 0
            ,accelerator='Ctrl+o'
            ,image = icono_carga_externa
            ,compound=LEFT
        )
        
        barramenu.add_command(
            label = 'Nuevo Viaje'
            ,command= self.nuevo_viaje
            ,underline= 0
            ,accelerator='Ctrl+n'
            ,image = icono_nuevo_viaje
            ,compound=LEFT
        )
        
        
        self.frame = Frame(self.raiz)
        
        self.frame.config(bg="lightblue")
        
        self.frame.config(width=400, height=300)
        
        self.frame.pack(side=TOP)
        
        
        self.raiz.bind("<Control-a>", lambda event: self.alta_billete())
        self.raiz.bind("<Control-l>", lambda event: self.listado_viajes())
        self.raiz.bind("<Control-o>", lambda event: self.carga_externa())
        
        
        
        self.raiz.mainloop()

    def destruir_frames_viajes(self):
        for widget in self.frame_viajes.winfo_children():
            widget.destroy()
            
    def destruir_frames(self):
        
        for widget in self.frame.winfo_children():
            widget.destroy()
        
    def alta_billete(self):
        self.destruir_frames()
        
        etiqueta_viajes    = ttk.Label(self.frame , text="Viajes: "   , justify="left", width=40, padding=[10])
        etiqueta_nombre    = ttk.Label(self.frame , text="Nombre: "   , justify="left", width=40, padding=[10])
        etiqueta_apellidos = ttk.Label(self.frame , text="Apellidos: ", justify="left", width=40, padding=[10])
        
        opciones = self.viajes.keys()
        
        
        select_viajes = OptionMenu(self.frame, self.viaje, *opciones)
        
        
        nombre    = ttk.Entry(self.frame, justify="left", textvariable=self.nombre)
        apellidos = ttk.Entry(self.frame, justify="left", textvariable=self.apellidos)
        
        
        guardar = ttk.Button(self.frame, text="Guardar", command=self.guardar_billete)
        
        etiqueta_viajes.pack(side=TOP, fill=BOTH, padx=5, pady=5)
        select_viajes.pack(side=TOP, fill=BOTH, padx=5, pady=5)
        etiqueta_nombre.pack(side=TOP, fill=BOTH, padx=5, pady=5)
        nombre.pack(side=TOP, fill=BOTH, padx=5, pady=5)
        etiqueta_apellidos.pack(side=TOP, fill=BOTH, padx=5, pady=5)
        apellidos.pack(side=TOP, fill=BOTH, padx=5, pady=5)
        guardar.pack(side=TOP, fill=BOTH, padx=5, pady=5)
        
        
    def guardar_billete(self):
        errores = False
        
        texto_errores = ''
        
        nuevo_billete = Billete()
        
        try:
            nuevo_billete.viaje = self.viaje.get()
        except:
            errores = True
            texto_errores += " - No se ha seleccionado ningún viaje\n "
        else:
            viaje_seleccionado = self.viajes.get(nuevo_billete.viaje)

        try:
            nuevo_billete.nombre = self.nombre.get()
        except:
            errores = True
            texto_errores += ' -  No se ha escrito un nombre.\n'
            
        try:
            nuevo_billete.apellidos = self.apellidos.get()
        except:
            errores = True
            texto_errores += ' -  No se ha escrito unos apellidos.\n'
            
            
        try:
            viaje_seleccionado.billetes_comprados = nuevo_billete
        except Exception as error:
            errores = True
            texto_errores += error.args[1]
            
        

        
        
        if errores:
            messagebox.showerror("Hay errores en el formulario", texto_errores)
        else:
            self.viajes[nuevo_billete.viaje] = viaje_seleccionado
            self.guardar_fichero()
            messagebox.showinfo("Agregado", "Se ha guardado el billete con éxito")
    
    def guardar_fichero(self):
        f = open(self.ruta_guardado,'w')
        
        dict_viajes = {}
        
        for viaje in self.viajes: 
            dict_viajes.update(self.viajes[viaje].diccionario())
        #hace lo mismo    
        # for key_viaje, viaje in self.viajes.items(): 
            # dict_viajes.update(viaje.diccionario())
            
        f.write(json.dumps(dict_viajes, indent=4))
            
    
    def listado_viajes(self):
        self.destruir_frames()
        
        etiqueta_filtro    = ttk.Label(self.frame , text="Filtro: "             , justify="left", width=40, padding=[10])
        etiqueta_listado   = ttk.Label(self.frame , text="Listado de viajes: "  , justify="left", width=40, padding=[10])
        
        filtro  = ttk.Entry(self.frame, justify="left", textvariable=self.filtro)
        filtrar = ttk.Button(self.frame, text="Filtrar", command=self.filtrar)
        
        self.frame_viajes = Frame(self.frame)
        
        etiqueta_filtro.pack(side=TOP, fill=BOTH, padx=5, pady=5)
        filtro.pack(side=TOP, fill=BOTH, padx=5, pady=5)
        filtrar.pack(side=TOP, fill=BOTH, padx=5, pady=5)
        etiqueta_listado.pack(side=TOP, fill=BOTH, padx=5, pady=5)      
        self.frame_viajes.pack(side=TOP)
        
        
        self.info_filtrar()
        
    def info_filtrar(self, texto_filtrado=""):
  
       
        scrollbar = Scrollbar(self.frame_viajes)
        scrollbar.pack(side="right",fill="y")
        
        self.treeview_viajes = ttk.Treeview(self.frame_viajes,  columns=('destino', 'avion', 'capacidad'), yscrollcommand= scrollbar.set)
        
        self.treeview_viajes.heading("#0"       , text="Origen")
        self.treeview_viajes.heading("destino"  , text="Destino")
        self.treeview_viajes.heading("avion"    , text="Avión")
        self.treeview_viajes.heading("capacidad", text="Capacidad")
        
        
        for key_viajes in self.viajes:
            contenido_viajes = str(self.viajes[key_viajes])
            
            if texto_filtrado == '' or texto_filtrado.lower() in contenido_viajes.lower():
            
                self.treeview_viajes.insert(
                        ""
                    ,END
                    ,text=self.viajes[key_viajes].origen.sede
                    ,values=(self.viajes[key_viajes].destino.sede, self.viajes[key_viajes].avion.modelo, self.viajes[key_viajes].avion.capacidad)
                )
        
        scrollbar.config(command=self.treeview_viajes.yview)
        self.treeview_viajes.pack()
        
        
        
        # dialogo = Toplevel()

        # AgenciaDeViajes.posx_y += 50 
        # tamypos = '400x300+'+str(AgenciaDeViajes.posx_y)+ '+'+ str(AgenciaDeViajes.posx_y)
        
        # #dialogo.geometry(tamypos)
        # self.scrollbar = ttk.Scrollbar(dialogo)
        # self.scrollbar.pack(side="right", fill="y")

        # self.treeview = ttk.Treeview(dialogo, columns=('nombre', 'apellidos') , yscrollcommand=self.scrollbar.set)

        # self.treeview.heading("#0"        , text="Viaje")
        # self.treeview.heading("nombre"    , text="Nombre")
        # self.treeview.heading("apellidos" , text="Apellidos")

        # for billete in viaje.billetes_comprados:
        #      self.treeview.insert(
        #          ""
        #          ,END
        #          ,text= billete.viaje
        #          ,values=(billete.nombre,billete.apellidos)
                  
        #      )
        
        # self.treeview.bind("<<TreeviewSelect>>", self.item_selected)

        # self.scrollbar.config(command=self.treeview.yview)



        # self.treeview.pack()

        # # texto_info_billetes = ''
        # # for billete in viaje.billetes_comprados:
        # #     texto_info_billetes += str(billete)

        # # text = Text(dialogo)
        # # text.pack()

        # # text.insert("1.0", texto_info_billetes)


        # dialogo.mainloop()
        
    
    def filtrar(self):
        self.destruir_frames_viajes()
        
        self.info_filtrar(self.filtro.get())
    
    def carga_externa(self):
        self.destruir_frames()
        
        ruta_datos_externos = fd.askopenfilename(initialdir="/", title="Seleccione archivo de carga externa", filetypes=(("json files","*.json"), ("todos los archivos", "*.*")))
        
        viajes_externos = self.leer_viajes(ruta_datos_externos)
        
        self.viajes.update(viajes_externos)
        
        self.guardar_fichero()
        
        #self.viajes

        
    
    def nuevo_viaje(self):
        self.destruir_frames()
        
        etiqueta_origen  = ttk.Label(self.frame , text="Origen: " , justify="left", width=40, padding=[10])
        etiqueta_destino = ttk.Label(self.frame , text="Destino: " , justify="left", width=40, padding=[10])
        etiqueta_avion   = ttk.Label(self.frame , text="Avión: " , justify="left", width=40, padding=[10])
        
        # select_origen  = OptionMenu(self.frame, self.origen, *Aeropuerto.listado)
        # select_destino = OptionMenu(self.frame, self.destino, *Aeropuerto.listado)
        # select_avion   = OptionMenu(self.frame, self.avion, *Avion.modelos.keys())
        
        select_origen  = ttk.Combobox(self.frame, textvariable=self.origen, values= Aeropuerto.listado)
        select_origen.set("Elija una opcion")
        select_destino = ttk.Combobox(self.frame, textvariable=self.destino, values= Aeropuerto.listado)
        select_destino.set("Elija una opcion")
        select_avion   = ttk.Combobox(self.frame, textvariable=self.avion, values = list(Avion.modelos.keys()))
        select_avion.set("Elija una opcion")
        
        guardar = ttk.Button(self.frame, text="Guardar", command=self.guardar_viaje)
        
        
        etiqueta_origen.pack(side=TOP, fill=BOTH, padx=5, pady=5)
        select_origen.pack(side=TOP, fill=BOTH, padx=5, pady=5)
        etiqueta_destino.pack(side=TOP, fill=BOTH, padx=5, pady=5)
        select_destino.pack(side=TOP, fill=BOTH, padx=5, pady=5)
        etiqueta_avion.pack(side=TOP, fill=BOTH, padx=5, pady=5)
        select_avion.pack(side=TOP, fill=BOTH, padx=5, pady=5)
        guardar.pack(side=TOP, fill=BOTH, padx=5, pady=5)
    
    
    def guardar_viaje(self):
        texto_errores = ''
        
        if not self.origen.get():
            texto_errores += " - No se ha especificado un origen.\n"
        if not self.destino.get():
            texto_errores += " - No se ha especificado un destino.\n"
        if not self.avion.get():
            texto_errores += " - No se ha especificado un avion.\n"
        if self.origen.get() and self.origen.get() == self.destino.get():
            texto_errores += " - Origen, no puede ser igual a destino.\n"
        if self.viajes.get(self.origen.get() + '-' + self.destino.get()):
            texto_errores += " - El viaje ya se encuentra en nuestra BBDD.\n"
            
        if texto_errores:
            messagebox.showerror("Hay errores en el formulario", texto_errores)
        else:
            viaje = Viaje(Aeropuerto(self.origen.get()),Aeropuerto(self.destino.get()), Avion(self.avion.get()))
            self.viajes[self.origen.get() + '-' + self.destino.get()] = viaje
            self.guardar_fichero()
            messagebox.showinfo("Éxito", "Viaje creado con éxito")
    
    def leer_viajes(self, ruta = ruta_guardado):
        
        # f = open(ruta,'r')
        
        # texto = f.read()
        
        # dict_viaje = ast.literal_eval(texto)
        
        
        # viajes = {}
        
        # for key  in dict_viaje:
            
            
        #     dict_viaje[key]
            
        #     viaje = Viaje(Aeropuerto(dict_viaje[key]['origen']),Aeropuerto(dict_viaje[key]['destino']),Avion(dict_viaje[key]['avion']))
        
        #     for nbillete in dict_viaje[key]['billetes_comprados']:
        #         billete = dict_viaje[key]['billetes_comprados'][nbillete]
                
        #         carga_billete = Billete()
                
        #         carga_billete.nombre    = billete.get('nombre')
        #         carga_billete.apellidos = billete.get('apellidos')
        #         carga_billete.viaje     = billete.get('viaje')
                
        #         viaje.billetes_comprados = carga_billete
    
        #     viajes[key] = viaje
        
        # print(viajes)    
        
        # return viajes
        
        viajes = []
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
            
        print(viajes)
        
        return viajes
    
def verificar_iconos(iconos):
    
    for icono in iconos:
        if not os.path.exists(icono):
            return False
        
        
    return True
    
def main():
    
    IMG_DIR = os.path.dirname(__file__) + os.sep + 'imagen' + os.sep


    iconos = (
        IMG_DIR + 'plane_icon.png'
        ,IMG_DIR + 'alta.png'
        ,IMG_DIR + 'carga.png'
        ,IMG_DIR + 'nuevo_viaje.png'
        ,IMG_DIR + 'listado.png'
    )
    
    
    not_error = verificar_iconos(iconos)
    
    if not_error:
        print("asdfasfdas")
        mi_app = AgenciaDeViaje(iconos)
        
        
    return 0

if __name__ == '__main__':
    main()