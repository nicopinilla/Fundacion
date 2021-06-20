from django.db import models

# Create your models here.

class Relacion (models.Model):
    idRelacion = models.IntegerField(primary_key=True, verbose_name="Id de Relación")
    nombreRelacion = models.CharField(max_length=80, blank=False, null=False, verbose_name="Nombre de la relación")

    def __str__(self):
        return self.nombreRelacion

class Usuario(models.Model):
    rut = models.CharField(max_length=10, primary_key=True, verbose_name="Rut")
    nombre = models.CharField(max_length=60, blank=False, null=False, verbose_name="Nombre")
    apellido = models.CharField(max_length=60, null=True, blank=True, verbose_name="Apellido")
    email = models.CharField(max_length=60, null=True, blank=True,verbose_name="Email")
    password = models.CharField(max_length=8, null=True, blank=True,verbose_name="Contraseña")
    relacion = models.ForeignKey(Relacion, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.rut


