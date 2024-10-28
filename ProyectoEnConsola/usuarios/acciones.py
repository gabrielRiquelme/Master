import usuarios.usuario as modelo


class Acciones():
    
    def registro(self):
        print('Perfeco,vamos a registrarnos en el sistema...')
        
        nombre = input('Cual es tu nombre?: ')
        apellido = input('Cual es tu apellido?: ')
        email = input('Cual es tu email?: ')
        password = input('Cual es tu contraseña?: ')

        usuario=modelo.Usuario(nombre,apellido,email,password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f'Registro exitoso,bienvenido {nombre}')
        else:
            print('NO se a registrado correctamente, intente nuevamente')

    def login(self):
        print('Perfecto, ingrese sus credenciales')

    try:
        email = input('Cual es tu email?: ')
        password = input('Cual es tu contraseña?: ')

        usuario = modelo.Usuario('', '',email, password)

        logueoUser,datos = usuario.identificar()
        
        if logueoUser:
            print(f'BIenvenido {datos[1]},te has logueado en el sistema a las {datos[5]}')
            self.proximasAcciones(datos)
        else:
            print('Logueo incorrecto, verifique sus datos.')
    
    except Exception as e:
        #print(type(e))
        #print(type(e).__name__)
        print(f"Login incorrecto! intentalo mas tarde.")

    def proximasAcciones(self,datos):
        pass