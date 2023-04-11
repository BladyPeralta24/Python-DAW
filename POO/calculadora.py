class Calculadora():
    
    def __init__(self, numero1, numero2):
        
        self.numero1 = numero1
        self.numero2 = numero2
        
    @property
    def numero1(self):
        return self.__numero1
    
    @numero1.setter
    def numero1(self, nuevo_valor):
        if isinstance(nuevo_valor, str) and nuevo_valor.isnumeric():
            self.__numero1 = nuevo_valor
        else:
            print("AQUI DEBE IR UN RAISE. IMPLEMENTAR MAS TARDE")
            
    
    @property
    def numero2(self):
        return self.__numero2
    
    @numero2.setter
    def numero2(self, nuevo_valor):
        if isinstance(nuevo_valor, str) and nuevo_valor.isnumeric():
            self.__numero2 = nuevo_valor
        else:
            print("AQUI DEBE IR UN RAISE. IMPLEMENTAR MAS TARDE")
            
            
    @staticmethod
    def sumar(self):
        return self.__numero1 + self.__numero2
    
    @staticmethod
    def restar(self):
        return self.__numero1 - self.__numero2
    
    @staticmethod
    def multiplicar(self):
        return self.__numero1 * self.__numero2
    
    @staticmethod
    def dividir(self):
        return self.__numero1 / self.__numero2