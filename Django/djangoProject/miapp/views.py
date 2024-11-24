from django.shortcuts import render,HttpResponse,redirect
from miapp.models import Article, Category
from django.db.models import Q
from miapp.forms import Form_article
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

def crear_articulo(request,title,content, public):
    articulo=Article(
        title= title,
        content= content,
        public= public
    )

    articulo.save()
    return HttpResponse(f'Articulo creado:{articulo.title}-{articulo.content}')
    
def mostrar_articulo(request):

    try:
        articulo = Article.objects.get(title='manzana')
        response = f'Articulo:{articulo.id} - {articulo.title}'
    except:
        response= "<h3>Articulo no encontrado en BBDD</h3>"

    return HttpResponse(response)

def create_full_article(request):
    formulario = Form_article()

    return render(request,'create_full_article.html',{
        'form':formulario
    })


def editar_articulo(request,id):

    articulo = Article.objects.get(pk=id)

    articulo.title = 'Batman'
    articulo.content = 'Pelicula del 2017'
    articulo.public = True

    articulo.save()

    return HttpResponse(f'Articulo actualizado:{articulo.title}-{articulo.content}')


def articulos(request):
    # Puedo usar ORDER BY como en SQL, ejemplo:
    # articulos = Article.objetcs.order_by('title')
    # Tambien puedo limitar elementos.
    #articulos = Article.objetcs.order_by('title')[:3]
    articulos = Article.objects.all().order_by('-id')
    """
    #condiciones locaps: Contains / exact / iexact funcionan similar a %like% en SQL.
    articulos = Article.objects.filter(title__contains='articulo')

    #Exclude lo que esta dentro de .exclude(campo = valor)
    articulos = Article.objects.filter(title='manzana').exclude(content='verde')

    #Consultas SQL CRUDA Y PURA

    articulos = Article.objects.raw("SELECT * FROM miapp_article WHERE title='manzana'")

    #USANDO EL ORM

    articulos = Article.objects.filter(Q(title__contains = 'manzana') | Q(title__contains='agua'))
"""
    return render(request,'articulos.html',{
        'articulos':articulos
    })

def save_article(request):

    if request.method == 'POST':

        title = request.POST['title']
        content = request.POST['content']
        public = request.POST['public']

        articulo=Article(
            title = title,
            content = content,
            public = public
        )

        articulo.save()
        return HttpResponse(f'Articulo creado:{articulo.title}-{articulo.content}')
    else:
        return HttpResponse("No se a podido crear el articulo")



def create_article(request):
    return render(request,'createArticle.html')

def borrar_articulo(request,id):
    articulo = Article.objects.get(pk=id)
    articulo.delete()

    return redirect('articulos')