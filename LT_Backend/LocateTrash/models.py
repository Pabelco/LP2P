from django.db import models


# Create your models here.
class Usuario(models.Model):
    usuario = models.CharField(max_length=25)
    email = models.EmailField()
    contrasena = models.CharField(max_length=15)    
    def __str__(self):
        template = '{0.usuario}, {0.email}, {0.contrasena}'
        return template.format(self)

class Basurero(models.Model):
    nombre = models.CharField(max_length=100)
    horaInicio = models.CharField(max_length=5,default='00:00')
    horaFin = models.CharField(max_length=5,default='00:00')
    latitud = models.CharField(max_length=20)
    longitud = models.CharField(max_length=20)
    calificacion = models.FloatField(default=0.0)

    def __str__(self):
        template = '{0.nombre}, {0.latitud}, {0.longitud}, {0.horaInicio}, {0.horaFin}, {0.calificacion}'
        return template.format(self)

class BasureroCalificado(models.Model):
    basurero = models.ForeignKey(Basurero, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    feeback = models.TextField()
    fechaCalificado = models.DateTimeField(auto_now_add=True)
    calificacion = models.FloatField(default=0.0)

    def __str__(self):
        template = '{0.basurero}, {0.usuario}, {0.feedback}, {0.fechaCalificado}, {0.calificacion}'
        return template.format(self)


# class BasureroCalificadoxUsuario(models.Model):
#     usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
#     basureroCalificado = models.ForeignKey(BasureroCalificado, on_delete=models.CASCADE)