from django.db import models

# Create your models here.

class Ingrediente(models.Model):
    nombre = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre