import json
import requests
from django.http import Http404
from django.core import serializers
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import PostNewMedicamentoForm, PostUpdateMedicamentoForm, PostNewUser, PostNewPacienteForm, PostNewPrescripcionForm
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

def medico(request, userType):
    return render(request, 'web/medico.html', {'userType' : userType})

def farmaceutico(request, userType):
    return render(request, 'web/farmaceutico.html', {'userType' : userType})

def administrador(request, userType):
    return render(request, 'web/administrador.html', {'userType' : userType})
    
def index(request, userType, uid):
    return render(request, 'web/index.html', {
        'userType' : userType,
        'uid' : uid
    })

def perfil(request, userType, uid):
    print('UID = '+uid)
    usuario = getUser2(uid)
    return render(request, 'web/perfil.html', {
        'userType' : userType,
        'usuario' : usuario
    })
#


# CENTROS MEDICOS
def centros_medicos(request, userType):
    centrosMedicos = getCentrosMedicos()
    return render(request, 'web/centros_medicos.html', {
        'userType' : userType,
        'centrosMedicos' : centrosMedicos
        })

def centros_medicos_add(request, userType):
    return render(request, 'web/centros_medicos_add.html', {'userType' : userType})
#

#
# MEDICAMENTOS
def medicamentos(request, userType, idCentroMedico):
    medicamentos = getMedicamentosByCentroMedico(request, idCentroMedico)
    return render(request, 'web/medicamentos.html', {
        'userType' : userType,
        'medicamentos' : medicamentos
        })

def medicamentos_add(request, userType):
    return render(request, 'web/medicamentos_add.html', {'userType' : userType})

def medicamentos_edit(request, userType, idMedicamento):
    medicamento = getMedicamentoById(request, idMedicamento)
    return render(request, 'web/medicamentos_edit.html', {
        'userType' : userType,
        'medicamento' : medicamento
        })
#


# ARTICULOS
def articulos(request):
    return render(request, 'web/articulos.html')

def articulos_add(request):
    return render(request, 'web/articulos_add.html')
#

# FARMACEUTICO
def administradores(request, userType):
    administradores = getUserByType('administrador')
    return render(request, 'web/administradores.html', {
        'userType' : userType,
        'administradores' : administradores
        })
#

# FARMACEUTICO
def farmaceuticos(request, userType):
    farmaceuticos = getUserByType('farmaceutico')
    return render(request, 'web/farmaceuticos.html', {
        'userType' : userType,
        'farmaceuticos' : farmaceuticos
        })
#

# MEDICO
def medicos(request, userType):
    medicos = getUserByType('medico')
    return render(request, 'web/medicos.html', {
        'userType' : userType,
        'medicos' : medicos
    })

# USUARIOS
def user_add(request, userType, newUserType, idCentroMedico):
    return render(request, 'web/user_add.html', {
        'userType' : userType,
        'newUserType': newUserType,
        'idCentroMedico' : idCentroMedico
        })
#

# PACIENTES
def pacientes(request, userType):
    pacientes = getPacientes()
    return render(request, 'web/pacientes.html', {
        'userType' : userType,
        'pacientes' : pacientes
    })

def pacientes_add(request, userType):
    return render(request, 'web/pacientes_add.html', {
        'userType' : userType,
    })
#

# PRESCRIPCIONES
def prescripciones(request, userType):
    return render(request, 'web/prescripciones.html', {
        'userType' : userType,
    })

def prescripciones_add(request, userType):
    medicamentos = getMedicamentos()
    return render(request, 'web/prescripciones_add.html', {
        'userType' : userType,
        'medicamentos' : medicamentos
    })
#


# ---------------------------------------------------------------- #
# --------------------FUNCIONES CONECCIÓN API--------------------- #
# ---------------------------------------------------------------- #
   
