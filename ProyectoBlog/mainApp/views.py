from django.shortcuts import render

# Create your views here.

def index(request):

    return render(request,'mainapp/index.html',{
        'title':'Inicio'
    })

def about(request):

    return render(request,'mainapp/index.html',{
        'title':'Acerca de nosotros'
    })