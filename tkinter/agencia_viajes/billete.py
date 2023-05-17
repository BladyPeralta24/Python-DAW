from aeropuerto import Aeropuerto

class Billete:

    def __init__(self):
        self.__viaje: str #origen-destino
        self.__nombre: str
        self.__apellido1: str
        self.__apellido2: str

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
    def apellido1(self):
        return self.__apellido1

    @apellido1.setter
    def apellido1(self,nuevos_apellido):
        if not nuevos_apellido:
            raise Exception("apellido1", "No se han insertado el primer apellido")
        else:
            self.__apellido1 = nuevos_apellido
            

    @property
    def apellido2(self):
        return self.__apellido2

    @apellido2.setter
    def apellido2(self,nuevos_apellido):
        self.__apellido2 = nuevos_apellido

    def diccionario(self):
        return {
            "viaje"     : self.__viaje
           ,"nombre"    : self.__nombre
           ,"apellido1" : self.__apellido1
           ,"apellido2" : self.__apellido2
        }
        
    def __str__(self):
        return f"Viaje: {self.__viaje} Nombre: {self.__nombre} apellido1: {self.__apellido1} apellido2: {self.__apellido2}\n"



#billete = Billete()
#
#billete.viaje = 'Madrid-Barcelona'
#billete.nombre = 'Andrés'
#billete.apellido1 = 'Calamaro'
#billete.apellido2 = 'Niidea'
#
#
#billete.guardar()