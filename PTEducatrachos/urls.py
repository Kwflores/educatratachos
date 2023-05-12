from django.conf import settings
from django.urls import include, path
from django.contrib import admin
from home.views import dia_destacado, galeria_fd
from seguridad.seguridad.views import signin, signout
from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from administracion.views import *
from recursos.views import *

from search import views as search_views


urlpatterns = [
    path("django-admin/", admin.site.urls),
    path("admin/", include(wagtailadmin_urls)),
    path("documents/", include(wagtaildocs_urls)),
    path("search/", search_views.search, name="search"),
    path("galeria-de-noticias/",galeria_noticias,name='galeria'),
    path("galeria-de-fechas/",fecha_destacada,name='galeria'),
    #path('', dia_destacado, name='dia_destacado'),
    path("repositorio/<int:id_dirigido>/<int:id_nivel>/<int:id_clase>/<int:id_grado>/",repositorios,name='repositorio_recursos'),
    path("grados/<int:id>/<int:id_grado>/",grados_academicos,name='grados'),
    path('login/', signin, name='signin'),
    path('logout/', signout, name='signout'),
    path("repositorio_detalle/<int:id_repositorio>/",repositorio_detalle,name='repositorio_detalle'),
    path("repositorio-de-recursos/<int:id_dirigido>/", nivelacademico, name='nivelacademico'),


    
    
 
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = urlpatterns + [
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    path("", include(wagtail_urls)),
    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    path("pages/", include(wagtail_urls)),
]
