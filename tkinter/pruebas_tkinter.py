from tkinter import *
from tkinter import ttk, font

#importar getpass solo para probrar:
import getpass


# PRIMERA APLICACION CON TKINTER

# definir la ventana principal de la aplicacion
"""raiz = Tk()"""

# Definir las dimensiones de la ventana, que se ubicará
# en el centro de la pantalla
"""raiz.geometry('300x200')""" # anchura y altura

# Asignar un color de fondo a la ventana. si se omite, el fondo será gris
"""raiz.configure(bg = 'beige')"""
# Asignar un título a la ventana
"""raiz.title('Aplicacion')"""
# Define un botón en la parte inferior de la ventana
# que cuando sea presionado hará que termine el programa.
# El primer parámetro indica el nombre de la ventana 'raiz'
# donde se ubicará el botón
"""ttk.Button(raiz, text='Salir', command=quit).pack(side=BOTTOM)"""
# Después de definir la ventana principal y un widget botón
# la siguiente línea hará que cuando se ejecute el programa
# construya y muestre la ventana, quedando a la espera de
# que alguna persona interactúe con ella.
# Si la persona presiona sobre el botón Cerrar 'X', o bien,
# sobre el botón 'Salir' el programa llegará a su fin.
"""raiz.mainloop()"""


# APLICACION ORIENTADA A OBJETOS

# Crea una clase Python para definir el interfaz de usuario de
# la aplicación. Cuando se cree un objeto del tipo 'Aplicacion'
# se ejecutará automáticamente el método __init__() qué
# construye y muestra la ventana con todos sus widgets:
"""class Aplicacion():
    
    def __init__(self):
        raiz = Tk()
        
        raiz.geometry('300x200')
        
        raiz.configure(bg = 'blue')
        
        raiz.title('Aplicacion')
        
        ttk.Button(raiz, text='Salir', command=raiz.destroy).pack(side=BOTTOM)
        
        raiz.mainloop()"""
        

# Define la función main() que es en realidad la que indica
# el comienzo del programa. Dentro de ella se crea el objeto
# aplicación 'mi_app' basado en la clase 'Aplicación':
"""def main():
    mi_app = Aplicacion()
    return 0"""

# Mediante el atributo __name__ tenemos acceso al nombre de un
# un módulo. Python utiliza este atributo cuando se ejecuta
# un programa para conocer si el módulo es ejecutado de forma
# independiente (en ese caso __name__ = '__main__') o es
# importado:
"""if __name__ == '__main__':
    main()"""
    
    
# OBTENER INFORMACION DE UNA VENTANA

