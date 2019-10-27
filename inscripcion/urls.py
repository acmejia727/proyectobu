
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls.static import static
from django.urls import include, path


urlpatterns = [
    path('perfilEstudiante/', views.perfilEstudiante, name='perfilEstudiante'),
    path('inscripcion/', views.inscripcion, name='inscripcion'),
 
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)