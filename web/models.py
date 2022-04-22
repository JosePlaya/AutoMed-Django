from django.db import models

#Modelo Region

class Region(models.Model):
    idRegion = models.IntegerField(primary_key=True, verbose_name="Id_Region")
    nombreRegion = models.CharField(max_length=100, verbose_name="Nombre_Region")
    
    def __str__(self):
        return self.nombreRegion

#Modelo Provincia

class Provincia(models.Model):
    idProvincia = models.IntegerField(primary_key=True, verbose_name="Id_Provincia")
    nombreProvincia = models.CharField(max_length=100, verbose_name="Nombre_Provincia")
     ## Cuadno se elimine Region se eliminaran las Provincias
    region = models.ForeignKey(Region, on_delete=models.CASCADE) 
    
    def __str__(self):
        return self.nombreProvincia

#Modelo Comuna

class Comuna(models.Model):
    idComuna = models.IntegerField(primary_key=True, verbose_name="Id_Comuna")
    nombreComuna = models.CharField(max_length=100, verbose_name="Nombre_Comuna")
     ## Cuadno se elimine Provincia se eliminaran las Comunas
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE) 
    
    def __str__(self):
        return self.nombreComuna


#Modelo Centro

class Centro(models.Model):
    idCentro = models.IntegerField(primary_key=True, verbose_name="Id_Centro")
    nombreCentro = models.CharField(max_length=100, verbose_name="Nombre_Centro")
    
    def __str__(self):
        return self.nombreCentro

#Modelo Sucursal

class Sucursal(models.Model):
    idSucursal = models.IntegerField(primary_key=True, verbose_name="Id_Sucursal")
    nombreSucursal = models.CharField(max_length=100, verbose_name="Sucursal")
    direccionSucursal = models.CharField(max_length=100, verbose_name="Direccion_Sucursal")
    comunaSucursal = models.CharField(max_length=100, verbose_name="Comuna_Sucursal")
    provinciaSucursal = models.CharField(max_length=100, verbose_name="Provincia_Sucursal")
    RegionSucursal = models.CharField(max_length=100, verbose_name="Region_Sucursal")
    ## Cuadno se elimine Centro se eliminaran las sucursales
    centro = models.ForeignKey(Centro, on_delete=models.CASCADE) 

    def __str__(self):
        return self.nombreSucursal


#Modelo Tipo Usuario

class TipoUsuario(models.Model):
    idTipoUsuario = models.IntegerField(primary_key=True, verbose_name="Id_TipoUsuario")
    nombreTipoUsuario = models.CharField(max_length=100, verbose_name="Nombre_TipoUsuario")
    
    def __str__(self):
        return self.nombreTipoUsuario

#Modelo Usuario

class Usuario(models.Model):
    idUsuario = models.IntegerField(primary_key=True, verbose_name="Id_Usuario")
    nombreUsuario = models.CharField(max_length=30, verbose_name="Nombre_Usuario")
    aPaternoUsuario = models.CharField(max_length=30, verbose_name="aPaterno_Usuario")
    aMaternoUsuario = models.CharField(max_length=30, verbose_name="aPaterno_Usuario")
    telefonoUsuario = models.IntegerField(max_length=30, verbose_name="Telefono_Usuario")
    correoUsuario = models.CharField(max_length=30, verbose_name="Correo_Usuario")    
    comunaUsuario = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    provinciaUsuario = models.ForeignKey(Provincia, on_delete=models.CASCADE)
    RegionUsuario = models.ForeignKey(Region, on_delete=models.CASCADE)
    tipoUsuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)
    centro = models.ForeignKey(Centro, on_delete=models.CASCADE)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)



    def __str__(self):
        return self.nombreUsuario



