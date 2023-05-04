from tkinter import *
from tkinter import  ttk

class Calculadora():
    
    def __init__(self):
        
        self.raiz = Tk()
        self.raiz.title("Calculadora")
        self.raiz.geometry("500x250")
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
        self.boton_borrar       = ttk.Button(frame_fila0, text="DEL", command= self.borrar, style='borrar.TButton')
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



