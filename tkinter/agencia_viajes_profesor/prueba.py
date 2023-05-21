
import os

# import ast

from tkinter import *
from tkinter import ttk, font, messagebox
# from aeropuerto import Aeropuerto
# from avion import Avion
# from billete import Billete
# from viaje import Viaje


class AgenciaDeViaje():
    
    
    ruta_guardado = os.path.dirname(__file__) + os.sep + 'bbdd' + os.sep + 'viajes.json'
    
    
    def __init__(self,iconos):
        
        self.iconos = iconos
        
        self.raiz = Tk()
        
        self.raiz.title("Agencia de viajes: El corte Francés")
        
        
        self.icono1= PhotoImage(file= self.iconos[0]) #Icono de la app
        
        # self.raiz.iconphoto(self.raiz, self.icono1)
        
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
        icono_nuevo_viaje   = PhotoImage(file=self.iconos[4])
        
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

    
    def alta_billete(self):
        pass
        
    def guardar_billete(self):
        pass
    
    def listado_viajes(self):
        pass
    
    def carga_externa(self):
        pass
    
    def leer_viajes(self):
        pass
    
    
    
    
    
    
    
    
    
def verificar_iconos(iconos):
    
    for icono in iconos:
        if not os.path.exists(icono):
            
            return False
        
        
    return True
    

    
def main():
    """ Iniciar aplicacion """
    # app_carpeta = os.path.dirname(__file__)
    
    IMG_DIR = os.path.dirname(__file__) + os.sep + 'imagenes' + os.sep
    
    print("La ruta de la carpeta esta en: ", os.path.dirname(__file__))
    
    # declarar y verificar iconos de la aplicacion:
    iconos = (
         IMG_DIR + "icono-app.png"
        ,IMG_DIR + "alta.png"
        ,IMG_DIR + "listado.png"
        ,IMG_DIR + "cargar.png"
        ,IMG_DIR + "salir32x32.png"
    )
    
    error1 = verificar_iconos(iconos)
    
    if not error1:
        mi_app = AgenciaDeViaje(iconos)
    return(0)



if __name__ == '__main__':
    main()