from tkinter import *
from tkinter import  ttk

"""class Calculadora():
    
    def __init__(self, ventana):
        
        #Inicializar la ventana con un titulo:
        self.ventana = ventana
        self.ventana.title('Calculadora')
        self.ventana.resizable(0,0)
        self.ventana.configure(bg="light blue")
        
        #Agregar una caja de texto para que sea la pantalla de la calculadora
        self.pantalla=Text(ventana, state='disabled', width=40,height=3, background='white', fg='black', font=("Helvetica", 15))
        
        #Situar la pantalla en la ventana
        # la parte del grid falta por implementar y cambiarla por el metodo pack al igual que los otros botones
        self.pantalla.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        
        #Inicializar la operacion mostrada en pantalla como String vacio
        self.operacion=""
        
        #Crear los botones de la calculadora
        boton1=self.crearBoton(7)
        boton2=self.crearBoton(8)
        boton3=self.crearBoton(9)
        boton4=self.crearBoton("Borrar", escribir=False)
        
        boton5=self.crearBoton(4)
        boton6=self.crearBoton(5)
        boton7=self.crearBoton(6)
        boton8=self.crearBoton("/")
        
        boton9=self.crearBoton(1)
        boton10=self.crearBoton(2)
        boton11=self.crearBoton(3)
        boton12=self.crearBoton("*")
        
        boton13=self.crearBoton(".")
        boton14=self.crearBoton("0")
        boton15=self.crearBoton("+")
        boton16=self.crearBoton("-")
        
        boton17=self.crearBoton("=", escribir=False, ancho=20, alto=2)
        
        #Situar los botones con el gestor grid
        botones = [boton1 ,boton2, boton3, boton4, boton5, boton6, boton7, boton8, boton9, boton10, boton11, boton12, boton13, boton14, boton15, boton16, boton17]
        contador = 0
        for fila in range(1,5):
            for columna in range(4):
                botones[contador].grid(row=fila, column=columna)
                contador += 1
            
        #Colocar el ultimo boton al final
        botones[16].grid(row=5, column=0, columnspan=4)
        
        return
        
    
    #Crear un boton mostrando el valor pasado por parámetro
    def crearBoton(self, valor, escribir=True, ancho=9, alto=1):
        return Button(self.ventana, text=valor, width=ancho, height=alto, font=("Helvetica", 15), command=lambda: self.click(valor, escribir))
    
    #Controlar el evento disparado al hacer click en un boton
    def click(self, texto, escribir):
        # Si el parametro escribir es True, entonces el parametro texto debe mostrarse en pantalla, de lo contrario no lo hará
        if not escribir:
            # Calcular si hay una operacion a ser evaluado y si el usuario presiona "="
            if texto=="=" and self.operacion!="":
                resultado = str(eval(self.operacion))
                self.operacion = ""
                self.limpiarPantalla()
                self.mostrarEnPantalla(resultado)
                
            # Si se presiona el boton de borrar, limpiar la pantalla
            elif texto=="Borrar":
                self.operacion=""
                self.limpiarPantalla()
        #Mostrar texto
        else:
            self.operacion += str(texto)
            self.mostrarEnPantalla(texto)
            
        return
            
            
    
    # Borrar el contenido de la pantalla de la calculadora
    def limpiarPantalla(self):
        self.pantalla.configure(state="normal")
        self.pantalla.delete("1.0", END)
        self.pantalla.configure(state="disabled")
        return
        
    # Mostrar en la pantalla de la calculadora el contenido de las operaciones y los resultados
    def mostrarEnPantalla(self, valor):
        self.pantalla.configure(state="normal")
        self.pantalla.insert(END, valor)
        self.pantalla.configure(state="disabled")
    
        
        


root = Tk()
calculadora = Calculadora(root)
root.mainloop() """

