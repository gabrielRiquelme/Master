""" Multiples excepciones.
try:
    numero = int(input('Ingrese un numero: '))

    print(f'El cuadrado es:'+str(numero * numero))
except TypeError:
    print('Debes convertir tus cadenas a enteros en el codigo')
except ValueError:
    print('Debes ingresar solo numeros enteros')
except Exception as e:
    print('A ocurrido un error: ', type(e).__name__)

"""
#Excepciones personalizadas.

nombre = input('Ingrese su nombre: ')
edad = int(input('Ingrese su edad: '))

if edad < 5 and edad > 110:
    raise ValueError('Edad introduci irreal.')
elif len(nombre) <= 1:
    raise ValueError('')