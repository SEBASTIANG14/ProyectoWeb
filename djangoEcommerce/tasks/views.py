from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.db import IntegrityError
from tasks.models import Carrito, CarritoProductos
from tasks.models import Producto
from . forms import ProductForm

# Create your views here.


def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'GET':
        return render(request, 'registro.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['contraseña'] == request.POST['contraseña2']:
            try:
                user = User.objects.create_user(
                    first_name=request.POST['nombre'],
                    last_name=request.POST['apellido'],
                    username=request.POST['correo'],
                    email=request.POST['correo'],
                    password=request.POST['contraseña'],
                    )
                user.save()
                login(request, user)
                return redirect('inicio')
            except IntegrityError:
                return render(request, 'registro.html', {
                    'form': UserCreationForm,
                    "error": 'El usuario ya existe'
                })

        return render(request, 'formulario.html', {
            'form': UserCreationForm,
            "error": 'Las contraseñas no coinciden'
        })


def inicio(request):
    if request.method == "GET":
        products = Producto.objects.all()
        return render(request, "inicio.html", {
            'products': products,
            'iterator': 5
        }) 
    else:
        post_info = request.POST
        nombre = post_info['Nombre']
        categoria = post_info['Categoria']
        precio = post_info['Precio']
        Id = post_info['id']
        obtCarrito = getCarrito(request.user)
        producto = Producto.objects.filter(id = Id).first()
        allCarrito = CarritoProductos(id_producto=producto, precio = precio, id_carrito = obtCarrito)
        allCarrito.save()
        products = Producto.objects.all()
        return render(request, 'Carrito.html', {'nombre': nombre, 'categoria': categoria, 'precio': precio}) 
    



#def formulario(request):
 #   print(request.POST)
  #  if request.method == 'POST':
   ##    if form.is_valid():
     #       form.save()
    #else:
     #   form = usuarioForm()
    #return render(request, 'registro.html', {'form': form})



def signin(request):
    if request.method == 'GET':
        return render(request, 'inicioSesion.html')
    else:
        correo = request.POST['Correo']
        contraseña = request.POST['Contraseña']
        print(correo, contraseña)
        # Autenticar usando el campo de correo en lugar de nombre de usuario
        user = authenticate(username=correo, password=contraseña)
        if user is None:
            return render(request, 'inicioSesion.html',{
                'error': 'El correo o la contraseña son incorrectos'
            })
        else:
            login(request, user)
            return redirect('inicio')
        

        return render(request, 'inicioSesion.html')
    

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("tasks:inicio")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("tasks:inicio")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("tasks:inicio")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("tasks:inicio")

def getCarrito(id_usuario):
    carrito = Carrito.objects.filter(id_usuario=id_usuario).first()
    if carrito is None:
        newCarrito = Carrito(id_usuario = id_usuario)
        newCarrito.save()
        return newCarrito
    if carrito.isOpen == True:
        return carrito
    else:
        newCarrito = Carrito(id_usuario = id_usuario)
        newCarrito.save()
        return newCarrito 
    

def carrito(request):
    return render(request, "") 
    
def busqueda(request):
    
    return render(request, "Busqueda.html")

def create_products(request):
    if request.method == 'GET':
        return render (request, 'create_product.html', {
            'form': ProductForm
        })
    else:
        form = ProductForm(request.POST)
        if form.is_valid():
            new_prod = form.save(commit=False)
            new_prod.user = request.user
            new_prod.save()
            return render(request, 'create_product.html',{
                'form': ProductForm
            })
        
