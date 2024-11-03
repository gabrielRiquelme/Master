from tkinter import *
from tkinter import messagebox

ventana = Tk()
ventana.geometry("700x400")
ventana.title("Calculadora en Tkinter | Juan")
ventana.config(
    bd=50
)

def cFloat(numero):
    try:
       result=float(numero)
    except:
        result=0
        messagebox.showerror('Error','Introduce bien los datos.')
    return result

def mostrarResultado ():
    messagebox.showinfo('Resultado',f'El resultado es: {resultado.get()}')    
    num1.set("")
    num2.set("")

def suma():
    try:
        resultado.set(cFloat(num1.get()) + cFloat(num2.get()))
        mostrarResultado()
    except:
        messagebox.showerror('Error','Introduce bien los datos.')
    

def resta():
    resultado.set(cFloat(num1.get()) - cFloat(num2.get()))
    mostrarResultado()

def multiplicacion():
    resultado.set(cFloat(num1.get()) * cFloat(num2.get()))
    mostrarResultado()

def division():
    resultado.set(cFloat(num1.get()) / cFloat(num2.get()))
    mostrarResultado()


num1 = StringVar()
num2= StringVar()
resultado = StringVar()


marco = Frame(ventana, width=250,height=190)
marco.config(
    bd=5,
    padx=15,
    pady=15,
    relief=SOLID

)
marco.pack(side=TOP,anchor=CENTER)
marco.pack_propagate(False)
# Ingreso de datos.

Label(marco,text="Ingresa numero 1 : ").pack()
Entry(marco,textvariable=num1,justify=CENTER).pack()

Label(marco,text="Ingresa numero 2 : ").pack()
Entry(marco,textvariable=num2,justify=CENTER).pack()

# Mostrar resultado

Label(marco,text="Resultado: ").pack()
texto_recogido=Label(marco,textvariable=resultado)
texto_recogido.pack()

# Botones

Button(marco,text="Suma",command=suma).pack(side='left',fill=X,expand=YES)
Button(marco,text="Resta",command=resta).pack(side='left',fill=X,expand=YES)
Button(marco,text="Divsion",command=division).pack(side='left',fill=X,expand=YES)
Button(marco,text="Multiplicacion",command=multiplicacion).pack(side='left',fill=X,expand=YES)

ventana.mainloop()