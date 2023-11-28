from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .models import Usuario
from .forms import *

# Create your views here.

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html',{
        'form' : UserCreationForm()
    })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('listar_usuario')
            except IntegrityError:
                return render(request, 'signup.html',{
                    'form' : UserCreationForm(),
                    'error':'usuario ya existe'
                })
        return render(request, 'signup.html',{
            'form' : UserCreationForm(),
            'error':'contraseña incorrecta'
        })
    
@login_required(login_url="signin")
def signout(request):
    logout(request)
    return  redirect('signin')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
            'form': AuthenticationForm,
            'error': 'USUARIO O CONTRASEÑA INCORRECTOS'
        })
        else:
            login(request, user)
            return redirect('listar_usuario')

@login_required(login_url="signin")
def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            # hacer algo despues que se ejecute
    else: 
        form = UsuarioForm()
    return render(request, 'dashboard/crear_usuario.html', {'form': form})

@login_required(login_url="signin")
def listar_usuario(request):
    datos = Usuario.objects.all()    
    data = {
        'consultas': datos
    }
    return render(request, 'dashboard/listar_usuario.html',data)