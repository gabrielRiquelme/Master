from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
# MVC = Modelo vista controlador == Acciones (metodos)
# MVT = Modelo template vista == Acciones (metodos)


layout = ""

def index(request):
    html =""
    year = 2021
    while year <= 2050:
        if year % 2 ==0:
            html += f"<li>{str(year)}</li>"
        year +=1
        
    html += "</ul>"

    return render(request,'index.html')

def hola_mundo(request):
    return render(request,'hola-mundo.html')

def pagina(request,redirigir=0):

    if redirigir == 1:
        return redirect('contacto',nombre='Juan',apellido='Riquelme')

    return render(request,'pagina.html')

#ejemplo utilizando httpresponse
def contacto(request,nombre="",apellido=""):
    html= ""

    if nombre and apellido:
        html += "<p>El nombre es:</p>"
        html += f"<h3>{nombre} {apellido}</h3>"

    return HttpResponse(layout+f"<h2>Contacto</h2>"+html)