from . import views as main_views
from django.urls import path
from .views import login, index,test
from .views import medico,farmaceutico,administrador
from .views import medicamentos, medicamentos_add
from .views import articulos, articulos_add
from .views import centros_medicos, centros_medicos_add
from .views import farmaceuticos, farmaceuticos_add
from .views import medicos, medicos_add


urlpatterns = [
    # ----------------------------------------------------------------- #
    # ---------------------------- VISTAS ----------------------------- #
    # ----------------------------------------------------------------- #
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
    
    # ----------------------------------------------------------------- #
    # ---------------------------- MÉTODOS ---------------------------- #
    # ----------------------------------------------------------------- #
    # CENTROS
    path('getCentros/', main_views.getCentros, name="getCentros"),
    
    # USUARIOS
    path('postNewUser/', main_views.postNewUser, name="postNewUser"),
    path('getUserByType/<str:type>', main_views.getUserByType, name="getUserByType"),
    path('getUser/<str:id>', main_views.getUser, name="getUser"),
    path('getUser_idCentroAtencion/<str:id>', main_views.getUser_idCentroAtencion, name="getUser_idCentroAtencion"),
    
    # MEDICAMENTOS
    path('postNewMedicamento/', main_views.postNewMedicamento, name="postNewMedicamento"),
    path('getMedicamentos/', main_views.getMedicamentos, name="getMedicamentos"),
    path('getMedicamentosByCentroMedico/<str:idCentroMedico>', main_views.getMedicamentosByCentroMedico, name="getMedicamentosByCentroMedico"),
]
