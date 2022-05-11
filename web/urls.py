from . import views as main_views
from django.urls import path
from .views import login, index,test
from .views import medico,farmaceutico,administrador
from .views import medicamentos, medicamentos_add
from .views import articulos, articulos_add
from .views import centros_medicos, centros_medicos_add
from .views import farmaceuticos, farmaceuticos_add
from .views import medicos, medicos_add
from .views import pacientes, pacientes_add
from .views import prescripciones, prescripciones_add


urlpatterns = [
    # VISTAS
    path('',login, name="login"),
    path('login/',login, name="login"),
    path('index/',index, name="index"),
    path('test/',test, name="test"),
    path('medico/',medico, name="medico"),
    path('farmaceutico/',farmaceutico, name="farmaceutico"),
    path('administrador/',administrador, name="administrador"),
    path('medicamentos/',medicamentos, name="medicamentos"),
    path('medicamentos_add/',medicamentos_add, name="medicamentos_add"),
    path('articulos/',articulos, name="articulos"),
    path('articulos_add/',articulos_add, name="articulos_add"),
    path('centros_medicos/',centros_medicos, name="centros_medicos"),
    path('centros_medicos_add/',centros_medicos_add, name="centros_medicos_add"),
    path('farmaceuticos/',farmaceuticos, name="farmaceuticos"),
    path('farmaceuticos_add/',farmaceuticos_add, name="farmaceuticos_add"),
    path('medicos/',medicos, name="medicos"),
    path('medicos_add/',medicos_add, name="medicos_add"),
    path('pacientes/',pacientes, name="pacientes"),
    path('pacientes_add/',pacientes_add, name="pacientes_add"),
    path('prescripciones/',prescripciones, name="prescripciones"),
    path('prescripciones_add/',prescripciones_add, name="prescripciones_add"),
    
    # MÉTODOS
    path('getCentros/', main_views.getCentros, name="getCentros"),
    path('getUser/<str:id>', main_views.getUser, name="getUser"),
    path('get_medicamentos/', main_views.get_medicamentos, name="get_medicamentos"),
]
