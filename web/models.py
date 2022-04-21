from django.db import models

#Modelo Sucursal

class Centro(models.Model):
    idCentro = models.IntegerField(primary_key=True, verbose_name="Id")
    nombreCentro = models.CharField(max_length=100, verbose_name="Sucursal")
    
    def __str__(self):
        return self.nombreCentro

class Sucursal(models.Model):
    idSucursal = models.IntegerField(primary_key=True, verbose_name="Id")
    nombreSucursal = models.CharField(max_length=100, verbose_name="Sucursal")
    direccionSucursal = models.CharField(max_length=100, verbose_name="Direccion")
    comunaSucursal = models.CharField(max_length=100, verbose_name="Comuna")
    provinciaSucursal = models.CharField(max_length=100, verbose_name="Provincia")
    RegionSucursal = models.CharField(max_length=100, verbose_name="Region")
    ## Cuadno se elimine Centro se eliminaran las sucursales
    Centro = models.ForeignKey(Centro, on_delete=models.CASCADE) 

    def __str__(self):
        return self.nombreSucursal



