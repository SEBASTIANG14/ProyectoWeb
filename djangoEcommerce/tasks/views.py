from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.db import IntegrityError
from . forms import usuarioForm

# Create your views here.


def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('inicio')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    "error": 'El usuario ya existe'
                })

        return render(request, 'signup.html', {
            'form': UserCreationForm,
            "error": 'Las contraseñas no coinciden'
        })


def inicio(request):
    return render(request, 'inicio.html')



def formulario(request):
    print(request.POST)
    if request.method == 'POST':
        form = usuarioForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = usuarioForm()
    return render(request, 'registro.html', {'form': form})



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
    
def carrito(request):
    return render(request, "") 
    
