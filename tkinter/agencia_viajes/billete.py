

class Billete:

    def __init__(self):
        self.__viaje = ''
        self.__nombre = ''
        self.__apellidos = ''

    @property
    def viaje(self):
        return self.__viaje

    @viaje.setter
    def viaje(self,nuevo_viaje):
        if not nuevo_viaje:
            raise Exception("viaje", "No se han insertado viajes")
        else:
            self.__viaje = nuevo_viaje


    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,nuevo_nombre):
        if not nuevo_nombre:
            raise Exception("nombre", "No se ha insertado ningún nombre")
        else:
            self.__nombre = nuevo_nombre
        
    @property
    def apellidos(self):
        return self.__apellidos

    @apellidos.setter
    def apellidos(self,nuevos_apellidos):
        if not nuevos_apellidos:
            raise Exception("apellido1", "No se han insertado el primer apellido")
        else:
            self.__apellidos = nuevos_apellidos
            

    def diccionario(self):
        
        return {
            "viaje"     : self.__viaje
           ,"nombre"    : self.__nombre
           ,"apellidos" : self.__apellidos
        }
        
    def __str__(self):
        return f"Viaje: {self.__viaje} Nombre: {self.__nombre} apellidos: {self.__apellidos}\n"
