import mysql.connector

#conexion

database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="master_python" # SETEO LA BASE DE DATOS QUE VOY A UTILIZAR, EN ESTE CASO MASTER_PYTHON
)

# Como saber si la conexion es correcta ?
#print(database)
#Devuelve un objeto de tipo MYSQL.

#Nos permite ejecutar las consultas.
cursor = database.cursor()

#Crear base de datos.
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")


"""
#Como ver la base de datos.
cursor.execute('SHOW DATABASES')

for bd in cursor:
    print(bd)
"""
#CREAR TABLAS.
cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
id int(10) auto_increment not null,
marca varchar(40) not null,
modelo varchar(40) not null,
precio float(10,2) not null,             
CONSTRAINT pk_vehiculo PRIMARY KEY(id)
)
""")

#Mostrar tabla.
cursor.execute('SHOW TABLES')

for table in cursor:
    print(table)

#INSERTAR DATO
#cursor.execute("INSERT INTO vehiculos VALUES(null,'audi','A4',20000)")
#

#Carga de datos masiva.
coches = [
    ('Seat','Ibiza',14000),
    ('BMW','Q5',30000),
    ('Mercedes Benza','Z4',40000),
    ('Renault','Clio',6000)
]

#cursor.executemany("INSERT INTO vehiculos VALUES(NULL,%s,%s,%s)",coches)
#where precio >= 10000 and marca ='audi'

#Mostrar datos de tabla + uso de where.
cursor.execute("SELECT * FROM vehiculos ")
result = cursor.fetchall()

print('------TODOS LOS AUTOS-----')
for coche in result:
    print(coche)

#ELIMINAR REGISTROS

cursor.execute("DELETE from vehiculos WHERE marca = 'Renault'")
database.commit()
#Te indica registros borrados + mensaje
print(cursor.rowcount, "BORRADOS")

#Actualizar campos

cursor.execute("UPDATE vehiculos SET modelo='TT' where marca='audi'")
database.commit()
print(cursor.rowcount, "MODIFICADOS.")