""" class Aplicacion():
    
    def __init__(self):
        
        # En el ejemplo se utiliza el prefijo 'self' para
        # declarar algunas variables asociadas al objeto
        # ('mi_app') de la clase 'Aplicacion'. Su uso es
        # imprescindible para que se pueda acceder a sus
        # valores desde otros métodos:
        self.raiz = Tk()
        self.raiz.geometry('300x200')
        
        # Impide que los bordes puedan desplazarse para
        # ampliar o reducir el tamaño de la ventana 'self.raiz':
        self.raiz.resizable(width=True,height=True)
        self.raiz.title('Ver informacion')
        
        # Define el widget Text 'self.tinfo ' en el que se
        # pueden introducir varias líneas de texto:
        self.tinfo = Text(self.raiz, width=40, height=10)
        
        # Sitúa la caja de texto 'self.tinfo' en la parte
        # superior de la ventana 'self.raiz':
        self.tinfo.pack(side=TOP)
        
        # Define el widget Button 'self.binfo' que llamará
        # al metodo 'self.verinfo' cuando sea presionado
        self.binfo = ttk.Button(self.raiz, text='Info', command=self.verinfo)
        
        # Coloca el botón 'self.binfo' debajo y a la izquierda
        # del widget anterior
        self.binfo.pack(side=LEFT)
        
        # Define el botón 'self.bsalir'. En este caso
        # cuando sea presionado, el método destruirá o
        # terminará la aplicación-ventana 'self.raíz' con
        # 'self.raiz.destroy'
        self.bsalir = ttk.Button(self.raiz, text='Salir', command=self.raiz.destroy)
         
        # Coloca el botón 'self.bsalir' a la derecha del
        # objeto anterior.
        self.bsalir.pack(side=RIGHT)
        
        # El foco de la aplicación se sitúa en el botón
        # 'self.binfo' resaltando su borde. Si se presiona
        # la barra espaciadora el botón que tiene el foco
        # será pulsado. El foco puede cambiar de un widget
        # a otro con la tecla tabulador [tab]
        self.binfo.focus_set()
        self.raiz.mainloop()
        
    def verinfo(self):
        
        # Borra el contenido que tenga en un momento dado
        # la caja de texto
        self.tinfo.delete('1.0', END)
        
        # Obtiene información de la ventana 'self.raiz':
        info1 = self.raiz.winfo_class()
        info2 = self.raiz.winfo_geometry()
        info3 = str(self.raiz.winfo_width())
        info4 = str(self.raiz.winfo_height())
        info5 = str(self.raiz.winfo_rootx())
        info6 = str(self.raiz.winfo_rooty())
        info7 = str(self.raiz.winfo_id())
        info8 = self.raiz.winfo_name()
        info9 = self.raiz.winfo_manager()
        
        # Construye una cadena de texto con toda la
        # información obtenida:
        texto_info = 'Clase de "raiz": ' + info1 + '\n'
        texto_info += "Resolución y posición: " + info2 + "\n"
        texto_info += "Anchura ventana: " + info3 + "\n"
        texto_info += "Altura ventana: " + info4 + "\n"
        texto_info += "Pos. Ventana X: " + info5 + "\n"
        texto_info += "Pos. Ventana Y: " + info6 + "\n"
        texto_info += "Id. de 'raiz': " + info7 + "\n"
        texto_info += "Nombre objeto: " + info8 + "\n"
        texto_info += "Gestor ventanas: " + info9 + "\n"
        
        # Insertar la informacion de la cahja de texto:
        self.tinfo.insert("1.0", texto_info)
        
        
def main():
    mi_app = Aplicacion()
    return 0

if __name__ == '__main__':
    main() """
    
    
    
# GESTOR DE GEOMETRIA PACK

