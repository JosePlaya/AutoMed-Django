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
    # ----------------------------------------------------------------- #
    # ---------------------------- VISTAS ----------------------------- #
    # ----------------------------------------------------------------- #
    path('',login, name="login"),
    path('login/',login, name="login"),
    path('index/<str:userType>/<str:idCentroMedico>',index, name="index"),
    path('test/',test, name="test"),
    path('medico/',medico, name="medico"),
    path('farmaceutico/',farmaceutico, name="farmaceutico"),
    path('administrador/',administrador, name="administrador"),
    path('medicamentos/<str:idCentroMedico>', medicamentos, name="medicamentos"),
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

# EAAKf5vBfUe0BANBju2n6AS0QUjSph0Ik8iTOvCrPWS9AMS08B3jMlZCfMX99dO881ieyIBoxgGyZCrIZAHc27lgvILK4nIi6PJUjmaZBPj5ZC5VZBSEufzG74ZANfXB5K3TNhQ7K7pGHrCyzvIeTzk0hNMdnIO9ZCOG1uuAk65xxxXsJZBrQZAwL2lOEkbap6C0wQmZAHTwQ6AoZCwZDZD
# EAAKf5vBfUe0BAPmbfhYcElYR4Bf0QMeC5FvbcE9QbNSyaURTepbbF5f7N2OZBPSP4T5Y74pu8wFudkJERkAkFiaZCVovFCyqZBMTqp3jFMkiQrjps8IVJPRdoaKxy4uXttdK5zK1msZAgiLH5uWnLhQJGZCWYgS8uxFMgo2IoNeXjy2McjVmKZBBuKlQvpvvneIbxhdEOC6AZDZD

# curl -i -X POST \
# >   https://graph.facebook.com/v12.0/103925202324943/messages \
# >   -H 'Authorization: Bearer 67b2d2f9709c36b64777f07a7e243fbe' \
# >   -H 'Content-Type: application/json' \
# >   -d '{ "messaging_product": "whatsapp", "to": "56976423354", "type": "template", "template": { "name": "hello_world", "language": { "code": "en_US" } } }'


# curl -i -X GET 
#   "https://graph.facebook.com/v13.0/110967794946398/businesses?access_token=EAAKf5vBfUe0BAPmbfhYcElYR4Bf0QMeC5FvbcE9QbNSyaURTepbbF5f7N2OZBPSP4T5Y74pu8wFudkJERkAkFiaZCVovFCyqZBMTqp3jFMkiQrjps8IVJPRdoaKxy4uXttdK5zK1msZAgiLH5uWnLhQJGZCWYgS8uxFMgo2IoNeXjy2McjVmKZBBuKlQvpvvneIbxhdEOC6AZDZD"
