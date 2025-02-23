import os
import shutil

directorio = os.getcwd()
listadoArchivos = os.listdir()


os.mkdir('Media')
os.mkdir('Documentos')
os.mkdir('Imagenes')
os.mkdir('Ejecutables y comprimidos')


for archivo in listadoArchivos:
    extension = archivo.split('.')[-1]
    listaDocs = ['csv','txt','pdf','md']
    if extension in listaDocs:
        if os.path.exists(archivo):
            try:
                shutil.move(archivo, directorio+ '\Documentos')
            except Exception as e:
                print(f"Error al mover el archivo {archivo}: {e}")
        else:
            print(f"El archivo {archivo} no existe")


