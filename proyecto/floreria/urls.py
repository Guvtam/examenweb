from django.urls import URLPattern, path 
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static 
from django.contrib.auth.views import  LoginView, LogoutView


urlpatterns=[
    path('',views.inicio, name='inicio'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('registro/',views.registro,name='registro'),
    path('tienda/',views.tienda,name='tienda'),
    path('registro/crear/',views.crear_producto,name='crear_producto'),
    path('registro/editar/<int:id>',views.editar_producto,name='editar_producto'),
    path('registro/eliminar/<int:id>',views.eliminar_producto,name='eliminar_producto'),
    path('registrar/usuario',views.registro_usuario,name='registro_usuario'),
    path('login/',LoginView.as_view(template_name='usuario/login.html'),name='login'),
    path('logout/',LogoutView.as_view(template_name='usuario/logout.html'),name='logout'),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)