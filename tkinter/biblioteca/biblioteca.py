

from editorial import Editorial

class Biblioteca():
    
    listado_anho = ["2021", "2020", "2019", "2018", "2017", "2016"]
    
    def __init__(self, libro = '', autor = '', editorial: Editorial = '', anho = ''):
        
        self.__libro = libro
        self.__autor = autor
        self.__editorial = editorial
        self.__anho  = anho
        
    @property
    def libro(self):
        return self.__libro
    
    @libro.setter
    def libro(self, nuevo_libro):
        if not nuevo_libro:
            raise Exception('libro', 'No se ha insertado un libro')
        else:
            self.__libro = nuevo_libro
            
    
    @property
    def autor(self):
        return self.__autor
    
    @autor.setter
    def autor(self, nuevo_autor):
        if not nuevo_autor:
            raise Exception('autor', 'No se ha insertado un autor')
        else:
            self.__autor = nuevo_autor
            
            
    @property
    def editorial(self):
        return self.__editorial
    
    @editorial.setter
    def editorial(self, nuevo_editorial):
        if not nuevo_editorial in Editorial.listado:
            raise Exception('editorial', 'No se encuentra en el listado')
        else:
            self.__editorial = nuevo_editorial
            
    
    @property
    def anho(self):
        return self.__anho
    
    @anho.setter
    def anho(self, nuevo_anho):
        if not nuevo_anho in Biblioteca.listado_anho:
            raise Exception('anho', 'No se ha se encuentra en el listado')
        else:
            self.__anho = nuevo_anho
            
    
    def diccionario(self):
        
        diccionario = {}
        
        diccionario[Editorial.editorial] = {
            "nombre"     : self.__libro
            ,"autor"     : self.__autor
            ,"editorial" : Editorial.editorial
            ,"Año"       : self.__anho
        }
        
        return diccionario
    
    def __str__(self) -> str:
        return f"Nombre: {self.__libro} Autor: {self.__autor}, Editorial: {self.__editorial}, Año: {self.__anho}"