cantantes = ['2pac','Icecube','SnoopDog','Drake']
numeros=[1,2,5,8,3,4]

#Ordenar

print(numeros)
numeros.sort()
print(numeros)

#Añadir elementos

cantantes.insert(1,'David Bisbal')
print(cantantes)

#Eliminar

cantantes.pop(1)
cantantes.remove('Drake')
print(cantantes)

#Dar la vuelta
print(numeros)
numeros.reverse()
print(numeros)

#Buscar dentro de una lista#

print('2pac' in cantantes)

#Contar elementos

print(len(cantantes))

# cuantas veces aparece un elemento
numeros.append(8)
print(numeros.count(8))

# conseguir indice

print(cantantes.index('2pac'))

#unir lista

cantantes.extend(numeros)
print(cantantes)