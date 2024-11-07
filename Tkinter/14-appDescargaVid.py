import youtube_dl
from tkinter import *

def descargaWeb(url,name):
    # URL del video
    url = input('Ingrese la URL del video: ')
    name = input('Ingrese nombre: ')

    # Configuración para descargar el video
    ydl_opts = {
        'format':'best',
        'outtmpl': f'C:/Users/sofia/Videos/Descargas/{name}.%(ext)s',
    }

    # Crea un objeto YoutubeDL y descarga el video
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    print("Descarga completada.")


# Definir ventana.
ventana = Tk()
#ventana.geometry("500x500")
ventana.minsize(500,500)
ventana.title('App')
ventana.resizable(0,0)

#Variables
url= StringVar()
name= StringVar()

#Pantallas
def home():
    # Montar pantalla
    home_label.config(
        fg="white",
        bg="black",
        font=("consolas",30),
        padx=190,
        pady=20
    )
    home_label.grid(row=0,column=0)

#Home
home_label= Label(ventana,text="Inicio")

#Menu superior  
menu_superior = Menu(ventana)
menu_superior.add_command(label="Inicio",command=home)
menu_superior.add_command(label="Salir",command=ventana.quit)

# Cargar Menu
ventana.config(menu=menu_superior)

#Cargar pantallas - MAIN
home()


# Cargar ventana
ventana.mainloop()