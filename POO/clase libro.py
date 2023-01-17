class Libro():
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        
    def mostrar_informacion(self):
        
        return 'Nombre: '+ self.titulo + '\nAutor: '+self.autor + '\nNumero de páginas: ' +str(self.paginas) + ' páginas'
        
    def abrir_libro(self):
        
        return 'El libro '+ self.titulo + ', está abierto'
        
    def cerrar_libro(self):
        
        return 'El libro '+ self.titulo + ', está cerrado'
    
    

quijote = Libro('Don quijote de la Mancha', 'Miguel de cervantes', 1345)

print(quijote.mostrar_informacion())
print(quijote.abrir_libro())
print(quijote.cerrar_libro())




# Ejercicio hecho por el profe:

# class Libro():
    
#     def __init__(self, titulo, autor, paginas):
#         self.titulo  = titulo
#         self.autor   = autor
#         self.paginas = paginas
        
#         self.__estado  = 'Cerrado'
        
#     def mostrar_informacion(self):
        
#         return f"El libro de títuo  {self.titulo} con autor {self.autor} y número de páginas {self.paginas} se encuentra {self.__estado}"
        
#     def abrir_libro(self):
        
#         print("El libro se encuentra {} y se ha abierto".format(self.__estado))
#         self.cambiar_estado()
        
#     def cerrar_libro(self):
        
#         print("El libro se encuentra {} y se ha cerrado".format(self.__estado))
#         self.cambiar_estado()
        
        
#     def cambiar_estado(self):
       
#         if self.__estado == 'Abierto':
#             self.__estado = 'Cerrado'
#         else:
#             self.__estado = 'Abierto'


# mi_libro = Libro("Las aventuras de Jaime", "Andrés", 20)


# print(mi_libro.mostrar_informacion())


# mi_libro.abrir_libro()


# print(mi_libro.mostrar_informacion())




