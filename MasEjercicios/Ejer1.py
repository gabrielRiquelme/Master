def inum():
    n = int(input('Ingrese un numero entre 1 & 10: '))

    if n >= 1 and n <=10:
        archivo = open(f"tabla-{n}.txt", "w")
        for i in range(1,10+1,1):
            archivo.write(f'{n} * {i} == {n*i} \n')
            
        archivo.close()
inum()

