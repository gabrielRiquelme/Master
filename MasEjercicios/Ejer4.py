from urllib import request

try:
    archivo = request.urlopen('https://raw.githubusercontent.com/gabrielRiquelme/ip-public-repo-2c2024/refs/heads/main/README.md')

    datosProcesados = archivo.read().decode('utf-8')
    palabra=datosProcesados.split()
    contPal = len(palabra)

    print(contPal)

except Exception:
    print('No fue posible ingresar a el archivo.')