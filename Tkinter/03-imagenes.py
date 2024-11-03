from tkinter import *
from PIL import Image, ImageTk

ventana = Tk()
ventana.geometry("700x500")

Label(ventana,text='Hola soy una juan').pack(anchor=W)

imagen= Image.open('./Tkinter/imagenes/fondo.jpg')
render = ImageTk.PhotoImage(imagen)

Label(ventana,image=render).pack(anchor=CENTER)

ventana.mainloop()