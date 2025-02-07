diccionario ={
    'Euro':'E',
    'Dollar': '$',
    'Yen':'Y'
}

#valor = input('Ingrese divisa a mostrar (Euro/Dollar/Yen): ')
#print(diccionario[valor])

diccionario_infor = {
    'nombre':'',
    'edad': '',
    'direccion':'',
    'telefono':''
    }

diccionario_infor['nombre']=input('ingrese su nombre: ')
diccionario_infor['edad']=int(input('ingrese su edad: '))
diccionario_infor['direccion']=input('ingrese direccion: ')
diccionario_infor['telefono']=int(input('ingrese su telefono: '))

print(diccionario_infor.items())