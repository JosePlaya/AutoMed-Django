from django.shortcuts import render

def login(request):
    return render(request, 'web/login.html')

def medico(request):
    return render(request, 'web/medico.html')

def farmaceutico(request):
    return render(request, 'web/farmaceutico.html')

def administrador(request):
    return render(request, 'web/administrador.html')

def articulos_farmacia(request):
    return render(request, 'web/articulos_farmacia.html')

def home_farmacia(request):
    return render(request, 'web/home_farmacia.html')

def medicamentos_farmacia(request):
    return render(request, 'web/medicamentos_farmacia.html')

def pacientes_farmacia(request):
    return render(request, 'web/pacientes_farmacia.html')

def prescripciones_farmacia(request):
    return render(request, 'web/prescripciones_farmacia.html')

def perfil(request):
    return render(request, 'web/perfil.html')
