
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls.static import static
from django.urls import include, path

if settings.DEBUG:
    import debug_toolbar

urlpatterns = [
    path('', views.home, name='home'),
    path('convocatoria/', views.convocatoria, name='convocatoria'),
    path('registro/', views.registro, name='registro'),
    path('pedido/', views.pedido, name='pedido'),
    path('editar_pedido/<int:id>/', views.editar_pedido, name='editar_pedido'),
    path('eliminar_pedido/<int:id>/', views.eliminar_pedido, name='eliminar_pedido'),
    path('mostrar_pedido/', views.mostrar_pedido, name='mostrar_pedido'),
    path('entrega/', views.entrega, name='entrega'),
    path('asistencia/<int:id>/', views.asistencia, name='asistencia'),    
    path('perfil/', views.perfil, name='perfil'),
    path('configuracion/', views.configuracion, name='configuracion'),
    path('accounts/login/', views.login, name='login'),   
    path('estudiantes_registrados/', views.estudiantes_registrados, name='estudiantes_registrados'), 
    path('beneficiario/', views.beneficiario, name='beneficiario'),
    path('falla/', views.fallas, name='fallas'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('change-password/', auth_views.PasswordChangeView.as_view()),
    path('__debug__/', include(debug_toolbar.urls)),
    # path('refrigerio/', views.refrigerio, name='refrigerio'),
    # path('almuerzo/', views.almuerzo, name='almuerzo')



    path('proveedor/', views.proveedor, name='proveedor'),
    path('proveedor_create/', views.proveedor_create, name='proveedor_create'),
    #path('proveedor_edit/', views.proveedor_edit, name='proveedor_edit'),
    path('proveedor_edit/<int:id>/', views.proveedor_edit, name='proveedor_edit'),
    path('proveedor_delete/<int:id>/', views.proveedor_delete, name='proveedor_delete'),





]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)