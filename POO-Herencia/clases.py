"""
Posibilidad de compartir atributos y metodos entre clases. Tambien que clases hereden de clases
"""

class Persona:
    """
    nombre
    apellido
    altura
    edad
    """

    def getNombre(self):
        return self.Nombre

    def getApellido(self):
        return self.Apellido

    def getAltura(self):
        return self.Altura
    
    def getedad(self):
        return self.Edad
    
    def setNombre(self,nombre):
        self.Nombre = nombre

    def setApellido(self,apellido):
        self.Apellido = apellido

    def setAltura(self, altura):
        self.Altura = altura

    def setEdad(self, edad):
        self.Edad = edad

    def hablar(self):
        return 'EStoy hablando'
    
    def caminar(self):
        return 'EStoy caminando'
    
    def dormir(self):
        return 'Estoy durmiendo'
    
class Informatico(Persona):
    """
    lenguaje
    experiencia
    """
    def __init__(self):
        self.lenguajes = 'HTML,CSS,JS,PYTHON'
        self.experiencia = 5

    def getLenguajes(self):
        return self.lenguajes

    def aprender(self,lenguajes):
        self.lenguajes = lenguajes
        return self.lenguajes

    def programar(self):
        return "Estoy programando"

    def reperar(self):
        return "Eh reparado tu PC"
    
class TecnicoRedes(Informatico):

    def __init__(self):
        super().__init__() # Sentencia para heredar propiedades de base de datos.
        self.auditarRedes = 'Experto'
        self.experiencia = 15

    def auditoria(self):
        return 'Estoy auditando una red'