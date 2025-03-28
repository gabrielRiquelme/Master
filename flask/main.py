from flask import Flask

app = Flask(__name__)

#Crear rutas
@app.route('/')
def index():
    return "Aprendiendo Flask"


#Pasando parametros
@app.route('/informacion')
@app.route('/informacion/<string:nombre>')#Pasando parametros
def informacion(nombre = None):
    return f"""
            <h1> Pagina informacion</h1>
            <p> Esta es la pagina de informacion</p>
            <h3>Bienvenido,{nombre}</h3>
            """

@app.route('/contacto')
def contacto():
    return "<h1> Pagina contacto</h1>"

@app.route('/lenguajes')
def lenguajes():
    return "<h1> Pagina lenguajes</h1>"

if __name__ == '__main__': 
    app.run(debug=True)