# ------------------------------------------------- #
#                      USUARIOS                     #
# ------------------------------------------------- #
# NUEVO USUARIO
def postNewUser(request):
    print('Iniciando post new user...')
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PostNewUser(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            data = {
                "rut": form.cleaned_data['rut'],
                "nombre": form.cleaned_data['nombre'],
                "correo": form.cleaned_data['correo'],
                "apaterno": form.cleaned_data['apaterno'],
                "amaterno": form.cleaned_data['amaterno'],
                "tipoUsuario": form.cleaned_data['tipoUsuario'],
                "password": form.cleaned_data['password'],
                "especialidad": form.cleaned_data['especialidad'],
                "idCentroMedico": form.cleaned_data['idCentroMedico']
            }
            print(data)
            url = urlAPI+"usuario/"
            payload = json.dumps(data)
            headers = {
                'Content-Type': 'application/json'
            }
            response = requests.request("POST", url, headers=headers, data=payload)
            if response.ok:
                print('OK')
                return render(request, 'web/index.html', {
                    'userType' : 'administrador'
                    })
            else:
                print('NO OK')
                print(response)
                try:
                    print(response.raise_for_status())
                except requests.exceptions.HTTPError as e:
                    print(e)
                return HttpResponse('<div><div><H1>Error interno, intente más tarde.</H1></div><div>Respuesta: ${response}</div><div>Error: ${e}</div><div><input class="btn btn-danger" type=button value="Cancelar" onClick="javascript:history.go(-1);"></div></div>')
        else:
            print('No es valido')
            print(form.errors)
            return HttpResponse('<div><div><H1>Error interno, intente más tarde.</H1></div><div>Error: ${form.errors}</div><div><input class="btn btn-danger" type=button value="Cancelar" onClick="javascript:history.go(-1);"></div></div>')
    else:
        return HttpResponse('<div><div><H1>Formulario no válido, intente con nuevos valores.</H1></div><div><input class="btn btn-danger" type=button value="Cancelar" onClick="javascript:history.go(-1);"></div></div>')

# OBTENER USUARIOS POR TIPO
def getUserByType(type):
    url = urlAPI+"usuarios/"+type
    payload={}
    headers = {
      'Content-Type': 'application/json'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    if response.ok:
        return response.json()
    else:
        return    
    
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

def getUser2(id):
    print('Iniciando get usuario...')
    url = urlAPI+"usuario/"+id
    payload={}
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.json()

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

# OBTENER INFORMACIÓN DE UN USUARIO
def getUser_idCentroAtencionYRut(request, id):
    print('Iniciando get di centro atención del usuario y rut...')
    url = urlAPI+"usuario/"+id
    payload={}
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    r = response.json()
    return HttpResponse(r['idCentroMedico']+'/'+r['rut'])

# ELIMINAR UN USUARIO
def deleteUsuario(request, idUsuario):
    print('Iniciando delete usuario...')
    url = urlAPI+"usuario/"+idUsuario
    payload={}
    headers = {
    'Content-Type': 'application/json'
    }
    response = requests.request("DELETE", url, headers=headers, data=payload)
    if response.ok:
        print('OK: eliminado.')
        return render(request, 'web/index.html', {
                    'userType' : 'administrador'
                })
    else:
        print('NO OK')
        print(response)
        try:
            print(response.raise_for_status())
        except requests.exceptions.HTTPError as e:
            print(e)
        return HttpResponse('<div><div><H1>Error interno, intente más tarde.</H1></div><div>Respuesta: {response}</div><div>Error: {e}</div><div><input class="btn btn-danger" type=button value="Cancelar" onClick="javascript:history.go(-1);"></div></div>')

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
def postNewPaciente(request):
    print('Iniciando post new paciente...')
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PostNewPacienteForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            fechan = form.cleaned_data['fechan']
            fechan = fechan.isoformat()
            data = {
                "rut": form.cleaned_data['rut'],
                "fechan": fechan,
                "correo": form.cleaned_data['correo'],
                "nombre": form.cleaned_data['nombre'],
                "apaterno": form.cleaned_data['apaterno'],
                "amaterno": form.cleaned_data['amaterno'],
                "telefono": form.cleaned_data['telefono'],
                "not_wsp": form.cleaned_data['not_wsp'],
                "not_cor": form.cleaned_data['not_cor'],
                "color_cif": form.cleaned_data['color_cif']
            }
            url = urlAPI+"paciente/"
            print(data)
            payload = ''
            try:
                payload = json.dumps(data)
            except requests.exceptions.HTTPError as e:
                print(e)
            headers = {
                'Content-Type': 'application/json'
            }
            response = requests.request("POST", url, headers=headers, data=payload)
            if response.ok:
                print('OK')
                pacientes = getPacientes()
                return render(request, 'web/pacientes.html', {
                    'userType' : 'medico',
                    'pacientes' : pacientes
                })
            else:
                print('NO OK')
                print(response.text)
                try:
                    print(response.raise_for_status())
                except requests.exceptions.HTTPError as e:
                    print(e)
                return HttpResponse('<div><div><H1>Formulario no válido, intente con nuevos valores.</H1></div><div><input class="btn btn-danger" type=button value="Cancelar" onClick="javascript:history.go(-1);"></div></div>')
        else:
            print('No es valido')
            print(form.errors)
            return HttpResponse('<div><div><H1>Formulario no válido, intente con nuevos valores.</H1></div><div><input class="btn btn-danger" type=button value="Cancelar" onClick="javascript:history.go(-1);"></div></div>')
    else:
        return HttpResponse('<div><div><H1>Formulario no válido, intente con nuevos valores.</H1></div><div><input class="btn btn-danger" type=button value="Cancelar" onClick="javascript:history.go(-1);"></div></div>')

# OBTENER TODOS LOS PACIENTES
def getPacientes():
    print('Iniciando get pacientes...')
    url = urlAPI+"pacientes/"
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.json()

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
                return render(request, 'web/medicamentos.html', {
                    'userType' : 'administrador',
                    'medicamentos' : medicamentos
                    })
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
        return render(request, 'web/medicamentos.html', {
                'userType' : 'administrador',
                'medicamentos' : medicamentos
            })
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
# CREAR NUEVA PRESCRIPCIÓN
def postNewPrescripcion(request):
    print('Iniciando post new prescripción...')
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PostNewPrescripcionForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            data = {
                "rutMedico": form.cleaned_data['rutMedico'],
                "rutPaciente": form.cleaned_data['rutPaciente'],
                "idCentroMedico": form.cleaned_data['idCentroMedico'],
                "descripcion": form.cleaned_data['descripcion'],
                "duracionTratamiento": form.cleaned_data['duracionTratamiento'],
                "medicamentos": form.cleaned_data['medicamentos']
            }
            
            print(data)
            url = urlAPI+"prescripcion/"
            payload = json.dumps(data)
            headers = {
                'Content-Type': 'application/json'
            }
            response = requests.request("POST", url, headers=headers, data=payload)
            if response.ok:
                print('OK')
                return render(request, 'web/index.html', {
                    'userType' : 'administrador'
                    })
            else:
                print('NO OK')
                print(response)
                try:
                    print(response.raise_for_status())
                except requests.exceptions.HTTPError as e:
                    print(e)
                return HttpResponse('<div><div><H1>Error interno, intente más tarde.</H1></div><div>Respuesta: ${response}</div><div>Error: ${e}</div><div><input class="btn btn-danger" type=button value="Cancelar" onClick="javascript:history.go(-1);"></div></div>')
        else:
            print('No es valido')
            print(form.errors)
            return HttpResponse('<div><div><H1>Error interno, intente más tarde.</H1></div><div>Error: ${form.errors}</div><div><input class="btn btn-danger" type=button value="Cancelar" onClick="javascript:history.go(-1);"></div></div>')
    else:
        return HttpResponse('<div><div><H1>Formulario no válido, intente con nuevos valores.</H1></div><div><input class="btn btn-danger" type=button value="Cancelar" onClick="javascript:history.go(-1);"></div></div>')

# OBTENER TODOS LOS MEDICAMENTOS

# OBTENER UNA PREESCRIPCION

# CREAR NUEVO MEDICAMENTOS

# ACTUALIZAR UN MEDICAMENTO

# ELIMINAR MEDICAMENTO 

