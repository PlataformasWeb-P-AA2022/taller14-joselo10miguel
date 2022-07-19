from django.db import models

# Create your models here.

class Propietario(models.Model):
    tipo_nacionalidad = (('ecuatoriana','ecuatoriana'),('peruana','peruana'),('colombiana','colombiana'))
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    nacionalidad = models.CharField(max_length=30, choices=tipo_nacionalidad)

    def __str__(self):
        return "%s %s %d %s" % (self.nombre,
                self.apellido,
                self.edad,
                self.nacionalidad)

class Departamento(models.Model):
    costo_depa = models.DecimalField(max_digits=100, decimal_places=2)
    num_cuartos= models.IntegerField()
    num_banios= models.IntegerField()
    valor= models.IntegerField()

    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE,
            related_name="propietario_depa")

    def __str__(self):
        return "%d %d %d %d" % (self.costo_depa,self.num_cuartos, self.num_banios, self.valor)