class Aplicacion():
    def __init__(self):
        
        self.raiz = Tk()
        self.raiz.title("Acceso")
        
        # Cambia el formato de la fuente actual a negrita para
        # resaltar las dos etiquetas que acompañan a las cajas
        # de entrada. (Para este cambio se ha importado el
        # módulo 'font' al comienzo del programa):
        fuente = font.Font(weight='bold')
        
        # Define las etiquetas que acompañan a las cajas de
        # entrada y asigna el formato de fuente anterior:
        self.etiqueta1 = ttk.Label(self.raiz, text="Usuario:", font=fuente)
        self.etiqueta2 = ttk.Label(self.raiz, text="Contraseña:", font=fuente)
        
        # Declara dos variables de tipo cadena para contener
        # el usuario y la contraseña:
        
        self.usuario = StringVar()
        self.clave = StringVar()
        
        # Realiza una lectura del nombre de usuario que
        # inició sesión en el sistema y lo asigna a la
        # variable 'self.usuario' (Para capturar esta
        # información se ha importando el módulo getpass
        # al comienzo del programa):
        self.usuario.set(getpass.getuser())
        
        # Define dos cajas de entrada que aceptarán cadenas
        # de una longitud máxima de 30 caracteres.
        # A la primera de ellas 'self.ctext1' que contendrá
        # el nombre del usuario, se le asigna la variable
        # 'self.usuario' a la opción 'textvariable'. Cualquier
        # valor que tome la variable durante la ejecución del
        # programa quedará reflejada en la caja de entrada.
        # En la segunda caja de entrada, la de la contraseña,
        # se hace lo mismo. Además, se establece la opción
        # 'show' con un "*" (asterisco) para ocultar la
        # escritura de las contraseñas:
        self.ctext1 = ttk.Entry(self.raiz, textvariable=self.usuario, width=30)
        self.ctext2 = ttk.Entry(self.raiz, textvariable=self.clave, width=30, show='*')
        self.separ1 = ttk.Separator(self.raiz, orient=HORIZONTAL)
        
        # Se definen dos botones con dos métodos: El botón
        # 'Aceptar' llamará al método 'self.aceptar' cuando
        # sea presionado para validar la contraseña; y el botón
        # 'Cancelar' finalizará la aplicación si se llega a
        # presionar:
        self.boton1 = ttk.Button(self.raiz, text='Aceptar', command=self.aceptar)
        self.boton2 = ttk.Button(self.raiz, text='Cancelar', command=quit)
        
        
        # Se definen las posiciones de los widgets dentro de
        # la ventana. Todos los controles se van colocando
        # hacia el lado de arriba, excepto, los dos últimos,
        # los botones, que se situarán debajo del último 'TOP':
        # el primer botón hacia el lado de la izquierda y el
        # segundo a su derecha.
        # Los valores posibles para la opción 'side' son:
        # TOP (arriba), BOTTOM (abajo), LEFT (izquierda)
        # y RIGHT (derecha). Si se omite, el valor será TOP
        # La opción 'fill' se utiliza para indicar al gestor
        # cómo expandir/reducir el widget si la ventana cambia
        # de tamaño. Tiene tres posibles valores: BOTH
        # (Horizontal y Verticalmente), X (Horizontalmente) e
        # Y (Verticalmente). Funcionará si el valor de la opción
        # 'expand' es True.
        # Por último, las opciones 'padx' y 'pady' se utilizan
        # para añadir espacio extra externo horizontal y/o
        # vertical a los widgets para separarlos entre sí y de
        # los bordes de la ventana. Hay otras equivalentes que
        # añaden espacio extra interno: 'ipàdx' y 'ipady':
        self.etiqueta1.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
        self.ctext1.pack(side=TOP, fill=X, expand=True, padx=5, pady=5)
        
        self.etiqueta2.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
        self.ctext2.pack(side=TOP, fill=X, expand=True, padx=5, pady=5)
        
        self.separ1.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
        
        self.boton1.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)
        self.boton2.pack(side=RIGHT, fill=BOTH, expand=True, padx=5, pady=5)
        
        # Cuando se inicia el programa se asigna el foco
        # a la caja de entrada de la contraseña para que se
        # pueda empezar a escribir directamente:
        self.ctext2.focus_set()
        
        self.raiz.mainloop()
        
    # El método 'aceptar' se emplea para validar la
    # contraseña introducida. Será llamado cuando se
    # presione el botón 'Aceptar'. Si la contraseña
    # coincide con la cadena 'tkinter' se imprimirá
    # el mensaje 'Acceso permitido' y los valores
    # aceptados. En caso contrario, se mostrará el
    # mensaje 'Acceso denegado' y el foco volverá al
    # mismo lugar.
    def aceptar(self):
        if self.clave.get() == 'tkinter':
            print("Acceso permitido")
            print("Usuario: ", self.ctext1.get())
            print("Contraseña: ", self.ctext2.get())
        else:
            print("Acceso denegado")
            
            # Se inicializa la variable 'self.clave' para
            # que el widget 'self.ctext2' quede limpio.
            # Por último, se vuelve a asignar el foco
            # a este widget para poder escribir una nueva
            # contraseña.
            self.clave.set("")
            self.ctext2.focus_set()
            
def main():
    mi_app = Aplicacion()
    return 0

if __name__ == '__main__':
    main()
        
