"""
CLASE FORO

Crea una clase que tenga una variable estática con el contenido del foro. 
Luego crea una clase Forero que tenga los métodos:

insertar(mensaje): Inserta un mensaje en un foro, especificando previamente el nombre/nick de la persona que ha escrito y el ID del mensaje.
borrar(id): Borra un mensaje del foro relacionado con el id pasado como parámetro. Sólo puede borrar mensajes creados por el usuario.
editar(id): Edita el mensaje con el id en cuestión.

""" 


class Foro():
    
    CONTENIDO_FORO = []
    

class Forero(Foro):
    
    def __init__(self, id_usuario, nick, id_mensaje):
        super().__init__()

        self.id_usuario     = id_usuario
        self.nick           = nick
        self.id_mensaje     = id_mensaje
        
        
    """ Inserta un mensaje en un foro, especificando previamente el nombre/nick de la persona que ha escrito y el ID del mensaje """
    def insertar(self, mensaje):
        if self.id_usuario != '' and self.id_mensaje != '':
            return Foro.CONTENIDO_FORO.append({'Nick': self.nick, 'ID': self.id_usuario, 'Mensaje': mensaje})
        else:
            return 'El usuario no existe. No puedes insertar mensajes.'
    
    
    """ Borra un mensaje del foro relacionado con el id pasado como parámetro. Sólo puede borrar mensajes creados por el usuario """
    def borrar(self, id_insertado):
        for mensaje in Foro.CONTENIDO_FORO:
            if mensaje[id_insertado] == self.id_usuario:
                Foro.CONTENIDO_FORO.remove(mensaje)
            else:
                return ('No se ha encontrado el mensaje con el id especificado')
    
    
    """ Edita el mensaje con el id en cuestión """
    def editar(self, id_insertado, nuevo_mensaje):
        for mensaje in Foro.CONTENIDO_FORO:
            if mensaje['ID'] == self.id_usuario:
                mensaje['mensaje'] = nuevo_mensaje
            else:
                return 'No se ha encontrado el mensaje con el id especificado'
            
            
    
blady = Forero(1, 'Blady', 1)
lucas = Forero(2, 'Lucas', 2)
maria = Forero('' , 'Maria', '')

blady.insertar('Este es mi primer mensaje')

lucas.insertar('Lucas ha conseguido insertar un mensaje')
lucas.editar(2, 'Lucas ha conseguido modificar el mensaje')
#lucas.borrar(2)

maria.insertar('maria ha iniciado sesion')

for mensaje in Foro.CONTENIDO_FORO:
    print (mensaje)