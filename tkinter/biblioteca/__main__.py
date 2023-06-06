import os
import ast
import json

from tkinter import *
from tkinter import ttk, font, messagebox
from tkinter import filedialog as fd
import tkinter as tk


from biblioteca import Biblioteca
from editorial import Editorial


class GestionBiblioteca():
    
    ruta_guardado = os.path.dirname(__file__) + os.sep + 'bbdd' + os.sep + 'biblioteca.json'
    
    def __init__(self, iconos):
        
        self.iconos = iconos
        
        self.raiz = Tk()
        
        self.raiz.title('Gestión de Biblioteca')
        
        self.icono1 = PhotoImage(file = self.iconos[0])
        
        self.raiz.iconphoto(self.raiz, self.icono1)
        
        self.raiz.option_add("*Font", "Helvetica 12")
        self.raiz.option_add("*tearOff", False)
        
        self.raiz.minsize(400,300)
        
        self.fuente = font.Font(weight='normal')
        
        self.nombre_libro = StringVar(value="")
        self.editorial    = StringVar(value="")
        self.autor        = StringVar(value="")
        self.anho         = StringVar(value="")
        self.filtro       = StringVar(value="")
        
        self.libros = self.leer_libros()
        
        
        barramenu = Menu(self.raiz)
        self.raiz['menu'] = barramenu
        
        icono_alta          = PhotoImage(file=self.iconos[1])
        icono_listado       = PhotoImage(file=self.iconos[2])
        icono_carga_externa = PhotoImage(file=self.iconos[3])
        
        barramenu.add_command(
            label = 'Alta'
            ,command= self.alta_libro
            ,underline= 0
            ,accelerator='Ctrl+a'
            ,image = icono_alta
            ,compound=LEFT
        )
        
        barramenu.add_command(
            label = 'Listado'
            ,command= self.listado_libros
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
        
        self.frame = Frame(self.raiz)
        
        self.frame.config(bg="lightblue")
        
        self.frame.config(width=400, height=300)
        
        self.frame.pack(side=TOP)
        
        self.raiz.bind("<Control-a>", lambda event: self.alta_libro())
        self.raiz.bind("<Control-l>", lambda event: self.listado_libros())
        self.raiz.bind("<Control-o>", lambda event: self.carga_externa())
        
        
        self.raiz.mainloop()
        
    def destruir_frames_libros(self):
        for widget in self.frame_libros.winfo_children():
            widget.destroy()
            
    def destruir_frames(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
            
    def alta_libro(self):
        self.destruir_frames
        
        etiqueta_nombre_libro = ttk.Label(self.frame, text='Nombre Libro: ', justify='left', width=40, padding=[10])
        etiqueta_editorial = ttk.Label(self.frame, text='Editorial: ', justify='left', width=40, padding=[10])
        etiqueta_autor = ttk.Label(self.frame, text='Autor: ', justify='left', width=40, padding=[10])
        
        nombre_libro = ttk.Entry(self.frame, justify='left', textvariable=self.nombre_libro)
        autor = ttk.Entry(self.frame, justify='left', textvariable=self.autor)
        
        editorial = ttk.Combobox(self.frame, textvariable=self.editorial, values=Editorial.listado)
        editorial.set("Elija una opcion")
        
        label_frame_anho = tk.LabelFrame(self.frame, text="Año")
        
        guardar = ttk.Button(self.frame, text="Guardar", command=self.guardar_libro)
        
        etiqueta_nombre_libro.pack(side=TOP, fill=BOTH, padx=5, pady=5)
        nombre_libro.pack(side=TOP, fill=BOTH, padx=5, pady=5)
        etiqueta_editorial.pack(side=TOP, fill=BOTH, padx=5, pady=5)
        editorial.pack(side=TOP, fill=BOTH, padx=5, pady=5)
        etiqueta_autor.pack(side=TOP, fill=BOTH, padx=5, pady=5)
        autor.pack(side=TOP, fill=BOTH, padx=5, pady=5)
        
        label_frame_anho.pack(side=TOP, fill=BOTH, padx=5, pady=5)
        
        var_anho = tk.IntVar()
        
        anho1 = ttk.Radiobutton(label_frame_anho, text="2021", variable=var_anho, value=1)
        anho1.pack(padx=5, pady=5)
        
        anho2 = ttk.Radiobutton(label_frame_anho, text="2020", variable=var_anho, value=2)
        anho2.pack(padx=5, pady=5)
        
        anho3 = ttk.Radiobutton(label_frame_anho, text="2019", variable=var_anho, value=3)
        anho3.pack(padx=5, pady=5)
        
        anho4 = ttk.Radiobutton(label_frame_anho, text="2018", variable=var_anho, value=4)
        anho4.pack(padx=5, pady=5)
        
        anho5 = ttk.Radiobutton(label_frame_anho, text="2017", variable=var_anho, value=5)
        anho5.pack(padx=5, pady=5)
        
        anho6 = ttk.Radiobutton(label_frame_anho, text="2016", variable=var_anho, value=6)
        anho6.pack(padx=5, pady=5)
        
        guardar.pack(side=TOP, fill=BOTH, padx=5, pady=5)
        
        
    def guardar_libro(self):
        errores = False
        
        texto_errores = ''
        
        nuevo_libro = Biblioteca()
        nuevo_editorial = Editorial()
        
        try:
            nuevo_libro.libro = self.nombre_libro.get()
        except:
            errores = True
            texto_errores += "- No se ha insertado un libro"
            
            
        try:
            nuevo_editorial.editorial = self.editorial.get()
        except:
            errores = True
            texto_errores += "- No se ha seleccionado un editorial"
        
            
        try:
            nuevo_libro.autor = self.autor.get()
        except:
            errores = True
            texto_errores += "- No se ha insertado un autor"
            
        if errores:
            messagebox.showerror("Hay errores en el formulario", texto_errores)
            
        else:
            self.guardar_fichero()
            messagebox.showinfo("Agregado", "Se ha guardado el libro con exito")
            
    def guardar_fichero(self):
        f = open(self.ruta_guardado,'w')
        
        dict_libros = {}
        
        for libro in self.libros:
            dict_libros.update(self.libros[libro].diccionario())
            
        f.write(json.dumps(dict_libros, indent=4))
    
    
    
    
    
    
    
    def listado_libros(self):
        self.destruir_frames()
        
        etiqueta_filtrar = ttk.Label(self.frame, text="Filtrar:", justify="left", width=40, padding=[10])
        etiqueta_listado = ttk.Label(self.frame, text="Listado de libros:", justify="left", width=40, padding=[10])
        
        filtro = ttk.Entry(self.frame, justify="left", textvariable=self.filtro)
        filtrar = ttk.Button(self.frame, text="Filtrar", command=self.filtrar)
        
        self.frame_libros = Frame(self.frame)
        
        etiqueta_filtrar.pack(side=TOP, fill=BOTH, padx=5, pady=5)
        filtro.pack(side=TOP, fill=BOTH, padx=5, pady=5)
        filtrar.pack(side=TOP, fill=BOTH, padx=5, pady=5)
        etiqueta_listado.pack(side=TOP, fill=BOTH, padx=5, pady=5)
        self.frame_libros.pack(side=TOP)
        
        self.info_filtrar()
        
    def filtrar(self):
        self.destruir_frames_libros()
        self.info_filtrar(self.filtro.get())
        
    def info_filtrar(self, texto_filtrado = ""):
        
        scrollbar = Scrollbar(self.frame_libros)
        scrollbar.pack(side="right", fill='y')
        
        self.treeview_libros = ttk.Treeview(self.frame_libros, columns=('autor', 'editorial', 'anho'), yscrollcommand=scrollbar.set)
        
        self.treeview_libros.heading('#0', text="Nombre")
        self.treeview_libros.heading('autor', text="Autor")
        self.treeview_libros.heading('editorial', text="Editorial")
        self.treeview_libros.heading('anho', text="Año")
        
        for key_libros in self.libros:
            contenido_libros = str(self.libros[key_libros])
            
            if texto_filtrado == '' or texto_filtrado.lower() in contenido_libros.lower():
                
                self.treeview_libros.insert(
                    ""
                    ,END
                    ,text=self.libros[key_libros].nombre
                )
    
    
    
    
    def carga_externa(self):
        self.destruir_frames()
        
        ruta_datos_externos = fd.askopenfilename(initialdir="/", title="Seleccione archivo de carga externa", filetypes=(("json files","*.json"), ("todos los archivos", "*.*")))
        
        libros_externos = self.leer_libros(ruta_datos_externos)
        
        self.libros.update(libros_externos)
        
        self.guardar_fichero()
    
    def leer_libros(self, ruta = ruta_guardado):
        
        f = open(ruta, 'r')
        
        texto = f.read()
        
        dict_libros = ast.literal_eval(texto)
        
        libros = {}
        
        for key in dict_libros:
            
            dict_libros[key]
            
            libro = Biblioteca(dict_libros[key]['libro'], dict_libros[key]['autor'], Editorial(dict_libros[key]['editorial']), dict_libros[key]['anho'])
            
            for nlibro in dict_libros[key]['editoria']:
                nuevo_libro = dict_libros[key]['editorial'][nlibro]
                
                carga_libro = Biblioteca()
                
                carga_libro.libro = nuevo_libro.get('libro')
                carga_libro.autor = nuevo_libro.get('autor')
                carga_libro.editorial = nuevo_libro.get('editorial')
                carga_libro.anho = nuevo_libro.get('anho')
                
                libro.editorial = carga_libro
                
            libros[key] = libro
        
        print(libros)
        
        return libros
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

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
        ,IMG_DIR + 'listado.png'
        ,IMG_DIR + 'carga.png'
    )
    
    
    not_error = verificar_iconos(iconos)
    
    if not_error:
        print("ejecucion con exito")
        mi_app = GestionBiblioteca(iconos)
        
        
    return 0

if __name__ == '__main__':
    main()