lista = []
valor=''

for i in range(1,121,1):
    if valor == 'parar':       
        print('Usted a salido o a llegado a 120 caracteres')
        break
    else:
        valor = input('Ingrese valores: ')
        lista.append(valor)
        i = i +1

print(lista)
