notas = 0
cant_alumnos = int(input('Ingrese numero de alumnos:'))

for i in range(1,cant_alumnos+1):
    notas = int(input(f'Ingrese nota de alumno {i}: '))
    if notas >= 7:
        print(f'El alumno {i} aprobo con {notas}')
    else:
        print(f'El alumno {i} reprobo.')