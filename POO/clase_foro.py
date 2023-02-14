"""
CLASE FORO

Crea una clase que tenga una variable estática con el contenido del foro. 
Luego crea una clase Forero que tenga los métodos:

insertar(mensaje): Inserta un mensaje en un foro, especificando previamente el nombre/nick de la persona que ha escrito y el ID del mensaje.
borrar(id): Borra un mensaje del foro relacionado con el id pasado como parámetro. Sólo puede borrar mensajes creados por el usuario.
editar(id): Edita el mensaje con el id en cuestión.

""" 


class Foro():
    
    CONTENIDO_FORO = {}
    
    id_mensaje = 0
    
    def __init__(self) -> None:
        pass
    
    """ Inserta un mensaje en un foro, especificando previamente el nombre/nick de la persona que ha escrito y el ID del mensaje """
    @staticmethod
    def insertar(mensaje : dict):
        
        Foro.id_mensaje += 1
        Foro.CONTENIDO_FORO[Foro.id_mensaje] = mensaje
        return Foro.id_mensaje
    
    
    """ Borra un mensaje del foro relacionado con el id pasado como parámetro. Sólo puede borrar mensajes creados por el usuario """
    @staticmethod
    def borrar(id_mensaje, id_forero):
        
        if Foro.CONTENIDO_FORO[id_mensaje]['id_forero'] == id_forero:
            del Foro.CONTENIDO_FORO[id_mensaje]
            return f'Se ha eliminado el mensaje con id:{id_mensaje} con éxito\n'
        else:
            return 'No se ha podido eliminar el mensaje\n'
    
    
    """ Edita el mensaje con el id en cuestión """  
    @staticmethod
    def editar(id_mensaje, id_forero, nuevo_mensaje: str):
        
        if Foro.CONTENIDO_FORO[id_mensaje]['id_forero'] == id_forero:
            Foro.CONTENIDO_FORO[id_mensaje]['mensaje'] = nuevo_mensaje
            return f'Se ha editado el mensaje con id:{id_mensaje} con éxito'
        else:
            return 'No ha sido posible editar el mensaje'
        
    @staticmethod
    def mostrar():
        salida = ""
        for id_mensaje, mensaje in Foro.CONTENIDO_FORO.items():
            salida += f"""
                {id_mensaje:>4d} + Usuario: {mensaje['Nick']}[{mensaje['id_forero']}] 
                     + Mensaje: {mensaje['mensaje']}
                +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"""
            
        return salida
    
    
    
class Forero(Foro):
    
    id_forero_ultimo = 0
    
    def __init__(self, nick):
        super().__init__()
        
        self.nick           = nick
        self.id_forero = Forero.id_forero_ultimo
        Forero.id_forero_ultimo += 1
        
        
    def insertar(self, mensaje):
        
        dic_mensaje = {}
        dic_mensaje['id_forero'] = self.id_forero
        dic_mensaje['Nick'] = self.nick
        dic_mensaje['mensaje'] = mensaje
        
        Foro.insertar(dic_mensaje)
    
    
    def borrar(self, id_mensaje):
        
        return Foro.borrar(id_mensaje, self.id_forero)
    
    
    
    def editar(self, id_mensaje, nuevo_mensaje):
        
        return Foro.editar(id_mensaje, self.id_forero, nuevo_mensaje)
            
            
    
blady = Forero('Blady')
lucas = Forero('Lucas')
maria = Forero('Maria')

blady.insertar('Blady ha iniciado sesion en el Foro')
#lucas.insertar('Lucas ha iniciado sesion en el Foro')
#maria.insertar('maria ha iniciado sesion en el Foro')
print(Foro.CONTENIDO_FORO)
print(Foro.mostrar())

    
    
    






# Ejercicio hecho por el profesor


# class Foro():
    
#     contenido = {}
    
#     id_mensaje = 0
        
#     def __init__(self) -> None:
#         pass
    
#     @staticmethod
#     def insertar(mensaje : dict):
        
#         Foro.id_mensaje += 1
        
#         Foro.contenido[Foro.id_mensaje] = mensaje
        
#         return Foro.id_mensaje
        
    
#     @staticmethod
#     def borrar(id_mensaje, id_forero):
        
#         if Foro.contenido[id_mensaje]['id_forero'] == id_forero:
#             del Foro.contenido[id_mensaje]
#             return f"Se ha eliminado el mensaje con id:{id_mensaje} con éxito"
#         else:
#             return "No ha sido posible eliminar el mensaje"
        
 
#     @staticmethod
#     def editar(id_mensaje, mensaje : str, id_forero):
#         if Foro.contenido[id_mensaje]['id_forero'] == id_forero:
#             Foro.contenido[id_mensaje]['mensaje'] = mensaje
#             return f"Se ha editado el mensaje con id:{id_mensaje} con éxito"
#         else:
#             return "No ha sido posible editar el mensaje"

#        @staticmethod
#    def mostrar():
#        salida = ""
#        for id_mensaje,mensaje in Foro.contenido.items():
#            salida += f"""
#                {id_mensaje:>4d} + Usuario: {mensaje['nick']}[{mensaje['id_forero']}] 
#                     + Mensaje: {mensaje['mensaje']}
#                +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"""
#            
#        return salida



# from foro import Foro

# class Forero():
    
#     id_forero_ultimo = 0
    
#     def __init__(self,nick):
#         self.nick = nick
        
#         self.id_forero = Forero.id_forero_ultimo
        
#         Forero.id_forero_ultimo += 1
        
        
#     def insertar(self, mensaje):
        
#         dic_mensaje = {}
#         dic_mensaje['id_forero'] = self.id_forero
#         dic_mensaje['nick'] = self.nick
#         dic_mensaje['mensaje'] = mensaje
        
        
#         Foro.insertar(dic_mensaje)
        
#     def borrar(self, id_mensaje):
#         return Foro.borrar(id_mensaje, self.id_forero)
    
    
#     def editar(self, id_mensaje, mensaje):
        
#         return Foro.editar(id_mensaje, mensaje, self.id_forero)
        
        
        
# andres = Forero("Andrés")
# jaime  = Forero("Jaime")

# andres.insertar("Hola, soy nuevo en el foro")
# andres.insertar("Soy natural de Órzola")
# andres.insertar("Me gusta el Ajedrez")
# jaime.insertar("Hola Andrés, bienvenido al Foro")

# print(jaime.borrar(1))
# print(jaime.borrar(2))


# print(Foro.contenido)

# print("\n\n")


# andres.editar(1,"Hola, soy Andrés y soy nuevo en el Foro")

# print(Foro.contenido)