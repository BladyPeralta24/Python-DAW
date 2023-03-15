""" 
Por último, realizar una clase Agenda la cuál deberá mostrar un menú con las siguientes opciones.
Añadir contacto: Te solicita todos los datos del contacto y lo añade a tu gestión.
Lista de contactos: Contactos ordenados por su nombre alfabéticamente.
Buscar contacto:  Busca contactos por cualquiera de sus parámetros.
Editar contacto: Tendrás que gestionar un menú para editar los parámetros de tu contacto, cualquiera de ellos. 
"""

from contacto import Contacto

class Agenda():
    
    def __init__(self):
        self.lista_contactos = {}
        
        
    def anhadir_contacto(self, contacto : Contacto):
        self.lista_contactos[contacto.nif] = contacto
        
    def listado_contactos(self):
        
        lista_contactos = []
        
        
        for nif, contacto in self.lista_contactos.items():
            lista_contactos.append(contacto)
            
        
        return sorted(lista_contactos)
            
            
    def buscar_contacto(self, parametro):
        
        encontrados = []
        for nif, contacto in self.lista_contactos.items():
            
            if parametro in contacto.datos():
                encontrados.append(contacto)
                
        return encontrados
            
            
    def editar_contacto(self, nif, contacto_editado):
        self.lista_contactos[nif] = contacto_editado
        
            
        
agenda = Agenda()

#print(agenda.listado_contactos())