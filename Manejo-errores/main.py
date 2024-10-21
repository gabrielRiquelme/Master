#Capturar y manejar errores
"""
try:
    nombre = input('Ingrese su nombre: ')
    if len(nombre)>1:
        nombre_usuario = 'El nombre es' + nombre
        
    print(nombre_usuario)

except:
    print('Ha ocurrido un error,ingrese bien su nombre')
else:
    print("Nombre ingresado correctamente")
finally:
    print('Fin de ejecucion')

"""
try:
    numero = input('Ingrese un numero: ')
    print('El cuadrado de un numeros es: '+str(numero*numero))
except:
    print('Se ingreso mal ')