import mysql.connector

class BBDD:
    
    def __init__(self):

        BBDD_HOST = 'localhost'
        BBDD_USER = 'root'
        BBDD_PASS = 'America10'
        BBDD_BBDD = 'agencia_de_viajes'

        self.conexion = mysql.connector.connect(
            host = BBDD_HOST,
            user = BBDD_USER,
            passwd = BBDD_PASS,
            db = BBDD_BBDD
        )

        self.cursor = self.conexion.cursor()
        
        
class Query:
    
    @staticmethod
    def ejec(query):
        
        bbdd = BBDD()
        
        bbdd.cursor.execute(query)
        
        data = 0
        
        if query.upper().startswith('SELECT'):
            data = bbdd.cursor.fetchall()
        else:
            bbdd.conexion.commit()
            
        bbdd.conexion.close()
        
        return data