import json
import requests
from django.http import Http404
from django.core import serializers
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import PostNewMedicamentoForm, PostUpdateMedicamentoForm
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
    print('userType: '+userType)
    return render(request, 'web/index.html', {'userType' : userType})
#


# CENTROS MEDICOS
def centros_medicos(request):
    centrosMedicos = getCentrosMedicos()
    return render(request, 'web/centros_medicos.html', {'centrosMedicos' : centrosMedicos})

def centros_medicos_add(request):
    return render(request, 'web/centros_medicos_add.html')
#

#
# MEDICAMENTOS
def medicamentos(request, idCentroMedico):
    medicamentos = getMedicamentosByCentroMedico(request, idCentroMedico)
    return render(request, 'web/medicamentos.html', {'medicamentos' : medicamentos})

def medicamentos_add(request):
    return render(request, 'web/medicamentos_add.html')

def medicamentos_edit(request, idMedicamento):
    medicamento = getMedicamentoById(request, idMedicamento)
    return render(request, 'web/medicamentos_edit.html', {'medicamento' : medicamento})
#


# ARTICULOS
def articulos(request):
    return render(request, 'web/articulos.html')

def articulos_add(request):
    return render(request, 'web/articulos_add.html')
#

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
# CREAR NUEVO CENTRO MEDICO

# OBTENER LISTADO DE TODOS LOS CENTROS MEDICOS
def getCentrosMedicos():
    print('Iniciando get centros medicos...')
    extencion = "centros/"
    finalURL = urlAPI+extencion
    payload={}
    headers = {}
    response = requests.request("GET", finalURL, headers=headers, data=payload)
    return response.json()

# OBTENER UN CENTRO MEDICO

# ELIMINAR UN CENTRO MEDICO 
def deleteCentroMedico(request, idCentroMedico):
    print('Iniciando delete centro medico...')
    url = urlAPI+"centro/"+idCentroMedico
    payload={}
    headers = {
    'Content-Type': 'application/json'
    }
    response = requests.request("DELETE", url, headers=headers, data=payload)
    if response.ok:
        print('OK: eliminado.')
        centrosMedicos = getCentrosMedicos()
        return render(request, 'web/centros_medicos.html', {'centrosMedicos' : centrosMedicos})
    else:
        print('NO OK')
        print(response)
        try:
            print(response.raise_for_status())
        except requests.exceptions.HTTPError as e:
            print(e)
        return HttpResponse('<div><div><H1>Error interno, intente más tarde.</H1></div><div><input class="btn btn-danger" type=button value="Cancelar" onClick="javascript:history.go(-1);"></div></div>')



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
def getMedicamentoById(request, idMedicamento):
    print('Iniciando get medicamento by id...')
    url = urlAPI+"medicamento-id/"+idMedicamento
    payload={}
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.json())
    return response.json()

# OBTENER UN MEDICAMENTO POR SU CÓDIGO

# ACTUALIZAR UN MEDICAMENTO
def postUpdateMedicamento(request):
    print('Iniciando patch medicamento...')
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PostUpdateMedicamentoForm(request.POST)
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
            url = urlAPI+"medicamento/update/"+form.cleaned_data['id']
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
                return HttpResponse('<div><div><H1>Error en el formulario.</H1></div><div><input class="btn btn-danger" type=button value="Cancelar" onClick="javascript:history.go(-1);"></div></div>')
        else:
            print('No es valido')
            return HttpResponse('<div><div><H1>Formulario no es valido.</H1></div><div><input class="btn btn-danger" type=button value="Cancelar" onClick="javascript:history.go(-1);"></div></div>')
    else:
        return HttpResponse('<div><div><H1>Error interno, intente más tarde.</H1></div><div><input class="btn btn-danger" type=button value="Cancelar" onClick="javascript:history.go(-1);"></div></div>')

# ELIMINAR MEDICAMENTO 
def deleteMedicamento(request, idMedicamento):
    print('Iniciando delete medicamento...')
    url = urlAPI+"medicamento/"+idMedicamento
    payload={}
    headers = {
    'Content-Type': 'application/json'
    }
    response = requests.request("DELETE", url, headers=headers, data=payload)
    if response.ok:
        print('OK: eliminado.')
        medicamentos = getMedicamentos()
        return render(request, 'web/medicamentos.html', {'medicamentos' : medicamentos})
    else:
        print('NO OK')
        print(response)
        try:
            print(response.raise_for_status())
        except requests.exceptions.HTTPError as e:
            print(e)
        return HttpResponse('<div><div><H1>Error interno, intente más tarde.</H1></div><div><input class="btn btn-danger" type=button value="Cancelar" onClick="javascript:history.go(-1);"></div></div>')
    
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

