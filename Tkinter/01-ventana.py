from tkinter import *
import os.path




#Crear ventana
ventana = Tk()

#titulo ventana
ventana.title('Interfaz')

#Comprobar si existe archivo
ruta_icono = os.path.abspath('./imagenes/github.ico')
if not os.path.isfile(ruta_icono):
    ruta_icono=os.path.abspath('./Tkinter/imagenes/github.ico')

#Icono de la ventana raiz
#ventana.iconbitmap(ruta_icono)

#Cambio en el tamaño de la ventana
ventana.geometry("750x450")

#bloquear el tamaño de la ventana
ventana.resizable(1,0)

#Arrancamos y mostramos la ventana hasta que se cierre
ventana.mainloop()