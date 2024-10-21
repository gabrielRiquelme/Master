import miModulo 
from miModulo import *
import datetime
import math
import random

miModulo.holaMundo('Juan')

miModulo.suma(10,10)

print(datetime.date.today())

fecha_completa = datetime.datetime.now()

print(fecha_completa)
print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)

fp = fecha_completa.strftime("%d/%m/%Y,%H:%M:%S")

print(f'Fecha personalizada {fp}')

#Modulo Math

print(f'Raiz cuadrada de 10: {math.sqrt(10)}')

print(f'Numero PI: {math.pi}')

print(f'Redondear: {math.ceil(6.5772378392)}')

print(f'Numero aleatorio: {random.randint(25,1000)}') #otro modulo