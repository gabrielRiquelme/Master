import usuarios.usuario as modelo
import notas.acciones

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
    
        try:
            print('Perfecto, ingrese sus credenciales')

        
            email = input('Cual es tu email?: ')
            password = input('Cual es tu contraseña?: ')

            usuario = modelo.Usuario('', '',email, password)

            logueoUser,datos = usuario.identificar()
            
            if logueoUser:
                print(f'BIenvenido {datos[1]},te has logueado en el sistema a las {datos[5]}')
                return self.proximasAcciones(datos)
            else:
                print('Logueo incorrecto')

        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print(f"Login incorrecto! intentalo mas tarde.")

    def proximasAcciones(self,datos):
        print("""
        Acciones disponibles:
            -Crear notas(crear - 1)
            -Mostrar tus notas(mostrar - 2)
            -Eliminar(eliminar - 3)
            -Salir(Salir - 4)
        """)

        accion = input("¿Que quieres hacer?")
        hazEl = notas.acciones.Acciones()


        if accion == 'crear' or accion == '1':
            hazEl.crear(datos)
            self.proximasAcciones(datos)

        elif accion == 'mostrar' or accion == '2':
            hazEl.mostrar(datos)
            self.proximasAcciones(datos)

        elif accion == 'eliminar' or accion == '3':
            hazEl.borrar(datos)
            self.proximasAcciones(datos)

        elif accion == 'salir' or accion == '4':
            print('Perfecto vamos a salir')
            exit()
    