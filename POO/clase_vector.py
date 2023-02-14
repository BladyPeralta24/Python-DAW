


class Vector():
    
    def __init__(self, coordenada_x, coordenada_y, coordenada_z):
        
        self.coordenada_x = coordenada_x
        self.coordenada_y = coordenada_y
        self.coordenada_z = coordenada_z
        
        
    @property
    def coordenada_x(self):
        return self.__coordenada_x
    
    @coordenada_x.setter
    def coordenada_x(self, nuevo_valor):
        if isinstance(nuevo_valor, int):
            self.__coordenada_x = nuevo_valor
        else:
            print("ERROR. La variable de la coordenada x no es válda")
            exit
            
    
    @property
    def coordenada_y(self):
        return self.__coordenada_y
    
    @coordenada_y.setter
    def coordenada_y(self, nuevo_valor):
        if isinstance(nuevo_valor, int):
            self.__coordenada_y = nuevo_valor
        else:
            print("ERROR. La variable de la coordenada y no es válda")
            exit
            
            
    @property
    def coordenada_z(self):
        return self.__coordenada_z
    
    @coordenada_z.setter
    def coordenada_z(self, nuevo_valor):
        if isinstance(nuevo_valor, int):
            self.__coordenada_z = nuevo_valor
        else:
            print("ERROR. La variable de la coordenada z no es válda")
            exit
            
    
    
    
    def __mul__(self, v):
        x = self.__coordenada_y * v.__coordenada_z - self.__coordenada_z * v.__coordenada_y
        y = self.__coordenada_x * v.__coordenada_z - self.__coordenada_z * v.__coordenada_x
        z = self.__coordenada_x * v.__coordenada_y - self.__coordenada_y * v.__coordenada_x
        
        return Vector(x,y,z)
    
    def __pow__(self, v):
        # Producto Escalar: w = 5 x 6 + 4 x 7 + 3 x 8 = 30 + 28 + 24 = 82
        producto_escalar = self.__coordenada_x * v.__coordenada_x + self.__coordenada_y * v.__coordenada_y + self.__coordenada_z * v.__coordenada_z
        return producto_escalar
    
    
    def __str__(self):
        return f"({self.__coordenada_x}i, {self.__coordenada_y}j, {self.__coordenada_z}k)"
        
        
        


        
vector1 = Vector(5,4,3)
vector2 = Vector(6,7,8)

vector3 = Vector(3,1,0)
vector4 = Vector(2,1,-1)


# Imprime los valores de los vectores, Tanto el producto escalar como el producto vectorial
print(vector1 ** vector2)
print(vector3 * vector4)