lista = []
valor=''
while len(lista) <= 120 or valor=='parar':
    if valor == 'parar':
        break
    else:
        valor = input('Ingrese valores: ')
        lista.append(valor)

print(lista)