import os
import shutil

directorio = os.getcwd()
listadoArchivos = os.listdir()

directorios = ['Documentos', 'Imagenesyvideos', 'Ejecutablescomprimidos']

for directorio in directorios:
    ruta = os.path.join(os.getcwd(), directorio)
    if not os.path.exists(ruta):
        os.mkdir(directorio)


for archivo in listadoArchivos:
    extension = archivo.split('.')[-1]

    listaDocs = ['csv','txt','pdf','md','xlsx']
    listaEjecutables = ['py','exe', 'msi','deb','zip','7z']
    listaMedia = ['MP3','mp4','PNG','JPEG','webm']
    
    if extension in listaDocs:
        if os.path.exists(archivo):
            try:
                shutil.move(archivo, directorio+ '\Documentos')
            except Exception as e:
                print(f"Error al mover el archivo {archivo}: {e}")

    elif extension in listaEjecutables:
        if os.path.exists(archivo):
            try:
                shutil.move(archivo, directorio+ '\Ejecutablescomprimidos')
            except Exception as e:
                print(f"Error al mover el archivo {archivo}: {e}")
    else:
        if extension in listaMedia:
            if os.path.exists(archivo):
                try:
                    shutil.move(archivo, directorio+ '\Imagenesyvideos')
                except Exception as e:
                    print(f"Error al mover el archivo {archivo}: {e}")
                    

        
    
        
        

