from django.urls import path
from .views import articulos_farmacia, home_farmacia, login
from .views import medico, pacientes_farmacia
from .views import farmaceutico, prescripciones_farmacia
from .views import administrador, perfil
from .views import medicamentos_farmacia




urlpatterns = [
    path('',login, name="login"),
    path('medico/',medico, name="medico"),
    path('farmaceutico/',farmaceutico, name="farmaceutico"),
    path('administrador/',administrador, name="administrador"),
    path('articulos_farmacia/',articulos_farmacia, name="articulos_farmacia"),
    path('home_farmacia/',home_farmacia, name="home_farmacia"),
    path('medicamentos_farmacia/',medicamentos_farmacia, name="medicamentos_farmacia"),
    path('pacientes_farmacia/',pacientes_farmacia, name="pacientes_farmacia"),
    path('prescripciones_farmacia/',prescripciones_farmacia, name="prescripciones_farmacia"),
    path('perfil/',perfil, name="perfil"),
]