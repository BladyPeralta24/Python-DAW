"""
Crea una clase "Estudiante" con atributos "nombre", "edad" y "calificaciones" (una lista de calificaciones) 
y métodos "agregar_calificacion", "mostrar_calificaciones" y "promedio_calificaciones". 
El método "agregar_calificacion" debe añadir una calificación a la lista de calificaciones del estudiante, 
el método "mostrar_calificaciones" debe imprimir todas las calificaciones del estudiante 
y el método "promedio_calificaciones" debe calcular y devolver
"""
class Estudiante():
    
    num_estudiantes = 0
    
    def __init__(self, nombre, edad, *argumentos_entrada):
        self.asignatura = ""
        self.lista_calificaciones = {}
        self.nombre = nombre
        self.edad = edad
        
        for nota in argumentos_entrada:
            self.agregar_calificacion(nota)
            
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo_valor):
        self.__nombre = nuevo_valor
        Estudiante.num_estudiantes += 1
            
    def agregar_calificacion(self, modulo, nota):

        self.lista_calificaciones[modulo] = nota

    def mostrar_calificacion(self):
        
        return self.lista_calificaciones


    def promedio_calificaciones(self):
        
        for modulo, calificacion in self.lista_calificaciones.items():
            
            numero_modulos += 1
            nota_total += calificacion
            
        return nota_total / numero_modulos
    
    @staticmethod
    def cantidad_companieros():
        return Estudiante.num_estudiantes
    
    
    
estudiante1 = Estudiante('Luis', 13)
estudiante2 = Estudiante('Jose', 24)
estudiante3 = Estudiante('Manu', 18)

print(Estudiante.cantidad_companieros())

# Ejercicio hecho por el profesor
"""
Clase Estudiante
Crea una clase "Estudiante" con atributos "nombre", "edad" y "calificaciones" (una lista de calificaciones) y métodos 
"agregar_calificacion", "mostrar_calificaciones" y "promedio_calificaciones". El método "agregar_calificacion" debe añadir
una calificación a la lista de calificaciones del estudiante, el método "mostrar_calificaciones" debe imprimir todas las 
calificaciones del estudiante y el método "promedio_calificaciones" debe calcular y devolver
"""


# class Estudiante():
    
#     cantidad_companheros = 0
#     def __init__(self,nombre, edad :int ):
        
#         self.nombre = nombre
#         self.edad   = edad
#         self.calificaciones = {}

#         Estudiante.cantidad_companheros += 1
        
#     def agregar_calificacion(self,modulo, nota):
#         self.calificaciones[modulo.title()] = nota
        
        
#     def mostrar_calificaciones(self):
#         return self.calificaciones
    
    
#     def promedio_calificaciones(self):
        
#         nota_total = 0
#         numero_modulos = 0
#         for modulo, calificaion in self.calificaciones.items():
#             numero_modulos += 1
#             nota_total += calificaion
            
#         return nota_total/numero_modulos

#      @staticmethod
#      def cantidad_companhero():
#          return Estudiante.cantidad_companheros
            
#       def __del__(self):
#           Estudiante.cantidad_companheros -= 1
        
        
# andres = Estudiante("Andrés", 22)

# andres.agregar_calificacion("Programación", 10)
# andres.agregar_calificacion("Entornos de desarrollo", 5)



# print(andres.mostrar_calificaciones())


# print(andres.promedio_calificaciones())

# print("La cantidad de compañeros de la cual dispongo, es: ", andres.cantidad_companhero())

# del andres

# print("La cantidad de compañeros de la cual dispongo, es: ", andres.cantidad_companhero())

