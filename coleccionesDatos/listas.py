peliculas = ['Batman','Spiderman','El señor de los anillos']
cantantes = list(('2pac','Icecube','SnoopDog'))
"""
print(peliculas)
print(cantantes)
"""
#Indices#
print(peliculas[1])

peliculas.append('Vikings')
print(peliculas)

#Recorrer lista#

for pelicula in peliculas:
    print(f"{peliculas.index(pelicula)}-{pelicula}")

#Listas multidimencionales#

print('*'*20,'Contactos','*'*20)
contactos=[[
    'Antonio',
    'antonio@gmail.com'
],
[
    'luis',
    'luis@gmail.com'
],
[
    'salvador',
    'salvador@gmail.com'
]
]

for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print(f'El nombre es {elemento}')
        else:
            print(f'El email es {elemento}')
    print('\n')

