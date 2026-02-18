from django.db import models

# Create your models here.

class ErrorReport(models.Model): 
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField(blank=False, null=False)
    tipo_error = models.CharField(blank=False, null=False)
    url = models.URLField
    metodo_http = models.CharField(max_length=10)
    