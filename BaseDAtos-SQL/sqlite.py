import sqlite3

# Conexion SQLITE 3

conexion = sqlite3.connect('pruebas.db')

#Crear Cursor para ejecutar sentencias

cursor = conexion.cursor()

#Crear tabla

cursor.execute("""CREATE TABLE IF NOT EXISTS productos(
id INTEGER PRIMARY KEY AUTOINCREMENT,
titulo varchar (255),
descripcion text,
precio int (255)
               
)
""")
conexion.commit()

#Insertar datos
"""
cursor.execute("INSERT INTO productos VALUES (NULL,'Primer producto','Descripcion',550)")
conexion.commit() #Guardar cambios
"""

#Borrar productos
cursor.execute("DELETE FROM productos")
conexion.commit()

#Insertar muchos productos

productos = [
    ('Laptop','HP I5',700),
    ('Iphone','15',1000),
    ('Alienware','MUy buena',1000),
    ('MacBOK','Pro',2000)
]
cursor.executemany('INSERT INTO productos VALUES(null, ? , ? , ?)',productos)
conexion.commit()

#update

cursor.execute("UPDATE productos SET precio=10000 where precio =700")

# Listar datos

cursor.execute("SELECT * FROM productos WHERE precio >=300;")
productos = cursor.fetchall()

for producto in productos:
    print('id:',producto[0])
    print('Titulo:',producto[1])
    print('Descripcion:',producto[2])
    print('precio:',producto[3])
    print('\n')




#cursor.execute("SELECT titulo FROM productos;")


producto = cursor.fetchone()
print(producto)



#Cerrar conexion
conexion.close()