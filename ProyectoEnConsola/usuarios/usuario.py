import usuarios.conexion as conexion
import datetime
import hashlib


connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

result = []
class Usuario:

    def __init__(self,nombre,apellido,email,password):
        self.nombre=nombre
        self.apellido=apellido
        self.email=email
        self.password=password

    def registrar(self):
        fecha = datetime.datetime.now()

        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        
        sql="Insert into usuarios values(null,%s,%s,%s,%s,%s)"
        usuario=(self.nombre, self.apellido, self.email, cifrado.hexdigest(), fecha)
        
        try:
            cursor.execute(sql, usuario)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result= [0,self]
        
        return result
    
    def identificar(self):
        #Consulta para verificar si existe el usuario
        sql = "SELECT * FROM usuarios where email = %s and password = %s"


        #cifrado pass
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        #datos para la consulta
        usuario=(self.email,cifrado.hexdigest())

        cursor.execute(sql,usuario)
        result=cursor.fetchone()
        datos = []
        if result:
            cursor.execute(sql,usuario)
            datos = cursor.fetchone()
            return True, datos
        else:
            return False