class Calculadora():
    
    def __init__(self):
        
        self.raiz = Tk()
        self.raiz.title("Calculadora")
        #self.raiz.resizable(0,0)
        
        
        frame_pantalla= Frame(self.raiz)
        frame_pantalla.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
        
        frame_fila789= Frame(self.raiz)
        frame_fila789.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
        
        frame_fila456 = Frame(self.raiz)
        frame_fila456.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
        
        frame_fila123 = Frame(self.raiz)
        frame_fila123.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
        
        frame_fila0 = Frame(self.raiz)
        frame_fila0.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
        
        self.pantalla = ttk.Entry(frame_pantalla, width=62, justify= RIGHT, style="")
        
        self.boton1             = ttk.Button(frame_fila123, text="1", command= lambda : self.escribir_numero(1))
        self.boton2             = ttk.Button(frame_fila123, text="2", command= lambda : self.escribir_numero(2))
        self.boton3             = ttk.Button(frame_fila123, text="3", command= lambda : self.escribir_numero(3))
        self.boton_multiplicar  = ttk.Button(frame_fila123, text="x", command= lambda : self.escribir_operacion('*'))
        
        self.boton4             = ttk.Button(frame_fila456, text="4", command= lambda : self.escribir_numero(4))
        self.boton5             = ttk.Button(frame_fila456, text="5", command= lambda : self.escribir_numero(5))
        self.boton6             = ttk.Button(frame_fila456, text="6", command= lambda : self.escribir_numero(6))
        self.boton_restar       = ttk.Button(frame_fila456, text="-", command= lambda : self.escribir_operacion('-'))
        
        self.boton7             = ttk.Button(frame_fila789, text="7", command= lambda : self.escribir_numero(7))
        self.boton8             = ttk.Button(frame_fila789, text="8", command= lambda : self.escribir_numero(8))
        self.boton9             = ttk.Button(frame_fila789, text="9", command= lambda : self.escribir_numero(9))
        self.boton_sumar        = ttk.Button(frame_fila789, text="+", command= lambda : self.escribir_operacion('+'))
        
        self.boton0             = ttk.Button(frame_fila0, text="0", width=30, command= lambda : self.escribir_numero(0))
        self.boton_dividir      = ttk.Button(frame_fila0, text="/", command= lambda : self.escribir_operacion('/'))
        self.boton_borrar       = ttk.Button(frame_fila0, text="DEL", command= 'self.borrar', style='borrar.TButton')
        self.boton_igual        = ttk.Button(frame_fila0, text='=', width=20, command= lambda : self.resultado())
        
        
        self.pantalla.pack(side=LEFT, fill=BOTH, expand=True, padx=5)
        
        self.boton7.pack(side=LEFT, fill=BOTH, expand=True, padx=5)
        self.boton8.pack(side=LEFT, fill=BOTH, expand=True, padx=5)
        self.boton9.pack(side=LEFT, fill=BOTH, expand=True, padx=5)
        self.boton_sumar.pack(side=LEFT, fill=BOTH, expand=True, padx=5)
        
        self.boton4.pack(side=LEFT, fill=BOTH, expand=True, padx=5)
        self.boton5.pack(side=LEFT, fill=BOTH, expand=True, padx=5)
        self.boton6.pack(side=LEFT, fill=BOTH, expand=True, padx=5)
        self.boton_restar.pack(side=LEFT, fill=BOTH, expand=True, padx=5)
        
        self.boton1.pack(side=LEFT, fill=BOTH, expand=True, padx=5)
        self.boton2.pack(side=LEFT, fill=BOTH, expand=True, padx=5)
        self.boton3.pack(side=LEFT, fill=BOTH, expand=True, padx=5)
        self.boton_multiplicar.pack(side=LEFT, fill=BOTH, expand=True, padx=5)
        
        self.boton_borrar.pack(side=LEFT, fill=BOTH, expand=True, padx=5)
        self.boton0.pack(side=LEFT, fill=BOTH, expand=True, padx=5)
        self.boton_dividir.pack(side=LEFT, fill=BOTH, expand=True, padx=5)
        self.boton_igual.pack(side=LEFT, fill=BOTH, expand=True, padx=5)
        
        
        # self.pantalla.focus_set()
        
        
        self.raiz.mainloop()
        
        self.operacion = ''
        self.operando1 = 0
        self.operando2 = 0
        
    # Indicar para saber por cual posicion se esta escribiendo
    i = 0
    
    # tomar una captura del indice, despues de escribir la operacion
    # para asignar al operando2 el valor desde este indice hasta el final
    j = 0
    
    def escribir_numero(self, numero):
        if self.pantalla.get() == "ERROR":
            self.pantalla.delete(0, END)
            self.pantalla.insert(0, 'ERROR')
            Calculadora.i = 0
        else:
            self.pantalla.insert(Calculadora.i, numero)
            Calculadora.i += 1
            
    
    def escribir_operacion(self, operacion):
        self.operando1 = float(self.pantalla.get())
        self.pantalla.insert(Calculadora.i, operacion)
        self.operacion = operacion
        Calculadora.j = Calculadora.i + 1
        Calculadora.i += 1
        
    def deshacer(self):
        if self.pantalla.get() == 'ERROR':
            self.borrar()
        else:
            self.pantalla.delete(Calculadora.i - 1, END)
            Calculadora.i -= 1
            
    def borrar(self):
        self.pantalla.delete(0, END)
        Calculadora.i = 0
        
    def resultado(self):
        
        contenido = self.pantalla.get()
        
        self.operando2 = float(contenido[Calculadora.j:])

        if self.operacion == '+':
            resultado = self.operando1 + self.operando2
        
        elif self.operacion == '-':
            resultado = self.operando1 - self.operando2
            
        elif self.operacion == '*':
            resultado = self.operando1 * self.operando2
            
        elif self.operacion == '/':
            resultado = self.operando1 / self.operando2
            
        else:
            self.pantalla.delete(0, END)
            self.pantalla.insert(0, 'ERROR')
            Calculadora.i = 0
            
        self.borrar()
        self.pantalla.insert(0, resultado)
        Calculadora.i = len(str(resultado))


def main():
    mi_calculadora = Calculadora()
    return 0

if __name__ == '__main__':
    main()



