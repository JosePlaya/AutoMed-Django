import json
import requests
from django.http import Http404
from django.core import serializers
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import PostNewMedicamentoForm
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
    
def index(request, userType, idCentroMedico):
    return render(request, 'web/index.html')

def medicamentos(request, idCentroMedico):
    medicamentos = getMedicamentosByCentroMedico(request, idCentroMedico)
    return render(request, 'web/medicamentos.html', {'medicamentos' : medicamentos})

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
   
# ------------------------------------------------- #
#                      USUARIOS                     #
# ------------------------------------------------- #
# NUEVO USUARIO
def postNewUser(request):
    print('Iniciando post new user...')
    print(request)
    url = urlAPI+"usuario"
    payload = json.dumps(request)
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    return

# OBTENER USUARIOS POR TIPO
def getUserByType(request, type):
    url = urlAPI+"usuarios/"+type
    payload={}
    headers = {
      'Content-Type': 'application/json'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)

# OBTENER INFORMACIÓN DE UN USUARIO
def getUser(request, id):
    print('Iniciando get usuario...')
    url = urlAPI+"usuario/"+id
    payload={}
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    rJSON = response.json()
    tipoUsuario = rJSON['tipoUsuario']
    idCentroMedico = rJSON['idCentroMedico']
    return HttpResponse(tipoUsuario+'/'+idCentroMedico)

# OBTENER INFORMACIÓN DE UN USUARIO
def getUser_idCentroAtencion(request, id):
    print('Iniciando get di centro atención del usuario...')
    url = urlAPI+"usuario/"+id
    payload={}
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    r = response.json()
    return HttpResponse(r['idCentroMedico'])


# ------------------------------------------------- #
#                     CENTORS                       #
# ------------------------------------------------- #
# CREAR NUEVO CENTRO

# OBTENER LISTADO DE TODOS LOS CENTROS
def getCentros():
    print('Iniciando get centros...')
    extencion = "centros/"
    finalURL = urlAPI+extencion
    payload={}
    headers = {}
    response = requests.request("GET", finalURL, headers=headers, data=payload)
    print(response.text)
    return

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
def postNewMedicamento(request):
    print('Iniciando post new medicamento...')
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PostNewMedicamentoForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            data = {
                "stock": form.cleaned_data['stock'],
                "nombre": form.cleaned_data['nombre'],
                "codigo": form.cleaned_data['codigo'],
                "gramaje": form.cleaned_data['gramaje'],
                "cantidad": form.cleaned_data['cantidad'],
                "contenido": form.cleaned_data['contenido'],
                "fabricante": form.cleaned_data['fabricante'],
                "descripcion": form.cleaned_data['descripcion'],
                "idCentroMedico": form.cleaned_data['idCentroMedico']
            }
            url = urlAPI+"medicamento/" 
            payload = json.dumps(data)
            headers = {
                'Content-Type': 'application/json'
            }
            response = requests.request("POST", url, headers=headers, data=payload)
            if response.ok:
                print('OK')
                medicamentos = getMedicamentos()
                return render(request, 'web/medicamentos.html', {'medicamentos' : medicamentos})
            else:
                print('NO OK')
                print(response)
                try:
                    print(response.raise_for_status())
                except requests.exceptions.HTTPError as e:
                    print(e)
                return HttpResponse('<H1>Error en el formulario</H1>')
        else:
            print('No es valido')
            return HttpResponse('<H1>Error en el formulario</H1>')
    else:
        return HttpResponse('<H1>Error en el formulario</H1>')

# OBTENER TODOS LOS MEDICAMENTOS
def getMedicamentos():
    print('Iniciando get medicamentos (todos)...')
    url = urlAPI+"medicamentos/"
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.json())
    return response.json()

# OBTENER TODOS LOS MEDICAMENTOS DE UN CENTRO
def getMedicamentosByCentroMedico(request, idCentroMedico):
    print('Iniciando get medicamentos by centro medico...')
    url = urlAPI+"medicamentos/"+idCentroMedico
    payload={}
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.json())
    return response.json()

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

