from django.urls import path, include
from .views import *

urlpatterns = [
    path('',signin, name='signin'),
    path('signup/' ,signup, name="'signup"),
    path('signuot/',signout,name="logout"),
    path('listar_usuario/',listar_usuario,name="listar_usuario"),
    path('crear_usuario/',crear_usuario,name="crear_usuario"),
]