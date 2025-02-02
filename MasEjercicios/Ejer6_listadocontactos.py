import os

ruta_archivo = r'C:\Users\sofia\OneDrive\Documentos\Master\MasEjercicios\listado.txt'


def crearListin():
    if not os.path.isfile(ruta_archivo):
        with open(ruta_archivo, 'w') as crear:
            print('Se genero archivo ya que no existia')
    else:
        print('Directorio ya generado no hago nada')

def agregarUser():
    nombrecontacto = input ('Ingrese nombre de contacto: ')
    telefonoContacto = input('Ingrese contacto: ')  

    with open(ruta_archivo, 'a') as escribir:
        escribir.write(f'{nombrecontacto} {telefonoContacto}\n')

def mostrarContacto():
    try:
        contactoBuscado = input('Ingrese nombre de contacto buscado o ingrese "ALL" para listar todos: ')
        if contactoBuscado != 'ALL':
            with open(ruta_archivo, 'r') as lectura:
                renglon = lectura.readlines()
                for palabra in renglon:
                    subcadena = palabra.split()
                    if subcadena[0] == contactoBuscado.strip().lower():
                        print(palabra)
        else:
            with open(ruta_archivo, 'r') as lecturaAll:
                print(lecturaAll.read())
    except Exception:
        print('Contacto no encontrado...')

def eliminarContacto():
    contactoBuscado = input('Ingrese nombre de contacto buscado: ')
    try:
        with open(ruta_archivo, 'r') as eliminar:
            lineas = [linea.strip() for linea in eliminar if contactoBuscado.lower() not in linea.lower()]
        
        with open(ruta_archivo, 'w') as f:
            for linea in lineas:
                f.write(linea + "\n")
        
        print("Contacto eliminado con éxito.")
    except FileNotFoundError:
        print(f"El archivo '{ruta_archivo}' no existe.")

#MAIN    


accion = 99
while accion != 5:
    accion = int(input('''
        ***Ingrese el numero correspondiente a la accion que desea realizar***
        1 = Crear listado en caso de no existir
        2 = Escribir contacto
        3 = Ver contacto
        4 = Eliminar contacto
        5 = Salir == '''))
    if accion == 1:
        crearListin()
    elif accion == 2:
        agregarUser()
    elif accion ==3:
        mostrarContacto()
    elif accion == 4:
        eliminarContacto()
    elif accion == 5:
        print('Gracaias por usar el programa saludos')
    