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
            width=400,
            height=400,
            bg="orange"
)
texto.pack(anchor=E)

ventana.mainloop()