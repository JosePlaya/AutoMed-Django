from django import forms

class PostNewMedicamentoForm(forms.Form):
    stock = forms.IntegerField(label='stock_medicamento')
    nombre = forms.CharField(label='nombre_medicamento', max_length=150)
    codigo = forms.CharField(label='codigo_medicamento', max_length=10)
    gramaje = forms.CharField(label='gramaje_medicamento', max_length=10)
    cantidad = forms.CharField(label='cantidad_medicamento', max_length=50)
    contenido = forms.CharField(label='contenido_medicamento', max_length=150)
    fabricante = forms.CharField(label='fabricante_medicamento', max_length=150)
    descripcion = forms.CharField(label='descripcion_medicamento', max_length=150)
    idCentroMedico = forms.CharField(label='id_centro_medico_medicamento', max_length=30)
    
class PostUpdateMedicamentoForm(forms.Form):
    id = forms.CharField(label='id_medicamento')
    stock = forms.IntegerField(label='stock_medicamento')
    nombre = forms.CharField(label='nombre_medicamento', max_length=150)
    codigo = forms.CharField(label='codigo_medicamento', max_length=10)
    gramaje = forms.CharField(label='gramaje_medicamento', max_length=10)
    cantidad = forms.CharField(label='cantidad_medicamento', max_length=50)
    contenido = forms.CharField(label='contenido_medicamento', max_length=150)
    fabricante = forms.CharField(label='fabricante_medicamento', max_length=150)
    descripcion = forms.CharField(label='descripcion_medicamento', max_length=150)
    idCentroMedico = forms.CharField(label='id_centro_medico_medicamento', max_length=30)
    
class PostNewUser(forms.Form):
    nombre = forms.CharField(label='nombre_usuario', max_length=150)
    rut = forms.CharField(label='rut_usuario', max_length=12)
    apaterno = forms.CharField(label='apaterno_usuario', max_length=10)
    amaterno = forms.CharField(label='amaterno_usuario', max_length=50)
    correo = forms.EmailField(label='correo_usuario', max_length=150)
    especialidad = forms.CharField(label='especialidad_usuario', max_length=150, required=False)
    tipoUsuario = forms.CharField(label='tipoUsuario_usuario', max_length=150)
    idCentroMedico = forms.CharField(label='id_centro_medico_usuario', max_length=30)
    password = forms.CharField(label='password_usuario', max_length=30)
    
class PostNewPacienteForm(forms.Form):
    VERDE = 'verde'
    ROSADO = 'rosado'
    CELESTE = 'celeste'
    COLOR_CHOICES = (
        (VERDE, "verde"),
        (ROSADO, "rosado"),
        (CELESTE, "celeste")
    )
    rut = forms.CharField(label='rut_paciente', max_length=12)
    nombre = forms.CharField(label='nombre_paciente', max_length=150)
    apaterno = forms.CharField(label='apaterno_paciente', max_length=10)
    amaterno = forms.CharField(label='amaterno_paciente', max_length=50)
    correo = forms.EmailField(label='correo_paciente', max_length=150)
    telefono = forms.IntegerField(label='telefono_paciente')
    fechan = forms.DateField(label='fecha_nacimiento_paciente')
    color_cif = forms.CharField(label='color_cif_paciente')
    not_wsp = forms.BooleanField(label='noticiacion_whatsapp_paciente')
    not_cor = forms.BooleanField(label='noticiacion_correo_paciente')
    
class PostNewPrescripcionForm(forms.Form):
    rutMedico = forms.CharField(label='rut_medico', max_length=12)
    rutPaciente = forms.CharField(label='rut_paciente', max_length=12)
    idCentroMedico = forms.CharField(label='id_centro_medico', max_length=100)
    descripcion = forms.CharField(label='descripcion', max_length=250)
    duracionTratamiento = forms.CharField(label='duracion_tratamiento', max_length=150)
    medicamentos = forms.CharField(label='medicamentos')
    
    
# curl -X "POST" "https://conversations.messagebird.com/v1/send" \
# -H "Authorization: AccessKey HbN2vflvdwndrCNqFkcsAB5Hs" \
# -H "Content-Type: application/json" \
# --data '{
#   "to": "+56976423354",
#   "from": "e22d1dc8-d9d1-4070-8da8-7d703df148fd",
#   "type": "text",
#   "content": {
#     "text": "¡Prueba de WshatApp!",
#     "disableUrlPreview": false
#   }
# }'