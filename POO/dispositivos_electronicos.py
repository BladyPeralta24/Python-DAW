class DispositivoElectronico():
    
    def __init__(self, nombre, marca, precio):
        
        self.nombre = nombre
        self.marca = marca
        self.__precio = precio
        
    @property
    def precio(self):
        return self.__precio
    
    @precio.setter
    def precio(self, nuevo_valor):
        if isinstance(nuevo_valor, float):
            self.__precio = nuevo_valor
        else:
            raise ValueError("ExcepcionPrecioControlada") 
        
    def __str__(self):
        return f'Nombre: {self.nombre}\nMarca: {self.marca}\nPrecio: {self.precio}€'
    
class Telefonica():
    
    operadoras = {
    'OR' : "Orange",
    'MS' : "MoviStar",
    'VF' : "Vodafone",
    'MM' : "Más Movil"
    }
    
class Telefono(DispositivoElectronico):
    
    prefijo = ["6","7","8","9"]

    def __init__(self):
        
        self.__numero = ""
        self.__companhia = ""
        
    @property
    def numero(self):
        return self.__numero
    
    @numero.setter
    def numero(self, nuevo_valor):
        if nuevo_valor[0] in Telefono.prefijo and len(nuevo_valor) == 9 and nuevo_valor.isnumeric():
            self.__numero = nuevo_valor
        else:
            raise Exception("ExcepcionNumeroControlada")
            
    
    @property
    def companhia(self):
        return self.__companhia
    
    @companhia.setter
    def companhia(self, nuevo_valor):
        if nuevo_valor.upper() in Telefonica.operadoras.keys():
            self.__companhia = nuevo_valor
        else:
            raise Exception("ExcepcionCompanhiaControlada")
            
    def __str__(self):
        return f'{super().__str__()}\nNúmero: {self.__numero}\nCompañia: {self.__companhia}'
    
    
    
class Portatil(DispositivoElectronico):
    
    resoluciones = ["HD", "4K", "8K"]
    
    def __init__(self, nombre, marca, precio, resolucion, tamanho):
        super().__init__(nombre, marca, precio)
        
        self.__resolucion = resolucion
        self.__tamanho = tamanho
        
    @property
    def resolucion(self):
        return self.__resolucion
    
    @resolucion.setter
    def resolucion(self, nuevo_valor):
        if nuevo_valor.upper() in Portatil.resoluciones:
            self.__resolucion = nuevo_valor
        else:
            raise Exception ("ExcepcionResolucionControlada")
            
            
    @property
    def tamanho(self):
        return self.__tamanho
    
    @tamanho.setter
    def tamanho(self, nuevo_valor):
        if isinstance(nuevo_valor, int):
            self.__tamanho = nuevo_valor
        else:
            raise Exception("ExcepcionTamanoControlada")
            
    def __str__(self):
        return f'{super().__str__()}\nResolucion: {self.__resolucion}\nTamaño: {self.__tamanho}'
   
    

 
 
 
 
portatil = Portatil('Ordenador','HP',55.4, '4k', 22)

try:
    portatil.precio = 'hola'
except Exception as error:
    if error.args[0] == 'precio':
        print('ExcepcionPrecioControlada')
        


	
telefono = Telefono()
try:
    telefono.companhia = 'hola'
except Exception as error:
    if error.args[0] == 'companhia':
        print('ExcepcionCompaniaControlada')