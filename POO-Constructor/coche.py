# Programacion orientada a objetos 

class Coche:
    #atributos

    color = 'rojo'
    marca = 'ferrari'
    modelo='aventador'
    velocidad=300
    caballaje = 500
    plaza=2
    
    #Visibilidad

    soy_publico = 'Hola soy publico'

    __soy_privado = 'Soy privado'

    #constructor

    def __init__(self,color,marca,modelo,velocidad,caballaje,plaza):
        self.color = color
        self.marca= marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje= caballaje
        self.plaza = plaza

    def getPrivado (self):
        return self.__soy_privado

    #metodos, acciones (funciones)

    #COLOR

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color
    #MODELO

    def setModelo(self, modelo):
        self.modelo = modelo

    def getModelo(self):
        return self.modelo
    
    #MARCA

    def setMarca(self, marca):
        self.marca = marca

    def getMarca(self):
        return self.marca


    #MAS FUNCIONES

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self):
        return self.velocidad
    
    def getInfo(self):

        informacion = ('--------Informacion coche -----------')
        informacion += (f'\n color:{self.getColor()}')
        informacion += (f'\n Marca:{self.getMarca()}')
        informacion += (f'\n Modelo:{self.getModelo()}')
        informacion += (f'\n Velocidad:{self.getVelocidad()}')

        return informacion
        
#fin delcaracion de clase


