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