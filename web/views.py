#import requests
import json
from django.shortcuts import render
#from pyrebase import pyrebase


# ---------------------------------------------------------------- #
# ---------------------CREDENCIALES FIREBASE---------------------- #
# ---------------------------------------------------------------- #
# For Firebase JS SDK v7.20.0 and later, measurementId is optional
#firebaseConfig = {
#  apiKey: "AIzaSyAXP_MEtzVz6-mEyfjXt0Z-OIEOcSXqDYs",
#  authDomain: "automed-cl.firebaseapp.com",
#  projectId: "automed-cl",
#  storageBucket: "automed-cl.appspot.com",
#  messagingSenderId: "509880148775",
#  appId: "1:509880148775:web:cf25756b2b7ccef529ff02",
#  measurementId: "G-MT8KWKPZ7E"
#}
#firebase=pyrebase.initialize_app(firebaseConfig)
#authe = firebase.auth()

# VARIABLES
urlAPI = "https:#us-central1-automed-cl.cloudfunctions.net/webApi/"

# VARIABLES
urlAPI = "https:#us-central1-automed-cl.cloudfunctions.net/webApi/"

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


# ---------------------------------------------------------------- #
# ---------------------FIREBASE AUTH METHOD----------------------- #
# ---------------------------------------------------------------- #
# METODO DE SIGN IN (AUTENTIFICAR USUARIO CON CORREO Y CONTRASEÑA)
#def postsignIn(request):
#    email=request.POST.get('email')
#    pasw=request.POST.get('pass')
#    try:
#        # if there is no error then signin the user with given email and password
#        user=authe.sign_in_with_email_and_password(email,pasw)
#    except:
#        message="Invalid Credentials!!Please ChecK your Data"
#        return render(request,"Login.html",{"message":message})
#    session_id=user['idToken']
#    request.session['uid']=str(session_id)
#    return render(request,"Home.html",{"email":email})

# CERRAR SECIÓN DEL USUARIO
#def logout(request):
#    try:
#        del request.session['uid']
#    except:
#        pass
#    return render(request,"Login.html")

#SE DEBE BORRAR ESTA FUNCION
def signup():
    print('test')


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
#                   CREAR USUARIO                   #
# ------------------------------------------------- #
# NEW ADMIN USER

# NEW MEDICO USER

# NEW FARMACEUTICO USER



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
#                INFORMACIÓN USUARIOS               \\
# ------------------------------------------------- \\
# OBTENER INFORMACIÓN USUARIO ADMIN

# OBTENER INFORMACIÓN USUARIO FARMACEUTICO

# OBTENER INFORMACIÓN USUARIO FARMACEUTICO



# ------------------------------------------------- \\
#                    MEDICAMENTOS                   \\
# ------------------------------------------------- \\
# CREAR NUEVO MEDICAMENTOS

# OBTENER TODOS LOS MEDICAMENTOS

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

