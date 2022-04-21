from django.shortcuts import render

def login(request):
    return render(request, 'web/login.html')

def medico(request):
    return render(request, 'web/medico.html')

def farmaceutico(request):
    return render(request, 'web/farmaceutico.html')

def administrador(request):
    return render(request, 'web/administrador.html')
