# Create your views here.

from django.template import Context, loader
from app.models import Articulo,ArticuloForm
from django.http import HttpResponse

def home (request):
	articulos = Articulo.objects.all().orderby('-fecha')[:5]
	t= loader.get_template('app/template/home.html')
    c=Context({
        list_articulos:articulos,
    	})
    HttpResponse(t.render(c))

def crear(request):

	#a=ArticuloForm(request.Articulo)
	#form = ArticleForm(instance=a)
	#t=loader.get_template('/ventas/app/templates/form.html')
    #c=Context({
     #  formulario:'pepe',
    #	})
    #HttpResponse(t.render(c))

    return render_to_response('app/templates/form.html', {'formulario': 'pepe'},
                               context_instance=RequestContext(request))