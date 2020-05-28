from django.db import models

# Create your models here.


class Libro(models.Model):
	codigo=models.CharField(max_length=10)
	nombre=models.CharField(max_length=50)
	def __str__(self):
		return '{}'.format(self.nombre)

class Estudiante(models.Model):
	carnet=models.CharField(max_length=10)
	nombre=models.CharField(max_length=10)
	def __str__(self):
		return '{}'.format(self.nombre)