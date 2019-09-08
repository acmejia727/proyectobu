
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
    path('', views.home, name='home'),
    path('convocatoria/', views.convocatoria, name='convocatoria'),
    path('registro/', views.registro, name='registro'),
    path('entrega/', views.entrega, name='entrega'),
    path('perfil/', views.perfil, name='perfil'),
    path('configuracion/', views.configuracion, name='configuracion'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('change-password/', auth_views.PasswordChangeView.as_view()),
 
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)