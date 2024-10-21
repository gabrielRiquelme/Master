import os

#Crear carpeta
if not os.path.isdir("./mi_carpeta"):
    os.mkdir("./mi_carpeta")
else:
    print('Ya existe la carpeta')


#copiar carpeta
import shutil

"""
ruta_Original = "./mi_carpeta"
ruta_nueva = "./mi_carpeta_copiada"

shutil.copytree(ruta_Original,ruta_nueva)
"""
#eliminar

os.rmdir('./mi_carpeta')

#listar contenido
ruta_comprobar = (os.path.abspath("./")+"/mi_carpeta_copiada")
print(ruta_comprobar)


print("Contenido de carpeta")
contenido = os.listdir(ruta_comprobar)
for fichero in contenido:
    print(f"Fichero: "+fichero)
