from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Perfil(models.Model):
    nombre = models.TextField()

class Project(models.Model):
    titulo = models.CharField(max_length=200 )
    descripcion = models.CharField(max_length=250 )
    foto = models.URLField( max_length=500)
    url = models.URLField(blank=True)
    tags = models.TextField()
    user_id = models.IntegerField(default=None)
    def username(self):
        return User.objects.get(id=self.user_id).username

class IpAddress (models.Model):
    pub_date=models.DateField("Fecha de petición")
    ip_address = models.GenericIPAddressField()

    class Meta:
        verbose_name = 'Direccion IP'
        verbose_name_plural = 'Direcciones de Ip'
    def __str__(self):
        return f"{self.ip_address}" 
