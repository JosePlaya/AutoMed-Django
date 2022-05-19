from . import views as main_views
from django.urls import path
from .views import login, index, medicamentos_edit, perfil,test, user_add
from .views import medico,farmaceutico,administrador
from .views import medicamentos, medicamentos_add
from .views import articulos, articulos_add
from .views import centros_medicos, centros_medicos_add
from .views import farmaceuticos, administradores
from .views import medicos
from .views import pacientes, pacientes_add
from .views import prescripciones, prescripciones_add, postNewPrescripcionDatos, prescripciones_add_medicamentos


urlpatterns = [
    # ----------------------------------------------------------------- #
    # ---------------------------- VISTAS ----------------------------- #
    # ----------------------------------------------------------------- #
    # LOGIN
    path('',login, name="login"),
    path('login/',login, name="login"),
    
    # INDEX
    path('<str:userType>/index/<str:uid>/',index, name="index"),
    
    # MEDICO
    path('/<str:userType>/medico/',medico, name="medico"),
    # FARMACEUTICO
    path('<str:userType>/farmaceutico/',farmaceutico, name="farmaceutico"),
    # ADMIN
    path('<str:userType>/administrador/',administrador, name="administrador"),
    
    # MEDICAMENTOS
    path('<str:userType>/medicamentos/<str:idCentroMedico>', medicamentos, name="medicamentos"),
    path('<str:userType>/medicamentos_add/',medicamentos_add, name="medicamentos_add"),
    path('<str:userType>/medicamentos_edit/<str:idMedicamento>',medicamentos_edit, name="medicamentos_edit"),
    # CENTROS MEDICOS
    path('<str:userType>/centros_medicos/',centros_medicos, name="centros_medicos"),
    path('<str:userType>/centros_medicos_add/',centros_medicos_add, name="centros_medicos_add"),
    path('<str:userType>/centros_medicos_edit/<str:idCentroMedico>',medicamentos_edit, name="centros_medicos_edit"),
    # 
    path('articulos/',articulos, name="articulos"),
    path('articulos_add/',articulos_add, name="articulos_add"),
    # ADMINISTRADORES
    path('<str:userType>/administradores/',administradores, name="administradores"),
    # FARMACEUTICOS
    path('<str:userType>/farmaceuticos/',farmaceuticos, name="farmaceuticos"),
    path('<str:userType>/farmaceuticos_edit/<str:idUsuario>',medicamentos_edit, name="farmaceuticos_edit"),
    # MEDICOS
    path('<str:userType>/medicos/',medicos, name="medicos"),
    path('<str:userType>/medicos_edit/<str:idUsuario>',medicamentos_edit, name="medicos_edit"),
    # PERFIL
    path('<str:userType>/perfil/<str:uid>',perfil, name="perfil"),
    # PACIENTES
    path('<str:userType>/pacientes/',pacientes, name="pacientes"),
    path('<str:userType>/pacientes_add/',pacientes_add, name="pacientes_add"),
    # PRESCRIPCIONES
    path('<str:userType>/prescripciones/',prescripciones, name="prescripciones"),
    path('<str:userType>/prescripciones_add/',prescripciones_add, name="prescripciones_add"),
    path('<str:userType>/prescripciones_add_medicamentos/<str:idPost>/',prescripciones_add_medicamentos, name="prescripciones_add_medicamentos"),
    #
    path('<str:userType>/user_add/<str:newUserType>/<str:idCentroMedico>/', user_add, name="user_add"),
    #
    path('test/',test, name="test"),
    
    # ----------------------------------------------------------------- #
    # ---------------------------- MÉTODOS ---------------------------- #
    # ----------------------------------------------------------------- #
    # CENTROS
    path('getCentros/', main_views.getCentrosMedicos, name="getCentros"),
    path('deleteCentroMedico/<str:idCentroMedico>', main_views.deleteCentroMedico, name="deleteCentroMedico"),
    
    # USUARIOS
    path('postNewUser/', main_views.postNewUser, name="postNewUser"),
    path('getUserByType/<str:type>', main_views.getUserByType, name="getUserByType"),
    path('getUser/<str:id>', main_views.getUser, name="getUser"),
    path('getUser_idCentroAtencion/<str:id>', main_views.getUser_idCentroAtencion, name="getUser_idCentroAtencion"),
    path('getUser_idCentroAtencionYRut/<str:id>', main_views.getUser_idCentroAtencionYRut, name="getUser_idCentroAtencionYRut"),
    path('deleteUsuario/<str:idUsuario>', main_views.deleteUsuario, name="deleteUsuario"),
    
    # MEDICAMENTOS
    path('postNewMedicamento/', main_views.postNewMedicamento, name="postNewMedicamento"),
    path('postUpdateMedicamento/', main_views.postUpdateMedicamento, name="postUpdateMedicamento"),
    path('getMedicamentos/', main_views.getMedicamentos, name="getMedicamentos"),
    path('getMedicamentosByCentroMedico/<str:idCentroMedico>', main_views.getMedicamentosByCentroMedico, name="getMedicamentosByCentroMedico"),
    path('deleteMedicamento/<str:idMedicamento>', main_views.deleteMedicamento, name="deleteMedicamento"),
    
    # PACIENTES
    path('postNewPaciente/', main_views.postNewPaciente, name="postNewPaciente"),
    
    # PRESCRIPCIÓN
    path('postNewPrescripcionDatos/', main_views.postNewPrescripcionDatos, name="postNewPrescripcionDatos"),
]

# EAAKf5vBfUe0BANBju2n6AS0QUjSph0Ik8iTOvCrPWS9AMS08B3jMlZCfMX99dO881ieyIBoxgGyZCrIZAHc27lgvILK4nIi6PJUjmaZBPj5ZC5VZBSEufzG74ZANfXB5K3TNhQ7K7pGHrCyzvIeTzk0hNMdnIO9ZCOG1uuAk65xxxXsJZBrQZAwL2lOEkbap6C0wQmZAHTwQ6AoZCwZDZD
# EAAKf5vBfUe0BAPmbfhYcElYR4Bf0QMeC5FvbcE9QbNSyaURTepbbF5f7N2OZBPSP4T5Y74pu8wFudkJERkAkFiaZCVovFCyqZBMTqp3jFMkiQrjps8IVJPRdoaKxy4uXttdK5zK1msZAgiLH5uWnLhQJGZCWYgS8uxFMgo2IoNeXjy2McjVmKZBBuKlQvpvvneIbxhdEOC6AZDZD

# curl -i -X POST \
# >   https://graph.facebook.com/v12.0/103925202324943/messages \
# >   -H 'Authorization: Bearer 67b2d2f9709c36b64777f07a7e243fbe' \
# >   -H 'Content-Type: application/json' \
# >   -d '{ "messaging_product": "whatsapp", "to": "56976423354", "type": "template", "template": { "name": "hello_world", "language": { "code": "en_US" } } }'


# curl -i -X GET 
#   "https://graph.facebook.com/v13.0/110967794946398/businesses?access_token=EAAKf5vBfUe0BAPmbfhYcElYR4Bf0QMeC5FvbcE9QbNSyaURTepbbF5f7N2OZBPSP4T5Y74pu8wFudkJERkAkFiaZCVovFCyqZBMTqp3jFMkiQrjps8IVJPRdoaKxy4uXttdK5zK1msZAgiLH5uWnLhQJGZCWYgS8uxFMgo2IoNeXjy2McjVmKZBBuKlQvpvvneIbxhdEOC6AZDZD"
