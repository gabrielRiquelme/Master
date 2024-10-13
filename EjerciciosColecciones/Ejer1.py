numeros=[1,3,2,5,4,7,9,8]

def recorrer(numeros):
    retorno=''
    print(f'Recorremos lista:')
    for elemento in numeros:
        retorno = retorno + str(elemento)
        retorno = retorno + '\n'
    return print(retorno)

recorrer(numeros)

print(f'La lista desordenada se ve asi:{numeros}')
numeros.sort()
print(f'La lista ordenada se ve asi: {numeros}')

print(f'La longitud de la lista es: {len(numeros)}')

num = int(input('Ingrese un numero para buscarlo en la lista: '))
comprobar = isinstance(num,int)

while not comprobar or num <= 0:
    num = int(input('Ingrese un numero para buscarlo en la lista: '))
else:
    if num in numeros:
        print(f'El numero {num} se encuentra en la lista en la posicion {numeros.index(num)}')
    else:
        print(f'El numero {num} no se encuentra en la lista.')

