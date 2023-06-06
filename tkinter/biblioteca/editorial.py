# seleccionar la editorial de una lista de editoriales cargadas en la clase
# Editorial

class Editorial():
    
    listado = ['Editorial 1', 'Editorial 2', 'Editorial 3', 'Editorial 4']
    
    def __init__(self, editorial):
        
        self.ditorial = editorial
        
    
    @property
    def editorial(self):
        return self.__editorial
    
    @editorial.setter
    def editorial(self, nuevo_valor):
        if nuevo_valor in Editorial.listado:
            self.__editorial = nuevo_valor
        else:
            raise Exception('cod_editorial', 'La editorial no se encuentra en nuestro listado')
        
        