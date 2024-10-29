from tkinter import *
import os.path

class Programa:

    def __init__(self):
        self.title = "Master en python"
        self.icon = "./imagenes/github.ico"
        self.icon_alt = "./Tkinter/imagenes/github.ico"
        self.size = "700x470"
        self.resizable = True
    
    def cargar(self):
        #Crear ventana
        ventana = Tk()
        self.ventana = ventana
        #titulo ventana
        ventana.title(self.title)

        #Comprobar si existe archivo
        ruta_icono = os.path.abspath('self.ico')
        if not os.path.isfile(ruta_icono):
            ruta_icono=os.path.abspath('self.icon_alt')

        #Icono de la ventana raiz
        #ventana.iconbitmap(ruta_icono)

        #Cambio en el tamaño de la ventana
        ventana.geometry(self.size)

        #bloquear el tamaño de la ventana
        if self.resizable:
            ventana.resizable(1,1)
        else:
            ventana.resizable(0,0)
        

    def addTexto(self,dato):
        texto = Label(self.ventana,text=dato)
        texto.pack()

    def mostrar(self):
        #Arrancamos y mostramos la ventana hasta que se cierre
        self.ventana.mainloop()

#PROGRAMA PRINCIPAL.
programa = Programa()  
programa.cargar()
programa.addTexto('Aguante boca')
programa.mostrar()