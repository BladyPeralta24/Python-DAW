from datetime import date, timedelta, datetime

from clase_calendario import Calendario

class CalendarioLaboral(Calendario):
    
    def __init__(self):
        super().__init__()
        self.dias_no_laborales = []
        
        self.fecha_hoy = date.today()
    
    def set_tipo_dia(self, dia, tipo):
        if tipo == 'N':
            self.dias_no_laborales.append(dia)
    
    def get_tipo_dia(self, dia):
        if dia in self.dias_no_laborales:
            return 'N'
        dia_datetime = datetime(int(dia[0:4]), int(dia[5:6]), int(dia[7:8]))
    
    def hoy(self):
        mes = ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')
        dia = ['Lunes', 'Martes', 'Miercoles', 'jueves', 'viernes', 'Sábado', 'Domingo']
        mes_actual = self.fecha_hoy.month - 1
        dia_actual = date.today().weekday()
        
        return f'Hoy es {dia[dia_actual]} {self.fecha_hoy.day} de {mes[mes_actual]} de {self.fecha_hoy.year}'
    
    
        
    def dias_laborales(self): 
        pass
    
    
fecha = CalendarioLaboral(13, 5, 2004)

print(fecha.hoy())







# Programa hecho por el profe
# from calendario import Calendario

# from datetime import datetime, date, timedelta


# class CalendarioLaboral(Calendario):
    
#     cods_tipo_dia = {
#          'N' : 'No Laborable'
#         ,'L' : 'Laborable'
#     }
    
#     def __init__(self):
#         self.dias_no_laborables = []
        
        
        
#     #dia = AAAAMMDD
#     #tipo = [N]o Laborable, [L]aborable
#     def set_tipo_dia(self, dia, tipo):
#         if tipo == 'N':
#             self.dias_no_laborables.append(dia)
    
#     #dia = AAAAMMDD    
#     def get_tipo_dia(self, fecha_aaaammdd):
#         if fecha_aaaammdd in self.dias_no_laborables:
#             return 'N'
#         #                             AAAAmmdd                      aaaaMMdd            aaaammDD
#         dia_datetime = datetime(int(fecha_aaaammdd[0:4]), int(fecha_aaaammdd[4:6]), int(fecha_aaaammdd[6:8]))
       
#         if dia_datetime.weekday() in (5,6):
#             return 'N'
        
#         return 'L'
        
#     "Hoy es DD de MM de AAAA. [Laboral|No Laboral]"
#     def hoy(self):
        
#         meses = ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio','Agosto','Septiembre','Octubre', 'Noviembre', 'Diciembre')
        
        
#         tipo_dia_aaaammdd_hoy = self.get_tipo_dia(datetime.today().strftime('%Y%m%d'))
        
#         #tipo_dia = 'No Laborable' if tipo_dia_aaaammdd_hoy == 'N' else 'Laborable'
        
#         tipo_dia = CalendarioLaboral.cods_tipo_dia[tipo_dia_aaaammdd_hoy]
        
#         return "Hoy es {} de {} de {}. [{}]".format(date.today().day,meses[date.today().month - 1], date.today().year,tipo_dia)
    
    
#     def dias_laborables(self, fecha_desde = '', fecha_hasta =''):
        
#         if fecha_desde == '':
#             desde = str(date.today().year) + '0101'
        
#         if fecha_hasta == '':
#             hasta = str(date.today().year) + '1231'
            
#         dia_actual = datetime(int(desde[0:4]), int(desde[4:6]), int(desde[6:8]))
            
#         dias_laborables = []
#         while int(desde) <= int(hasta):

            
            
#             if self.get_tipo_dia(desde) == 'L':
#                 dias_laborables.append(desde)
                
#             dia_actual += timedelta(days=1)
#             desde = str(dia_actual).replace('-','')[0:8]
             
#         return dias_laborables   
            
               
# #datetime.today().strftime('%Y%m%d')

# #print(datetime.today().strftime('%Y%m%d'))

# calendario_laboral = CalendarioLaboral()

# calendario_laboral.set_tipo_dia('20230102','N')

# print(calendario_laboral.hoy())

# print(calendario_laboral.dias_laborables())
