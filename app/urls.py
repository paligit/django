from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns(

	url (r'^$/','app.views.crear',name="crearArticulo"),
	#url (r'^ventas/$','app.views.crear',name='crear'),
	
    # Examples:
    # url(r'^$', 'ventas.views.home', name='home'),
    # url(r'^ventas/', include('ventas.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
