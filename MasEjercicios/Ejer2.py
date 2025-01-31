def inum():
    n = int(input('Ingrese un numero entre 1 & 10: '))
    
    if n >= 1 and n <=10:
        nombre = str(f'tabla-{n}.txt')
        print(nombre)
        try:
            archivo = open(nombre, "r")
            
            print(archivo.read())
            
            archivo.close()
        except Exception:
            print('Tabla no encontrada')
                
        

inum()

'''
Escribir una función que pida un número entero entre 1 y 10, lea el fichero tabla-n.txt con la tabla de multiplicar de ese número, done n es el número introducido, y la muestre por pantalla. Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.
'''
