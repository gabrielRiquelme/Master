def inum():
    n = int(input('Ingrese un numero entre 1 & 10: '))

    m = int(input('Ingrese otro numero entre 1 & 10: '))    

    if n >= 1 and n <=10 and m >=1 and m <=10:

        nombre = str(f'tabla-{n}.txt')
        print(nombre)
        try:
            archivo = open(nombre, "r")
            extract = archivo.readlines()
            print(extract[m-1].strip())
            
            archivo.close()
        except Exception:
            print('Tabla no encontrada')
                
        

inum()

'''
Escribir una función que pida dos números n y m entre 1 y 10, lea el fichero tabla-n.txt con la tabla de multiplicar de ese número, y muestre por pantalla la línea m del fichero. Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.
'''
