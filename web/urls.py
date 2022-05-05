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
]