from django.db import models
from ckeditor.fields import RichTextField # INSTALO PAQUETE Y LO IMPORTO

# Create your models here.

class Page(models.Model):
    title = models.CharField(max_length=50,verbose_name='Titulo')
    content = RichTextField(verbose_name="Contenido")
    slug = models.CharField(unique=True,max_length=50,verbose_name='URL')
    order = models.IntegerField(default=0,verbose_name="Orden")
    visible = models.BooleanField(verbose_name="¿Visible?")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="Creado el")
    updated_at = models.DateTimeField(auto_now_add=True,verbose_name="Actualizado el")


    class Meta:
        verbose_name= 'Pagina'
        verbose_name_plural = 'Paginas'

    def __str__(self):
        return self.title
    
#Las migraciones se realizan cuando se hace un cambio en este archivo que 
#modifique o interactue con la BBDD