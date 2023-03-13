from datetime import date

from clase_calendario import Calendario

class CalendarioLaboral(Calendario):
    
    def __init__(self, dd, mm, aaaa):
        super().__init__()
        self.dd = dd
        self.mm = mm
        self.aaaa = aaaa
        self.fecha_hoy = date.today()
    
    def set_tipo_dia(dia, tipo):
        return super().set_tipo_dia(tipo)
    
    def get_tipo_dia(dia):
        return super().get_tipo_dia()
    
    def hoy(self):
        mes = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
        dia = ['Lunes', 'Martes', 'Miercoles', 'jueves', 'viernes', 'Sábado', 'Domingo']
        mes_actual = self.fecha_hoy.month - 1
        dia_actual = date.today().weekday()
        
        return f'Hoy es {dia[dia_actual]} {self.fecha_hoy.day} de {mes[mes_actual]} de {self.fecha_hoy.year}'
    
    
        
    def dias_laborales(self): 
        pass
    
    
fecha = CalendarioLaboral(13, 5, 2004)

print(fecha.hoy())