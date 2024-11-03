from tkinter import *

ventana = Tk()
ventana.geometry("500x500")

texto = Label(ventana,text="Bievenido a mi programa")
texto.pack()

texto = Label(ventana,text="Aguante boca")
texto.config(
            fg='white',
            bg='black',
            padx=20,
            pady=20,
            font=("Arial",30)
)
texto.pack()

texto = Label(ventana,text="Aguante messi")
texto.config(
            width=100,
            height=100,
            bg="orange"
)
texto.pack(anchor=E)


def pruebas(nombre,apellido,pais):
    return f"Hola {nombre}{apellido} veo que eres de {pais}"

texto = Label(ventana,text=pruebas(nombre='Juan',apellido='Riquelme',pais='Argentina'))
texto.config(
            height=3,
            font=('Arial',18),
            padx=10,
            pady=10,
            bg="green"
)
texto.pack(anchor=NW)

ventana.mainloop()