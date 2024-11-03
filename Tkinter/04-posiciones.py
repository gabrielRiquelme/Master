from tkinter import *

ventana = Tk()
#ventana.geometry("500x500")

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
texto.pack(side=TOP,fill=X,expand=YES)


texto = Label(ventana,text='basico 1')
texto.config(
            height=3,
            font=('Arial',18),
            padx=10,
            pady=10,
            bg="green"
)
texto.pack(side=LEFT,fill=X,expand=YES)


texto = Label(ventana,text='basico 2')
texto.config(
            height=3,
            font=('Arial',18),
            padx=10,
            pady=10,
            bg="red"
)
texto.pack(side=LEFT,fill=X,expand=YES)

texto = Label(ventana,text="basico 3")
texto.config(
            height=3,
            font=('Arial',18),
            padx=10,
            pady=10,
            bg="orange"
)
texto.pack(side=LEFT,fill=X,expand=YES)

ventana.mainloop()