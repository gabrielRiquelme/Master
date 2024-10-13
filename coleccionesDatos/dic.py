# Tipo de dato de coleccion de valores que almacena conjunto de datos en formato clave valor.

persona = {
    'nombre':'Juan',
    'apellido':'Riquelme',
    'web':'JuanRiquelmeWEB'
}

print(persona)

#Lista con diccionarios.

contactos = [
    {
        'nombre':'Juan',
        'email':'gabrielcabj986@gmail.com'
    },
    {
        'nombre':'Luis',
        'email':'luis@gmail.com'
    },
    {
        'nombre':'cristian',
        'email':'cristiandelosperales@gmail.com'
    }
]

print(contactos)
print('#'*50,'MODIFICO de juan a antoñito','#'*50)
contactos[0]['nombre']='Antoñito'
print(contactos)
print('#'*50,'imprimo contactos','#'*50)
for contacto in contactos:
    print(f'Nombre:{contacto['nombre']}')
    print(f'email:{contacto['email']}')
    print('(************************************)')