from tkinter import *

ventana = Tk()
ventana.geometry("800x300")

encabezado = Label(ventana, text="Formulario 2")
encabezado.config(
    padx=15,
    pady=15,
    bg='green',
    fg='white',
    font=('consolas',20)
)
encabezado.grid(row=0,column=0,columnspan=5,sticky=W)

#Botones Check
web = IntVar()
movil = IntVar()
backend = IntVar()

def mostrarProfesion():
    texto = ""

    if web.get():
        texto += 'Desarrollo Web'
        mostrar.config(
            text= texto,
            bg='green',
            fg='white'
        )

    if backend.get():
        if web.get():
            texto += 'Y desarrollo Backend'
        else:
            texto += 'Desarrollo Backend'
    
Label(ventana,text="¿A que te dedicas?").grid(row=1,column=0)
Checkbutton(
    ventana,
    text="Desarrollo web",
    variable=web,
    onvalue=1,
    offvalue=0,
    command=mostrarProfesion
).grid(row=2,column=0)
Checkbutton(
    ventana,
    text="Backend",
    variable=backend,
    onvalue=1,
    offvalue=0,
    command=mostrarProfesion
).grid(row=3,column=0)

mostrar = Label(ventana)
mostrar.grid(row=5,column=0)
# Radio Button.
opcion = StringVar()
opcion.set(None)

def marcar():
    marcado.config(text=opcion.get())

Label(ventana,text='Cual es tu genero ?').grid(row=6)

Radiobutton(ventana,text='Masculino',variable=opcion,value='Masculino',command=marcar).grid(row=7)
Radiobutton(ventana,text='Femenino',variable=opcion,value='Femenino',command=marcar).grid(row=8)

marcado = Label(ventana)
marcado.grid(row=9)
# Opciones menu
def seleccionar():
    vistaSel.config(text=opcion.get())

opcion = StringVar()
opcion.set('opcion 1')

Label(ventana,text='Selecciona una opcion').grid(row=5,column=1)
select=OptionMenu(ventana,opcion,"opcion 1","opcion 2","opcion 3")
select.grid(row=6,column=1)
Button(ventana,text="VER",command=seleccionar).grid(row=7,column=1)
vistaSel = Label(ventana)
vistaSel.grid(row=8,column=1)


ventana.mainloop()