from tkinter import *
from tkinter import  ttk

class Calculadora():
    
    def __init__(self, ventana):
        
        #Inicializar la ventana con un titulo:
        self.ventana = ventana
        self.ventana.title('Calculadora')
        self.ventana.resizable(0,0)
        
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
root.mainloop()