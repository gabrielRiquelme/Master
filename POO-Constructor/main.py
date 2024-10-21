from coche import Coche

carro = Coche("Amarillo","Renault","Clio", 15 , 2000 , 4)

print(carro.getInfo())

carro2 = Coche("Fuxia","Civic","GTR", 200 , 5000 , 4)

print(carro2.getInfo())

carro3 = Coche("Negro","Volskwagen","Gol Trend", 100 , 1000 , 4)

print(carro3.getInfo())

#Detectar tipado

if type(carro3) == Coche:
    print('Es un objeto correcto !')
else:
    print('No es un objeto.')

#Visibilidad publica y privada

print(carro.soy_publico)
print(carro.getPrivado())