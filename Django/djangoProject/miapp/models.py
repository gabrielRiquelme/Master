from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    content= models.TextField()
    image= models.ImageField(default='null',verbose_name='Miniatura',upload_to='articles/')
    public= models.BooleanField()
    create_at=models.DateTimeField(auto_now_add=True)
    update_at= models.DateTimeField(auto_now_add=True)

class Category(models.Model):
    name = models.CharField(max_length=110)
    description = models.CharField(max_length=250)
    create_at = models.DateField( )
    