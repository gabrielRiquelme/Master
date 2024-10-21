from io import open
import pathlib
import shutil
"""
#Abrir archivo
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
print(ruta)
archivo = open(ruta, "a+")

#Escribir
archivo.write('*******Soy un texto desde python**********\n')

archivo.close()

#Abrir archivo
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
print(ruta)
archivo_lectura = open(ruta, "r")

#leer contenido

#contenido = archivo_lectura.read()
#print(contenido)

#Leer y guardar en lista
lista = archivo_lectura.readlines()

archivo_lectura.close()

for elemento in lista:
    #lista_frase = frase.split() por cada elemento si hay un espacio lo guarda en listas
    print("-"+elemento.center(100))

#copiar archivos
ruta_Original = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado.txt"

shutil.copyfile(ruta_Original,ruta_nueva)

#mover archivo

ruta_Original = str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado_nuevo.txt"

shutil.move (ruta_Original,ruta_nueva)

#ELiminar
"""
import os
"""
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado_nuevo.txt"
os.remove(ruta_nueva)
"""
#comprobar si existe

import os.path

#print(os.path.abspath("../"))
ruta_comprobar = (os.path.abspath("./")+"/fichero_texto")

print(ruta_comprobar)


if os.path.isfile(os.path.abspath("./")+"/fichero_texto.txt"):
    print('EL archivo existe')
else:
    print('EL archivo no existe')