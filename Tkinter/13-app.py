from tkinter import *
from tkinter import ttk
# Definir ventana.
ventana = Tk()
#ventana.geometry("500x500")
ventana.minsize(500,500)
ventana.title('App')
ventana.resizable(0,0)

#Pantallas
def home():
    # Montar pantalla
    home_label.config(
        fg="white",
        bg="black",
        font=("consolas",30),
        padx=190,
        pady=20
    )
    home_label.grid(row=0,column=0)
    product_box.grid(row=2)
    """
    #Listar productos
    for product in products:
        if len(product) == 3:
            product.append('Añadido')
            Label(product_box, text=product[0]).grid()
            Label(product_box, text=product[1]).grid()
            Label(product_box, text=product[2]).grid()
            Label(product_box,text="-----------------").grid()
    """

    #Listar productos
    for product in products:
        if len(product) == 3:
            product.append('Añadido')
            product_box.insert('',0,text=product[0],values=(product[1]))

    # Ocultar pantalla
    add_label.grid_remove()
    add_frame.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
    
    return True

def add():
    add_label.config(
        fg="white",
        bg="black",
        font=("consolas",30),
        padx=80,
        pady=20
    )
    add_label.grid(row=0,column=0,columnspan=10)

    #campos del formulario

    add_frame.grid(row=1)

    add_name_label.grid(row=1,column=0,padx=5,pady=5,sticky=E)
    add_name_entry.grid(row=1,column=1,padx=5,pady=5,sticky=W)

    add_price_label.grid(row=2,column=0,padx=5,pady=5,sticky=E)
    add_price_entry.grid(row=2,column=1,padx=5,pady=5,sticky=W)

    add_description_label.grid(row=3,column=0,padx=5,pady=5,sticky=NW)
    add_description_entry.grid(row=3,column=1,padx=5,pady=5,sticky=W)
    add_description_entry.config(width=30,height=5,font=("consolas",12),padx=15,pady=15)

    add_separador.grid(row=4)

    BotonForm.grid(row=5, column=1,sticky=E)
    BotonForm.config(padx=15,pady=5,bg="green",fg='white')

    # Ocultar pantalla
    home_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
    product_box.grid_remove()
    return True

def info():
    info_label.config(
        fg="white",
        bg="black",
        font=("consolas",30),
        padx=2,
        pady=20
    )
    info_label.grid(row=0,column=0)

    data_label.grid(row=1,column=0)

    # Ocultar pantalla
    home_label.grid_remove()
    add_label.grid_remove()
    add_frame.grid_remove()
    product_box.grid_remove()
    return True

def add_product():
    products.append(
        [
        name_data.get(),
        price_data.get(),
        add_description_entry.get("1.0","end-1c"),
        ]
    )
    name_data.set("")
    price_data.set("")
    add_description_entry.delete("1.0",END)

    home()

#Variables importantes.
products=[]
name_data=StringVar()
price_data=StringVar()

#Definir campos de pantalla 

#Home
home_label= Label(ventana,text="Inicio")
product_box=Frame(ventana,width=250)

#Tabla de home productos
Label(product_box).grid(row=0)
Label(ventana).grid(row=1)
product_box = ttk.Treeview(height=12,columns=2)
product_box.grid(row=0,column=0,columnspan=2)
product_box.heading("#0", text="Producto",anchor=W)
product_box.heading("#1", text="Precio",anchor=W)

#Add
add_label= Label(ventana,text="Añadir Producto")
#Info
info_label= Label(ventana,text="Informacion Productos ")
#Data label
data_label = Label(ventana,text="Creado por Jr | 2024")


#Campos de formulario

add_frame= Frame(ventana)

add_name_label=Label(add_frame,text="Nombre del producto: ")
add_name_entry = Entry(add_frame, textvariable=name_data)

add_price_label=Label(add_frame,text="Precio del producto: ")
add_price_entry = Entry(add_frame, textvariable=price_data)

add_description_label = Label(add_frame, text="Descripcion: ")
add_description_entry = Text(add_frame)

add_separador=Label(add_frame)

BotonForm = Button(add_frame,text="Guardar",command=add_product)

#Cargar pantallas - MAIN
home()

#Menu superior
menu_superior = Menu(ventana)
menu_superior.add_command(label="Inicio",command=home)
menu_superior.add_command(label="Añadir",command=add)
menu_superior.add_command(label="Informacion",command=info)
menu_superior.add_command(label="Salir",command=ventana.quit)

# Cargar Menu
ventana.config(menu=menu_superior)

# Cargar ventana
ventana.mainloop()