# Programacion orientada a objetos 

class Auto:
    #atributos

    color = 'rojo'
    marca = 'ferrari'
    modelo='aventador'
    velocidad=300
    caballaje = 500
    plaza=2

    #metodos, acciones (funciones)

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setModelo(self, modelo):
        self.modelo = modelo

    def getModelo(self):
        return self.modelo


    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self):
        return self.velocidad

#fin delcaracion de clase

coche = Auto()

coche.setColor('Amarillo')

print(coche.marca,coche.getModelo(),coche.color)
print('la velocidad del auto es: ', coche.velocidad)

coche.acelerar()
coche.acelerar()
coche.acelerar()


print('la velocidad del auto es: ', coche.velocidad)

print('------------------------------------------')
# CREANDO OTRO OBJETO
coche2 = Auto()
coche2.setColor('Verde')
coche2.setModelo('Diablo')
print('Coche2: ',coche2.marca,coche2.getColor(),coche2.getModelo())

