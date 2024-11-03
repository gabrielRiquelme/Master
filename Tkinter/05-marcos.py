from tkinter import *

ventana = Tk()
ventana.title("Marcos | Master Python")
ventana.geometry("700x700")

# Marco padre
marco_padre1 = Frame(ventana,width=250, height=250)
marco_padre1.config(bg='green',bd=5,relief='solid')
marco_padre1.pack(side=BOTTOM, fill=X,expand=YES)

# Marco 1
marco = Frame(marco_padre1,width=250, height=250)
marco.config(bg='yellow',bd=5,relief='solid')
marco.pack(side=LEFT, anchor=SW)

texto = Label(marco,text="Primer marco")
texto.config(
bg="red",
fg="white",
font=("Arial",20),
height=10,
width=10,
bd=3,
relief=SOLID,
anchor=CENTER
)
texto.pack(anchor=CENTER,fill=Y,expand=YES)



# Marco padre 2
marco_padre2 = Frame(ventana,width=250, height=250)
marco_padre2.config(bg='blue',bd=5,relief='solid')
marco_padre2.pack(side=TOP, anchor=N,fill=X,expand=YES)

# Marco 1
marco = Frame(marco_padre2,width=250, height=250)
marco.config(bg='red',bd=5,relief='solid')
marco.pack(side=LEFT, anchor=SW)


ventana.mainloop()