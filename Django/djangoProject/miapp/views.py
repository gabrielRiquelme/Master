from django.shortcuts import render,HttpResponse

# Create your views here.
# MVC = Modelo vista controlador == Acciones (metodos)
# MVT = Modelo template vista == Acciones (metodos)

def index(request):
    html ="""<h1>Hola mundo con Django!</h1>"""
    return HttpResponse(html)

def hola_mundo(request):

    return HttpResponse("""
                        <h1>Hola mundo con Django!</h1>
                        <h3>Echo por Juan!</h3>
                        """)

def pagina(request):
    return HttpResponse("""
                        <h1>Pagina de mi web</h1>
                        <h3>Echo por Juan!</h3>
                        """)