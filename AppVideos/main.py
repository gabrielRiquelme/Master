from tkinter import *
from tkinter import ttk
import os.path
import youtube_dl
import yt_dlp

# Definir ventana.
class App:

    def __init__(self):
        # Atributos iniciales
        self.title = "Download videos"
        self.size = "700x470"
        self.resizable = True
        self.ventana = None  # Inicializamos ventana como None
        self.dato = None  # Inicializamos como None
        self.resultado = None  # Inicializamos como None

    def cargar(self):
        # Crear ventana
        self.ventana = Tk()

        # Inicializar las variables asociadas a la ventana
        self.dato = StringVar(self.ventana)
        self.resultado = StringVar(self.ventana)

        # Configuración de ventana
        self.ventana.title(self.title)
        self.ventana.geometry(self.size)

        # Configuración de redimensionamiento
        if self.resizable:
            self.ventana.resizable(1, 1)
        else:
            self.ventana.resizable(0, 0)

    def TextoTitulo(self, proposito):
        # Crear título
        textoTitulo = Label(self.ventana, text=proposito, font=("Arial", 16))
        textoTitulo.pack(anchor=W, pady=10)

    def descargarVideos(self,name,url):
        # Configuración para descargar el video
        ydl_opts = {
            'format': 'best',
            'outtmpl': f'C:/Users/Juan G. Riquelme/Videos/{name}.%(ext)s',
        }

        # Intentar con youtube_dl
        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                print("Intentando descargar con youtube_dl...")
                ydl.download([url])
            print("Descarga completada con youtube_dl.")
        except Exception as e:
            print(f"Error con youtube_dl: {e}")
            print("Intentando con yt-dlp...")
            
            # Si falla, intentar con yt-dlp
            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                print("Descarga completada con yt-dlp.")
            except Exception as e:
                print(f"Error con yt-dlp: {e}")
                print("No se pudo descargar el video con ninguna librería.")

    def main(self):
        # Crear entrada y botones

        # URL
        url = Label(self.ventana, text="Ingrese URL: ").pack(anchor=NW, pady=5)
        self.entry_url = Entry(self.ventana)  # Nueva variable para el Entry de URL
        self.entry_url.pack(anchor=NW, pady=5)

        # Nombre de video
        titulo = Label(self.ventana, text="Ingrese nombre del video: ").pack(anchor=NW, pady=5)
        self.entry_titulo = Entry(self.ventana)  # Nueva variable para el Entry de título
        self.entry_titulo.pack(anchor=NW, pady=5)

        # Directorio por defecto
        Label(self.ventana,text="Descarga disponible en carpeta de videos ").pack(anchor=W)

        # Botón enviar datos
        Button(self.ventana, text="Descargar", command=lambda: self.descargarVideos(self.entry_url.get(), self.entry_titulo.get())).pack(anchor=NW, pady=5)

    def mostrar(self):
        # Mostrar ventana
        self.ventana.mainloop()


# PROGRAMA PRINCIPAL
descVideos = App()  
descVideos.cargar()
descVideos.TextoTitulo('Descargar videos desde cualquier plataforma')
descVideos.main()
descVideos.mostrar()
