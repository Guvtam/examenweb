from pyexpat.errors import messages
from django.shortcuts import redirect, render
from .models import Producto
from .forms import UserRegisterForm,ProductoForm
from django.contrib import messages

# Create your views here.
def inicio(request):
    return render(request,'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def registro(request):
    productos = Producto.objects.all()
    return render(request,'productos/registro.html',{'productos': productos})

def tienda(request):
    productos = Producto.objects.all()
    return render(request,'paginas/tienda.html',{'productos' : productos})

def crear_producto(request):
    formulario = ProductoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('registro')
    return render(request,'productos/crear_producto.html',{'formulario' : formulario})

def editar_producto(request,id):
    producto = Producto.objects.get(id=id)
    formulario = ProductoForm(request.POST or None, request.FILES or None, instance=producto)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('registro')
    return render(request,'productos/editar_producto.html',{'formulario' : formulario})

def eliminar_producto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    return redirect('registro')

def registro_usuario(request):
    if request.method == 'POST':
        formulario = UserRegisterForm(request.POST)
        if formulario.is_valid():
            #username = formulario.cleaned_data['username']
            #messages.success(request, f'Usuario {username} creado')
            formulario.save()
            return redirect('nosotros')
    else:
        formulario = UserRegisterForm()
    return render(request,'usuario/registro_usuario.html',{'formulario' : formulario})


