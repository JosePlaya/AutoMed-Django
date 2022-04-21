from django.urls import path
from .views import login
from .views import medico
from .views import farmaceutico
from .views import administrador




urlpatterns = [
    path('',login, name="login"),
    path('medico/',medico, name="medico"),
    path('farmaceutico/',farmaceutico, name="farmaceutico"),
    path('administrador/',administrador, name="administrador")
]