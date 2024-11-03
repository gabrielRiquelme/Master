from tkinter import *

ventana = Tk()
ventana.geometry("700x400")
ventana.title("Formularios en Tkinter | Juan")

#Texto encabezado.


encabezado = Label(ventana,text="Formularios Tk | JUAN")
encabezado.config(
    fg="white",
    bg="darkgray",
    font=("Open Sans", 18),
    padx=10,
    pady=10
)

encabezado.grid(row=0,column=0, columnspan=3, sticky=W)

#Label para el campo (Nombre)

label = Label(ventana,text="Nombre")
label.grid(row=1,column=0,sticky=W,padx=5,pady=5)

#Campo de texto (Nombre)

campo_texto=Entry(ventana)
campo_texto.grid(row=1,column=1,sticky=W,padx=5,pady=5)
campo_texto.config(justify="left",state="normal")

#Label para el campo (Apellidos)

label = Label(ventana,text="Apellido(s)")
label.grid(row=2,column=0,sticky=W,padx=5,pady=5)

#Campo de texto (Apellidos)

campo_texto=Entry(ventana)
campo_texto.grid(row=2,column=1,sticky=W,padx=5,pady=5)
campo_texto.config(justify="left",state="normal")

# Label para el campo (Descripcion)
label = Label(ventana,text="Descripcion")
label.grid(row=3,column=0,padx=5,pady=5,sticky=NW)

# Campo de texto GRANDE (descripcion)
campo_grande = Text(ventana)
campo_grande.grid(row=3,column=1,padx=5,pady=5)
campo_grande.config(
    width=30,
    height=5,
    font=("Arial",12)
)

#boton
Label(ventana).grid(row=4,column=1)
boton = Button(ventana,text='Enviar')
boton.grid(row=5,column=1,sticky=W)
boton.config(padx=10,pady=10)





ventana.mainloop()