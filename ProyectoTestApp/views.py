from django.shortcuts import render, HttpResponse


# Create your views here.

def home(request): 
    
    return render(request, "ProyectoTestApp/home.html")

def tienda(request):    #BORRAR

    return render(request, "ProyectoTestApp/tienda.html")

def blog(request):      #BORRAR

    return render(request, "ProyectoTestApp/blog.html")

def contacto(request):  #BORRAR

    return render(request, "ProyectoTestApp/contacto.html")