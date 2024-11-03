from tkinter import *
from tkinter import messagebox as MessageBox

ventana = Tk()
ventana.geometry("700x400")
ventana.title("Formularios en Tkinter | Juan")

def sacarAlerta():
    MessageBox.showinfo("Alerta",'Ojo no completas la url.')
    #MessageBox.showwarning()
    #MessageBox.showerror()
Button(ventana,text="Mostrar alerta: ",command=sacarAlerta).pack()

def sacarSalir(nombre):
    resultado = MessageBox.askquestion("Salir",'Quieres continuar ejecutando la aplicacion?')
    if resultado != 'yes':
        MessageBox.showinfo('Adios',f'Adios {nombre}')
        ventana.destroy()
    
    #MessageBox.showwarning()
    #MessageBox.showerror()

Button(ventana,text="Salir ",command=lambda: sacarSalir('Juan')).pack()







ventana.mainloop()