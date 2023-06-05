import mysql.connector

BBDD_HOST = '127.0.0.1'
BBDD_USER = 'bladimir'
BBDD_PASS = 'America_10'
BBDD_BBDD = 'agencia_de_viajes'

miConexion = mysql.connector.connect(
    host    = BBDD_HOST,
    user    = BBDD_USER,
    passwd  = BBDD_PASS,
    db      = BBDD_BBDD
)

cur = miConexion.cursor()

cur.execute("select * from viaje;")

for viaje in cur.fetchall():
    print (viaje)
    
sql = """
insert into avion (id_avion, modelo) values (1, "Airbus 319");
insert into avion (id_avion, modelo) values (2, "Airbus 320");
insert into avion (id_avion, modelo) values (3, "Airbus 321");
insert into avion (id_avion, modelo) values (4, "Boeing 737");
insert into avion (id_avion, modelo) values (5, "Boeing 747");
"""

for sede in cur.execute(sql, multi=True): pass

miConexion.commit()
    
miConexion.close()

