from . import views as main_views
from django.urls import path
from .views import login
from .views import medico
from .views import farmaceutico
from .views import administrador
from .views import test

urlpatterns = [
    path('',login, name="login"),
    path('test/',test, name="test"),
    path('medico/',medico, name="medico"),
    path('farmaceutico/',farmaceutico, name="farmaceutico"),
    path('administrador/',administrador, name="administrador"),
    path('getCentros/', main_views.getCentros, name="getCentros"),
    path('signup/', main_views.signup, name="signup")
]
