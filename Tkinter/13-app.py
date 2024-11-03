from tkinter import *

# Definir ventana.
ventana = Tk()
ventana.geometry("500x500")
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

    # Ocultar pantalla
    add_label.grid_remove()
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
    add_name_label.grid(row=1,column=0,padx=5,pady=5,sticky=E)
    add_name_entry.grid(row=1,column=1,padx=5,pady=5,sticky=W)



    # Ocultar pantalla
    home_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()

    return True

def info():
    info_label.config(
        fg="white",
        bg="black",
        font=("consolas",30),
        padx=25,
        pady=20
    )
    info_label.grid(row=0,column=0)

    data_label.grid(row=1,column=0)

    # Ocultar pantalla
    home_label.grid_remove()
    add_label.grid_remove()

    return True

#Variables importantes.

name_data=StringVar()
price_data=StringVar()

#Definir campos de pantalla 

#Home
home_label= Label(ventana,text="Inicio")
#Add
add_label= Label(ventana,text="Añadir Producto")
#Info
info_label= Label(ventana,text="Informacion Productos ")
#Data label
data_label = Label(ventana,text="Creado por Jr | 2024")


#Campos de formulario

add_name_label=Label(ventana,text="Nombre del producto: ")
add_name_entry = Entry(ventana, textvariable=name_data)

add_price_label=Label(ventana,text="Precio del producto: ")
add_price_entry = Entry(ventana, textvariable=price_data)

add_description_label = Label(ventana, text="Descripcion: ")
add_description_entry = Text(ventana)
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