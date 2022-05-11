import requests
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
#from pyrebase import pyrebase


# VARIABLES
urlAPI = "https://us-central1-automed-cl.cloudfunctions.net/webApi/"


# ---------------------------------------------------------------- #
# -----------------------------VISTAS----------------------------- #
# ---------------------------------------------------------------- #

def test(request):
    return render(request, 'web/test.html')

def login(request):
    return render(request, 'web/login.html')

def medico(request):
    return render(request, 'web/medico.html')

def farmaceutico(request):
    return render(request, 'web/farmaceutico.html')

def administrador(request):
    return render(request, 'web/administrador.html')
    
def index(request):
    return render(request, 'web/index.html')

def medicamentos(request):
    return render(request, 'web/medicamentos.html')

def medicamentos_add(request):
    return render(request, 'web/medicamentos_add.html')

def articulos(request):
    return render(request, 'web/articulos.html')

def articulos_add(request):
    return render(request, 'web/articulos_add.html')

def centros_medicos(request):
    return render(request, 'web/centros_medicos.html')

def centros_medicos_add(request):
    return render(request, 'web/centros_medicos_add.html')

def farmaceuticos(request):
    return render(request, 'web/farmaceuticos.html')

def articulos_add(request):
    return render(request, 'web/articulos_add.html')

def farmaceuticos_add(request):
    return render(request, 'web/farmaceuticos_add.html')

def medicos(request):
    return render(request, 'web/medicos.html')

def medicos_add(request):
    return render(request, 'web/medicos_add.html')

def pacientes(request):
    return render(request, 'web/pacientes.html')

def pacientes_add(request):
    return render(request, 'web/pacientes_add.html')

def prescripciones(request):
    return render(request, 'web/prescripciones.html')

def prescripciones_add(request):
    return render(request, 'web/prescripciones_add.html')


# ---------------------------------------------------------------- #
# --------------------FUNCIONES CONECCIÓN API--------------------- #
# ---------------------------------------------------------------- #

# OBTENER LISTADO DE TODOS LOS CENTROS
def getCentros():
    print('Iniciando get centros...')
    extencion = "centros/"
    finalURL = urlAPI+extencion
    payload={}
    headers = {}
    response = requests.request("GET", finalURL, headers=headers, data=payload)
    print(response.text)
    
# ------------------------------------------------- #
#                      USUARIOS                     #
# ------------------------------------------------- #
# NEW USUARIO

# OBTENER USUARIOS POR TIPO

# OBTENER INFORMACIÓN DE UN USUARIO
def getUser(request, id):
    print('Iniciando get usuario...')
    url = urlAPI+"usuario/"+id
    payload={}
    headers = {
    'Content-Type': 'application/json'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    r = response.json()
    return HttpResponse(r['tipoUsuario'])


# ------------------------------------------------- #
#                     CENTORS                       #
# ------------------------------------------------- #
# CREAR NUEVO CENTRO

# OBTENER TODOS LOS CENTRO

# OBTENER UN CENTRO



# ------------------------------------------------- \\
#                     PACIENTES                     \\
# ------------------------------------------------- \\
# CREAR NUEVO PACIENTE

# OBTENER TODOS LOS PACIENTES

# OBTENER UN PACIENTE POR ID

# OBTENER UN PACIENTE POR RUT

# ACTUALIZAR UN PACIENTE

# ELIMINAR PACIENTE 



# ------------------------------------------------- \\
#                    MEDICAMENTOS                   \\
# ------------------------------------------------- \\
# CREAR NUEVO MEDICAMENTOS

# OBTENER TODOS LOS MEDICAMENTOS
def get_medicamentos():
    print('Iniciando get medicamentos...')
    url = "https://us-central1-automed-cl.cloudfunctions.net/webApi/medicamentos/"
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.json())

# OBTENER TODOS LOS MEDICAMENTOS DE UN CENTRO

# OBTENER UN MEDICAMENTO POR ID

# OBTENER UN MEDICAMENTO POR SU CÓDIGO

# ACTUALIZAR UN MEDICAMENTO

# ELIMINAR MEDICAMENTO 

# OBTENER STOCK DE UN MEDICAMENTO POR ID

# OBTENER STOCK DE UN MEDICAMENTO POR SU CÓDIGO

# ACTUALIZAR STOCK DE UN MEDICAMENTO POR ID



# ------------------------------------------------- \\
#                    PREESCRIPCIÓN                  \\
# ------------------------------------------------- \\
# OBTENER TODOS LOS MEDICAMENTOS

# OBTENER UNA PREESCRIPCION

# CREAR NUEVO MEDICAMENTOS

# ACTUALIZAR UN MEDICAMENTO

# ELIMINAR MEDICAMENTO 

