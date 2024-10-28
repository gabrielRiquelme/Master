import notas.nota as modelo

class Acciones:

    def crear(self,datos):
        print(f' {datos[1]}, vamos a crear una nueva nota...')
        titulo = input('Introduce titulo de tu nota: ')
        descripcion = input('Introduce contenido de la nota: ')

        nota = modelo.Nota(datos[0],titulo,descripcion)
        guardar = nota.guardar()

        if guardar[0] >=1:
            print(f'\nPerfecto has guardado la nota correctamente: {nota.titulo}')
        else:
            print(f'No se guardado la nota {datos.nombre}, intentalo nuevamente.')

    
    def mostrar(self,datos):
        print(f'Perfecto {datos[1]} aqui muestro tus notas: ')

        nota = modelo.Nota(datos[0])
        notas = nota.listar()
        for nota in notas:
            print("\n*************************************")
            print(nota[2])
            print(nota[3])
            print("*************************************")

    def borrar(self,datos):
        print(f'Perfecto {datos[1]} eliminaremos la nota')

        titulo = input('Ingrese el titulo de la nota a borrar: ')

        nota = modelo.Nota(datos[0],titulo)
        eliminar = nota.eliminar()
        
        if eliminar[0] >=1:
            print(f'Hemos eliminado la nota: {nota.titulo}')
        else:
            print('Nota no borrada.')