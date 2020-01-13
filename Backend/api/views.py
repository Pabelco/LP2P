# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.db.models import Count


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'isAdmin': user.is_superuser
            ,
            'cod': user.cod_usuario
        })


#USUARIO
#--------------------------------------------------------------
class CreateUsuario(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Usuario.objects.filter(is_superuser=False)
    serializer_class = UsuarioSerializer

class GetUsuario(generics.RetrieveAPIView):
    permission_classes = (AllowAny,)
    queryset = Usuario.objects.filter(is_superuser=False)
    serializer_class = UsuarioSerializer

class UsuarioList(generics.ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Usuario.objects.filter(is_superuser=False)
    serializer_class = UsuarioSerializer

class DeleteUsuario(generics.DestroyAPIView):
    permission_classes = (AllowAny,)
    queryset = Usuario.objects.filter(is_superuser=False)
    serializer_class = UsuarioSerializer

class UpdateUsuario(generics.UpdateAPIView):
    permission_classes = (AllowAny,)
    queryset = Usuario.objects.filter(is_superuser=False)
    serializer_class = UsuarioSerializer
#--------------------------------------------------------------

#CLIENTE
#--------------------------------------------------------------
class ClienteList(generics.ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class GetCliente(generics.RetrieveAPIView):
    
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class CreateCliente(generics.CreateAPIView):
    
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class UpdateCliente(generics.UpdateAPIView):
    
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer   

class DeleteCliente(generics.DestroyAPIView):
   
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
#--------------------------------------------------------------

#AUDITOR
#--------------------------------------------------------------
class AuditorList (generics.ListAPIView):
    
    queryset = Auditor.objects.all()
    serializer_class = AuditorSerializer


class CreateAuditor(generics.CreateAPIView):
    
    queryset = Auditor.objects.all()
    serializer_class = AuditorSerializer

class GetAuditor(generics.RetrieveAPIView):   
    
    queryset = Auditor.objects.all()
    serializer_class = AuditorSerializer

class UpdateAuditor(generics.UpdateAPIView):   
    
    queryset = Auditor.objects.all()
    serializer_class = AuditorSerializer 

class DeleteAuditor(generics.DestroyAPIView):
    
    queryset = Auditor.objects.all()
    serializer_class = AuditorSerializer
#--------------------------------------------------------------

#PROFORMA
#--------------------------------------------------------------
class ProformaList (generics.ListAPIView):
    
    queryset = Proforma.objects.all()
    serializer_class = ProformaSerializer

class CreateProforma (generics.CreateAPIView):
    
    queryset = Proforma.objects.all()
    serializer_class = ProformaSerializer

class GetProforma (generics.RetrieveAPIView):
    
    queryset = Proforma.objects.all()
    serializer_class = ProformaSerializer

class GetProforma2 (generics.RetrieveAPIView):
    
    queryset = Proforma.objects.all()
    serializer_class = ProformaSerializer2

class UpdateProforma (generics.UpdateAPIView):
    
    queryset = Proforma.objects.all()
    serializer_class = ProformaSerializer2

class DeleteProforma (generics.DestroyAPIView):
    
    queryset = Proforma.objects.all()
    serializer_class = ProformaSerializer           
#--------------------------------------------------------------

#CERTIFICADO
#--------------------------------------------------------------
class CertificadoList (generics.ListAPIView):
    
    queryset = Certificado.objects.all()
    serializer_class = CertificadoSerializer 

class GetCertificado (generics.RetrieveAPIView):
    
    queryset = Certificado.objects.all()
    serializer_class = CertificadoSerializer 

class CreateCertificado (generics.CreateAPIView):
    
    queryset = Certificado.objects.all()
    serializer_class = CertificadoSerializer 

class UpdateCertificado (generics.UpdateAPIView):
    
    queryset = Certificado.objects.all()
    serializer_class = Certificado2Serializer

class DeleteCertificado (generics.DestroyAPIView):
    
    queryset = Certificado.objects.all()
    serializer_class = CertificadoSerializer 
#--------------------------------------------------------------

#CORREO
#--------------------------------------------------------------
class SendEmail(APIView):
    permission_classes =(AllowAny,)
    def post(self, request,format='json'):
        if(request.method=='POST'):
            name = "Nombre :"+request.data['name']
            mail = "Email :"+request.data['mail']
            telefono = "Telefono :"+request.data['telefono']
            mensaje= "Mensaje :"+request.data['mensaje']
            user = Usuario.objects.get(is_superuser=True)
            emailAdmin = user.email
             
            
            send_mail('Contactenos Bureau Veritas',mensaje,settings.EMAIL_HOST_USER, [emailAdmin], fail_silently=False)
            return Response(request.data)
#--------------------------------------------------------------


#APIVIEW
#--------------------------------------------------------------
class CantidadCP(APIView):
    permission_classes =(AllowAny,)
    def get(self,request,format= 'none'):
        cantidad = Cliente.objects.count()
        proforma = Proforma.objects.count()
        return Response({'Clientes':cantidad,'Proforma':proforma})
#--------------------------------------------------------------

# Tipo AUDITOR
#--------------------------------------------------------------
class GetTipoAuditor(generics.ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Tipo_Auditor.objects.all()
    serializer_class = Tipo_AuditorSerializer
#--------------------------------------------------------------

#Norma
#--------------------------------------------------------------
class GetNorma(generics.ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Norma.objects.all()
    serializer_class = NormaSerializer
#--------------------------------------------------------------

#Tipo Certificado
#--------------------------------------------------------------
class GetTipoCertificado(generics.ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Tipo_Certificado.objects.all()
    serializer_class = Tipo_CertificadoSerializer
#--------------------------------------------------------------

#Estado Certificado
class GetEstadoCertificado(generics.ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Estado_Certificado.objects.all()
    serializer_class = Estado_CertificadoSerializer

#Estado Proforma
class GetEstadoProforma(generics.ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Estado_Proforma.objects.all()
    serializer_class = Estado_ProformaSerializer
















   
class GraficosApi(APIView):

    permission_classes =(AllowAny,)


    def get(self, request, format=None):

        datos= Certificado.objects.count()
        datos2 = Proforma.objects.count()
        return Response({"certificados":datos,"proformas":datos2})
    
class GraficosApiTwo(APIView):

    permission_classes =(AllowAny,)


    def get(self, request, format=None):

        datos= Certificado.objects.values('cod_usuario').annotate(dcount=Count('cod_usuario'))
        return Response(datos)
    
class GraficosApiThree(APIView):

    permission_classes =(AllowAny,)


    def get(self, request, format=None):

        datos= Proforma.objects.values('cod_usuario').annotate(dcount=Count('cod_usuario'))
        return Response(datos)
    
