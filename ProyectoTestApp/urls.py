from django.urls import path

from ProyectoTestApp import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('tienda', views.tienda, name="Tienda"),        #BORRAR
    path('blog', views.blog, name="Blog"),              #BORRAR
    path('contacto', views.contacto, name="Contacto")   #BORRAR

]

