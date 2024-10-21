lista = ['Hola','Boca','Messi','Real madrid']
strin = 'Hola'
num = 1
bandera = True

def comprobarTipo(valor,tipo):
    resultado = isinstance(valor,tipo)

    if resultado == True:
        print(f'El tipo de datos es correcto')
    else:
        return print('El tipo no coincide.')
    

comprobarTipo(lista,int)
comprobarTipo(strin,int)
comprobarTipo(num,int)
comprobarTipo(bandera,list)