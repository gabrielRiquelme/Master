from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
# MVC = Modelo vista controlador == Acciones (metodos)
# MVT = Modelo template vista == Acciones (metodos)


layout = ""

def index(request):
    """
    html =""

    year = 2021
    while year <= 2050:
        if year % 2 ==0:
            html += f"<li>{str(year)}</li>"
        year +=1
        
    html += "</ul>"
    """
    year = 2021
    hasta = range(year,2051)
    nombre = 'Juan Riquelme'
    lenguajes = ['Javascript','python','php','c']

    return render(request,'index.html',{
        'title':'Inicio',
        'mi_variable':'Soy un dato de la vista',
        'nombre':nombre,
        'lenguajes':lenguajes,
        'years':hasta,

    })

def hola_mundo(request):
    return render(request,'hola-mundo.html')

def pagina(request,redirigir=0):

    if redirigir == 1:
        return redirect('contacto',nombre='Juan',apellido='Riquelme')

    return render(request,'pagina.html',{
        'texto':'',
        'lista':[1,2,3]
    })

#ejemplo utilizando httpresponse
def contacto(request,nombre="",apellido=""):
    html= ""

    if nombre and apellido:
        html += "<p>El nombre es:</p>"
        html += f"<h3>{nombre} {apellido}</h3>"

    return HttpResponse(layout+f"<h2>Contacto</h2>"+html)