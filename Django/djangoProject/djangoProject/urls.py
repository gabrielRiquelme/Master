"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

#Importar miapp con mis vistas
from miapp import views
#import miapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('inicio/', views.index,name='inicio'),
    path('hola-mundo/', views.hola_mundo,name='hola_mundo'),
    path('pag-pruebas/', views.pagina,name='pag_pruebas'),
    path('pag-pruebas/<int:redirigir>', views.pagina,name='pag_pruebas'),
    path('contacto/', views.contacto,name='contacto'),
    path('contacto/<str:nombre>', views.contacto,name='contacto'),
    path('contacto/<str:nombre>/<str:apellido>', views.contacto,name='contacto'),
    path('crear_articulo/<str:title>/<str:content>/<str:public>',views.crear_articulo,name='crear_articulo'),
    path('mostrar_articulo/',views.mostrar_articulo,name='mostrar_articulo'),
    path('editar_articulo/<int:id>',views.editar_articulo),
    path('articulos/', views.articulos,name='articulos'),
    path('borrar_articulo/<int:id>', views.borrar_articulo,name='borrar_articulo'),
    path('save_article/', views.save_article,name='save_article'),
    path('create_article/', views.create_article,name='create_article'),
    path('create_full_article/', views.create_full_article,name='create_full_article')
]
