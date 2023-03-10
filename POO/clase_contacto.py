from clase_persona import Persona

class Contacto(Persona):
    
    def __init__(self, nombre, primer_apellido, segundo_apellido, edad, nif, direccion, telefono_fijo, telefono_movil, email):
        super().__init__(nombre, primer_apellido, segundo_apellido, edad, nif)
        
        self.direccion = direccion
        self.telefono_fijo = telefono_fijo
        self.telefono_movil = telefono_movil
        self.email = email
        
            
            
    def __str__(self):
        return f': ( Nombre: {self.nombre}, Primer Apellido: {self.primer_apellido}, Segundo apellido: {self.segundo_apellido}, Edad: {self.edad}, NIF: {self.nif}, Direccion: {self.direccion}, Telefono fijo: {self.telefono_fijo}, Telefono movil: {self.telefono_movil}, Email: {self.email} )\n'

