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