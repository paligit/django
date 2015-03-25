from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

# Create your models here.

class Usuario(User):
	apodo = models.CharField(max_length=60)

class Articulo(models.Model):
	titulo = models.CharField(max_length=60)
	url_img = models.ImageField(upload_to="Articulo")
	fecha = models.DateTimeField(auto_now_add=True)
	stock = models.IntegerField()
	usario = models.ManyToManyField(Usuario,through='Compra')
    
class Carateristica(models.Model):
	articulo = models.ForeignKey("Articulo")
	carateristica = models.CharField(max_length=80)

class Compra(models.Model):
	  user = models.ForeignKey(Usuario)
	  articulo = models.ForeignKey(Articulo)
	  fecha = models.DateTimeField()

     
class ArticuloForm(ModelForm):
	class Meta:
		model = Articulo
		#exclude = ('fecha')


class ArticuloForm(ModelForm):
	class Meta:
		model = Carateristica
		#fields = ('carateristica')



	


 	






