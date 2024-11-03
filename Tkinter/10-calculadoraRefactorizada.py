from tkinter import *
from tkinter import messagebox

class Calculadora:
    
    def __init__(self,alertas):
        self.num1 = StringVar()
        self.num2= StringVar()
        self.resultado = StringVar()
        self.alertas = alertas

    def cFloat(self,numero):
        try:
            result=float(numero)
        except:
            result=0
            messagebox.showerror('Error','Introduce bien los datos.')
        return result

    def mostrarResultado (self):
        self.alertas.showinfo('Resultado',f'El resultado es: {self.resultado.get()}')    
        self.num1.set("")
        self.num2.set("")

    def suma(self):
            self.resultado.set(self.cFloat(self.num1.get()) + self.cFloat(self.num2.get()))
            self.mostrarResultado()
        
    def resta(self):
        self.resultado.set(self.cFloat(self.num1.get()) - self.cFloat(self.num2.get()))
        self.mostrarResultado()

    def multiplicacion(self):
        self.resultado.set(self.cFloat(self.num1.get()) * self.cFloat(self.num2.get()))
        self.mostrarResultado()

    def division(self):
        self.resultado.set(self.cFloat(self.num1.get()) / self.cFloat(self.num2.get()))
        self.mostrarResultado()

ventana = Tk()
ventana.geometry("700x400")
ventana.title("Calculadora en Tkinter | Juan")
ventana.config(
    bd=50
)

calculadora = Calculadora(messagebox)


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
Entry(marco,textvariable=calculadora.num1,justify=CENTER).pack()

Label(marco,text="Ingresa numero 2 : ").pack()
Entry(marco,textvariable=calculadora.num2,justify=CENTER).pack()

# Mostrar resultado

Label(marco,text="Resultado: ").pack()
texto_recogido=Label(marco,textvariable=calculadora.resultado)
texto_recogido.pack()

# Botones

Button(marco,text="Suma",command=calculadora.suma).pack(side='left',fill=X,expand=YES)
Button(marco,text="Resta",command=calculadora.resta).pack(side='left',fill=X,expand=YES)
Button(marco,text="Divsion",command=calculadora.division).pack(side='left',fill=X,expand=YES)
Button(marco,text="Multiplicacion",command=calculadora.multiplicacion).pack(side='left',fill=X,expand=YES)

ventana.mainloop()