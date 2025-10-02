from django.db import models

# Create your models here.
class Programador(models.Model):

    
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=100)
    fechaNacimiento = models.DateField()
    rol = models.CharField(max_length=50, checkconstraints=['Programador', 'Tester', 'Jefe de Equipo'])

    def __str__(self):
        return f"{self.id} {self.nombre} {self.apellido}" 

class Tarea(models.Model):
    nombreTarea = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=300)
    estimacion = models.IntegerField(null=True, blank=True)
    asignada = models.BooleanField(default=False)
    usuario = models.ForeignKey(Programador, on_delete=models.CASCADE, null=True, blank=True)
    sprint = models.ForeignKey('Sprint', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.id} {self.nombreTarea} {self.asignada} {self.descripcion} {self.estimacion} "

class Sprint(models.Model):
    nombre = models.CharField(max_length=50)
    fechaInicio = models.DateField()
    fechaFin = models.DateField()

    def __str__(self):
        return f"{self.id} {self.nombre} {self.fechaInicio} - {self.fechaFin} "