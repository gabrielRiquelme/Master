from urllib import request

try:
    archivo = request.urlopen('https://datosmacro.expansion.com/pib/argentina')
    datos = archivo.readlines()
    for contenido in datos:
            print(f'{contenido}\n')
except Exception:
    print('No fue posible ingresar a el archivo.')