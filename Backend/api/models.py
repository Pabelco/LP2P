from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings


class Usuario(AbstractUser):
    cod_usuario = models.CharField(max_length=4,primary_key=True,unique=True)
    
    def __str__(self):
        return self.first_name + " " + self.last_name

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)



class Estado_Proforma(models.Model):
    cod_es_pro = models.CharField(max_length=1,primary_key=True,unique=True)
    estado_pro = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=50)
    def __str__(self):
        return "{0}:[{1},{2}]".format(self.cod_es_pro,self.estado_pro,self.descripcion)


class Estado_Factura(models.Model):
    cod_es_fac = models.CharField(max_length=1,primary_key=True,unique=True)
    estado_fac = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=50)
    def __str__(self):
        return "{0}:[{1},{2}]".format(self.cod_es_fac,self.estado_fac,self.descripcion)

class Estado_Certificado(models.Model):
    cod_es_cer = models.CharField(max_length=1,primary_key=True,unique=True)
    estado_cer = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=50)
    def __str__(self):
        return "{0}:[{1},{2}]".format(self.cod_es_cer,self.estado_cer,self.descripcion)



class Tipo_Auditor(models.Model):
    cod_auditor = models.CharField(max_length=1,primary_key=True,unique=True)
    tipo_auditor = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=50)
    def __str__(self):
        return "{0}:[{1},{2}]".format(self.cod_auditor,self.tipo_auditor,self.descripcion)

class Tipo_Certificado(models.Model):
    cod_tipo_cer = models.CharField(max_length=3,primary_key=True,unique=True)
    tipo_certificado = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=50)
    def __str__(self):
        return "{1}".format(self.cod_tipo_cer,self.tipo_certificado,self.descripcion)




class Cliente(models.Model):
    cod_cliente = models.CharField(max_length=4,primary_key=True,unique=True)
    ruc = models.CharField(max_length=10)
    nombre_cliente = models.CharField(max_length= 20)
    representante = models.CharField(max_length= 20)
    correo = models.EmailField(max_length= 255)
    telefono = models.CharField(max_length= 10)
    direccion = models.CharField(max_length= 50)
    cod_usuario = models.ForeignKey(Usuario,null=False,blank =False, on_delete=models.CASCADE)
   
    def __str__(self):
        return "{0}:[{1},{2},{3}]".format(self.cod_cliente,self.ruc,self.nombre_cliente,self.representante)

class Auditor(models.Model):
    cod_auditor = models.CharField(max_length=4,primary_key=True,unique=True)
    cedula_auditor = models.CharField(max_length=10)
    nombres_auditor = models.CharField(max_length= 20)
    apellidos_auditor = models.CharField(max_length= 20)
    telefono = models.CharField(max_length= 10)
    correo = models.EmailField(max_length= 255)
    tipo_auditor = models.ForeignKey(Tipo_Auditor, null=False, blank=False, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=50)
    
    def __str__(self):
        return "{0} {1}".format(self.nombres_auditor,self.apellidos_auditor)

class Norma(models.Model):
    cod_norma = models.CharField(max_length=1,primary_key=True,unique=True)
    nombre_norma = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=50)
    def __str__(self):
        return "{0}:[{1},{2}]".format(self.cod_norma,self.nombre_norma,self.descripcion)

class Proforma(models.Model):
    cod_proforma = models.CharField(max_length=3,primary_key=True,unique=True)
    cod_cliente = models.ForeignKey(Cliente, null=False, blank=False, on_delete=models.CASCADE)
    cod_norma = models.ForeignKey(Norma, null=False, blank=False, on_delete=models.CASCADE)
    costo = models.FloatField()
    fecha_proforma = models.DateField()
    estado_proforma = models.ForeignKey(Estado_Proforma, null=False, blank=False, on_delete=models.CASCADE)
    cod_usuario = models.ForeignKey(Usuario, null=False, blank=False, on_delete=models.CASCADE)
    def __str__(self):
        return "{0}:[{1},{2},{3},{4}]".format(self.cod_proforma,self.cod_cliente,self.cod_norma,self.costo,self.fecha_proforma)

class Certificado(models.Model):
    cod_certificado = models.CharField(max_length=3,primary_key=True,unique=True)
    cod_norma = models.ForeignKey(Norma, null=False, blank=False, on_delete=models.CASCADE)
    tipo_certificado = models.ForeignKey(Tipo_Certificado, null=False, blank=False, on_delete=models.CASCADE)
    cod_Auditor = models.ForeignKey(Auditor, null=False, blank=False, on_delete=models.CASCADE)
    cod_cliente = models.ForeignKey(Cliente, null=False, blank=False, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    dias_certificacion = models.CharField(max_length= 3)
    fecha_fin = models.DateField()
    costo = models.FloatField()
    estado_certificado = models.ForeignKey(Estado_Certificado, null=False, blank=False, on_delete=models.CASCADE)
    observaciones = models.CharField(max_length= 50)
    cod_usuario = models.ForeignKey(Usuario, null=False, blank=False, on_delete=models.CASCADE)
    def __str__(self):
        return "{0}:[{1},{2},{3},{4},{5}]".format(self.cod_certificado,self.cod_norma,self.tipo_certificado,self.fecha_inicio,self.fecha_fin,self.dias_certificacion)

class Factura(models.Model):
    cod_factura = models.CharField(max_length=3,primary_key=True,unique=True)
    cod_certificado = models.ForeignKey(Certificado, null=False, blank=False, on_delete=models.CASCADE)
    cod_usuario = models.ForeignKey(Usuario, null=False, blank=False, on_delete=models.CASCADE)
    fecha_factura = models.DateField()
    valor_factura = models.FloatField()
    estado_factura = models.ForeignKey(Estado_Factura, null=False, blank=False, on_delete=models.CASCADE)
    def __str__(self):
        return "{0}:[{1},{2},{3},{4}]".format(self.cod_factura,self.cod_certificado,self.cod_usuario,self.fecha_factura,self.estado_factura)