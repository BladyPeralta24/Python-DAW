# Crea una clase llamada 'Empleado' con atributos 'nombre', 'apellido' y 'salario'. 
# Crea una clase llamada 'Gerente' que herede de la clase 'Empleado' y añade el atributo 'bono'. 
# Crea los getters y setters para todos los atributos en ambas clases y utiliza un método llamado 'aumentar_salario' 
# en la clase 'Empleado' que aumente el salario en un 10% 
# y un método llamado 'aumentar_bono' en la clase 'Gerente' que aumente el bono en un 20%

class Empleado():
    def __init__(self, nombre, apellido, salario = 0):
        self.nombre = nombre
        self.apellido = apellido
        self.salario = salario
        
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo_valor):
        if isinstance(nuevo_valor, str):
            self.__nombre = nuevo_valor
        else:
            print("ERROR. El valor del nombre no es valido")
            exit
            
    @property
    def apellido(self):
        return self.__apellido
    
    @apellido.setter
    def apellido(self, nuevo_valor):
        if isinstance(nuevo_valor, str):
            self.__apellido = nuevo_valor
        else:
            print("ERROR. El valor del apellido no es valido")
            exit
    
    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self, nuevo_valor):
        if isinstance(nuevo_valor, int):
            self.__salario = nuevo_valor
        else:
            print("ERROR. El valor del salario no es valido")
            exit
            
            
    def aumentar_salario(self, aumento = 0.1):
        aumento *= self.__salario
        self.__salario += aumento
        
    def mostrar(self):
        return f"Nombre: {self.__nombre}\nApellidos: {self.__apellido}\nSalario: {self.__salario}€"
            
            
            
class Gerente(Empleado):
    def __init__(self, nombre, apellido, salario, bono = 0):
        super().__init__(nombre, apellido, salario)
        
        self.bono = bono
        
    @property
    def bono(self):
        return self.__bono
    
    @bono.setter
    def bono(self, nuevo_valor):
        if isinstance(nuevo_valor, int):
            self.__bono = nuevo_valor
        else:
            print("ERROR. El valor del bono no es valido")
            
    def aumentar_bono(self, aumento = 0.2):
        aumento *= self.__bono
        self.__bono += aumento
        
    def mostrar(self):
        return f'{super().mostrar()}\nBono: {self.__bono}%\n'
    
    



miguel = Gerente('Miguel', 'Hernandez Ochoa', 1200, 10)

print(miguel.mostrar())
miguel.aumentar_salario()
miguel.aumentar_bono()
print(miguel.mostrar())
        
