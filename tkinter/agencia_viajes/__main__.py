from aeropuerto import Aeropuerto
from avion import Avion
from billete import Billete
from viaje import Viaje

import os
import ast
from tkinter import *
from tkinter import ttk, font, messagebox
from tkinter import filedialog as fd
import json


class AgenciaDeViajes():
    
    ruta_guardado = os.path.dirname(__file__) + os.sep + 'bbdd' + os.sep + 'viajes.json'
    
    
    def __init__(self, iconos):

        
        self.iconos = iconos
        
        self.raiz = Tk()
        
        self.raiz.title("Agencia de Viajes")
        
        self.icono1 = PhotoImage(file=self.iconos[0]) 
        self.raiz.iconphoto(self.raiz, self.icono1) 
        
        self.raiz.option_add('*Font', 'Helvetica 12')
        self.raiz.option_add('*tearOff', False) 
        
        self.raiz.minsize(500,300)
        
        self.fuente = font.Font(weight='normal')
        
        """
        Declarar variables para opciones predeterminadas:
        (Estos valores se podrian leer de un archivo de 
        configuración)
        """
        self.nombre     = StringVar(value="")
        self.apellidos  = StringVar(value="")
        self.viaje      = StringVar(value="")
        self.origen     = StringVar(value="")
        self.destino    = StringVar(value="")
        self.avion      = StringVar(value="")
        self.filtro     = StringVar(value="")
        
        
        self.viajes = self.leer_viajes()
        
        
        # Definir barra de menu de la aplicacion:
        barramenu = Menu(self.raiz)
        self.raiz['menu'] = barramenu
        
        # Definir submenus
        icono2 = PhotoImage(file=self.iconos[1])
        icono3 = PhotoImage(file=self.iconos[2])
        icono4 = PhotoImage(file=self.iconos[3])
        icono5 = PhotoImage(file=self.iconos[4])
        icono6 = PhotoImage(file=self.iconos[5])
        
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
            label         = "Nuevo Viaje"
            ,command      = self.nuevo_viaje
            ,underline    = 0
            ,accelerator  = 'Ctrl+o'
            ,image        = icono5
            ,compound     =LEFT
        )
        
        barramenu.add_command(
             label        = 'Salir'
            ,command      = self.salir
            ,underline    = 0
            ,accelerator  = "Ctrl+s"
            ,image        = icono6
            ,compound     = LEFT
        )
        
        # Creamos el frame donde vamos a colocar el Alta y el listado de viajes
        self.frame = Frame(self.raiz)
        
        self.frame.config(bg='lightblue')
        
        self.frame.config(width=500, height=300)
        self.frame.pack(side=TOP)
        
        # Declarar teclas de acceso rapido:
        self.raiz.bind("<Control-a>", lambda event: self.alta_billete())
        self.raiz.bind("<Control-l>", lambda event: self.listado_viajes())
        self.raiz.bind("<Control-c>", lambda event: self.carga_externa())
        self.raiz.bind("<Control-o>", lambda event: self.nuevo_viaje())
        self.raiz.bind("<Control-s>", lambda event: self.salir())
        
        self.raiz.mainloop()
        
        
        
        
    def destruir_frames_viajes(self):
        for widget in self.frame_viajes.winfo_children():
            widget.destroy()
        
    def destruir_frames(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
            

        
    def leer_viajes(self, ruta = ruta_guardado):
        f = open(ruta, 'r')
        
        texto = f.read()
        
        dict_viajes = ast.literal_eval(texto)
        
        viajes = {}
        
        for key in dict_viajes:
            
            dict_viajes[key]
            
            viaje = Viaje(Aeropuerto(dict_viajes[key]['origen']),Aeropuerto(dict_viajes[key]['destino']),Avion(dict_viajes[key]['avion']))
            
            for nbillete in dict_viajes[key]['billetes_comprados']:
                billete = dict_viajes[key]['billetes_comprados'][nbillete]
                
                carga_billete = Billete()
                
                carga_billete.nombre    = billete.get('nombre')
                carga_billete.apellidos = billete.get('apellidos')
                carga_billete.viaje     = billete.get('viaje')
                
                viaje.billetes_comprados = carga_billete
            
            viajes[key] = viaje
        
        print(viajes)
        
        return viajes
    
    def guardar_billete(self):
        errores = False
        
        texto_errores = ''
        
        nuevo_billete = Billete()
        
        try:
            nuevo_billete.viaje = self.viaje.get()
        except:
            errores = True
            texto_errores += ' - No se ha seleccionado ningun viaje\n'
        else:
            viaje_seleccionado = self.viajes.get(nuevo_billete.viaje)
            
        try:
            nuevo_billete.nombre = self.nombre.get()
        except:
            errores = True
            texto_errores += ' - No se ha escrito un nombre.\n'
            
        try:
            nuevo_billete.apellidos = self.apellidos.get()
        except:
            errores = True
            texto_errores += ' - No se ha escrito unos apellidos.\n'
            
        try:
            viaje_seleccionado.billetes_comprados = nuevo_billete
        except Exception as error:
            errores = True
            texto_errores += error.args[1]
            
            
            
        if errores:
            messagebox.showerror('Hay errores en el formulario', texto_errores)
        else:
            self.viajes[nuevo_billete.viaje] = viaje_seleccionado
            self.guardar_fichero()
            messagebox.showinfo("Agregado", "Se ha guardado el billete con éxito")
        
        
        
    def alta_billete(self):
        
        # Introducir datos del Usuario
        self.destruir_frames()
        
        opciones = self.viajes.keys()
        
        etiqueta_viajes    = ttk.Label(self.frame, text='Viajes:', justify='left', width=40, padding=[10])
        etiqueta_nombre    = ttk.Label(self.frame, text='Nombre', justify='left', width=40, padding=[10])
        etiqueta_apellidos = ttk.Label (self.frame, text='Apellidos', justify='left', width=40, padding=[10])
        
        
        select_viajes = OptionMenu(self.frame, self.viaje, *opciones)
        
        nombre = ttk.Entry(self.frame, justify='left', textvariable=self.nombre)
        apellidos = ttk.Entry(self.frame, justify='left', textvariable=self.apellidos)
        
        guardar = ttk.Button(self.frame, text='Guardar', command=self.guardar_billete)
        
        
        etiqueta_viajes.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
        select_viajes.pack(side=TOP, fill=BOTH, padx=5, pady=5)
        
        etiqueta_nombre.pack(side=TOP, fill=BOTH, padx=10, pady=5)
        nombre.pack(side=TOP, fill=X,padx=10, pady=5)
        
        etiqueta_apellidos.pack(side=TOP, fill=BOTH,padx=10, pady=5)
        apellidos.pack(side=TOP, fill=X, padx=10, pady=5)
        
        guardar.pack(side=TOP, fill=BOTH, padx=5, pady=5)

    
    def listado_viajes(self):
        self.destruir_frames()
        
        etiqueta_filtro = ttk.Label(self.frame, text='Filtro:', justify='left', width=40, padding=[10])
        etiqueta_filtro.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
        
        filtro = ttk.Entry(self.frame, justify='left', textvariable=self.filtro)
        filtro.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
        
        filtrar = ttk.Button(self.frame, text="Filtrar", command=self.filtrar)
        filtrar.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
        
        etiqueta_listado = ttk.Label(self.frame, text="Listado de viajes:", justify="left", width=40, padding=[10])
        etiqueta_listado.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
        
        
        self.frame_viajes = Frame(self.frame)
        self.frame_viajes.pack(side=TOP)
        
        
        self.info_filtrar()
        
        
    def info_filtrar(self, texto_filtrado =""):
        
        scrollbar = Scrollbar(self.frame_viajes)
        scrollbar.pack(side="right", fill="y")
        
        self.treeview_viajes = ttk.Treeview(self.frame_viajes, columns=('destino', 'avion', 'capacidad'), yscrollcommand= scrollbar.set)
        
        self.treeview_viajes.heading("#0"       , text="Origen")
        self.treeview_viajes.heading("destino"  , text="Destino")
        self.treeview_viajes.heading("avion"    , text="Avion")
        self.treeview_viajes.heading("capacidad", text="Capacidad")
        
        for key_viajes in self.viajes:
            contenido_viajes = str(self.viajes[key_viajes])
            
            if texto_filtrado == '' or texto_filtrado.lower() in contenido_viajes.lower():
                
                self.treeview_viajes.insert(
                      ""
                    , END
                    , text=self.viajes[key_viajes].origen.sede
                    , values=(self.viajes[key_viajes].destino.sede, self.viajes[key_viajes].avion.modelo, self.viajes[key_viajes].avion.capacidad)
                )
                
        scrollbar.config(command=self.treeview_viajes.yview)
        self.treeview_viajes.pack()
    
    def filtrar(self):
        self.destruir_frames_viajes()
        
        self.info_filtrar(self.filtro.get())
                
                
        
    def carga_externa(self):
        self.destruir_frames()
        
        ruta_datos_externos = fd.askopenfilename(initialdir="/", title="Seleccione archivo de carga externa", filetypes=(("json files","*.json"), ("todos los archivos", "*.*")))
        
        viajes_externos = self.leer_viajes(ruta_datos_externos)
        
        self.viaje.update(viajes_externos)
        
        self.guardar_fichero()
        
    
    def nuevo_viaje(self):
        self.destruir_frames()
        
        etiqueta_origen  = ttk.Label(self.frame, text="Origen: ", justify="left", width=40, padding=[10])
        etiqueta_destino = ttk.Label(self.frame, text="Destino: ", justify="left", width=40, padding=[10])
        etiqueta_avion   = ttk.Label(self.frame, text="Avion: ", justify="left", width=40, padding=[10])
        
        select_origen  = OptionMenu(self.frame, self.origen, *Aeropuerto.listado)
        select_destino = OptionMenu(self.frame, self.destino, *Aeropuerto.listado)
        select_avion   = OptionMenu(self.frame, self.avion, *Avion.modelos.keys())
        
        guardar = ttk.Button(self.frame, text="Guardar", command=self.guardar_viaje())
        
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
            texto_errores += "- No se ha especificado un origen.\n"
        if not self.destino.get():
            texto_errores += "- No se ha especificado un destino.\n"
        if not self.avion.get():
            texto_errores += "- No se ha especificado un avion.\n"
        if self.origen.get() and self.origen.get() == self.destino.get():
            texto_errores += "- Origen, no puede ser igual a destino.\n"
        if self.viajes.get(self.origen.get() + '-' + self.destino.get()):
            texto_errores += "- El viaje ya se encuentra en nuestra BBDD.\n"
            
        if texto_errores:
            messagebox.showerror("Hay errores en el formulario", texto_errores)
        else:
            viaje = Viaje(Aeropuerto(self.origen.get()), Aeropuerto(self.destino.get()), Avion(self.avion.get()))
            self.viajes[self.origen.get() + '-' + self.destino.get()] = viaje
            self.guardar_fichero()
            messagebox.showinfo("Exito", "Viaje creado correctamente")
            
    
    def guardar_fichero(self):
        f = open(self.ruta_guardado,'w')

        dict_viajes = {}

        for viaje in self.viajes:
            dict_viajes.update(self.viajes[viaje].diccionario())

        f.write(json.dumps(dict_viajes, ident=4))

    
        
    def salir(self):
        self.destruir_frames()
        self.abrir_ventana()
        
        etiqueta_salir = ttk.Label(self.frame, text='Si quiere salir, vuelva pulsar el boton salir.', justify='left', width=40, padding=[10])
        etiqueta_salir.pack(side=TOP)
        

            
    def abrir_ventana(self):
        
        self.ventana = Toplevel()

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

def verificar_iconos(iconos):

    for icono in iconos:
        if not os.path.exists(icono):
            return False
        
    return True

def main():
    
    
    print("La ruta de la carpeta esta en: ", os.path.dirname(__file__))
    
    IMG_DIR = os.path.dirname(__file__) + os.sep + 'imagenes' + os.sep
    
    # declarar y verificar iconos de la aplicacion:
    iconos = (
         IMG_DIR + "icono-app.png"
        ,IMG_DIR + "alta.png"
        ,IMG_DIR + "listado.png"
        ,IMG_DIR + "cargar.png"
        ,IMG_DIR + "conec32x32.png"
        ,IMG_DIR + "salir32x32.png"
    )
    
    not_error = verificar_iconos(iconos)
    
    if not_error:
        print("Entrada con éxito")
        mi_app = AgenciaDeViajes(iconos)
        
    return 0

if __name__ == '__main__':
    main()