from .views import *
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token 


urlpatterns =[
    path('usuario/',CreateUser.as_view(),name='Usuario'),
    path('ver_usuario/',UsuarioList.as_view(),name='ver_usuario'),
    path('usuario/<int:pk>', Usuario_detail),
    path('rest-auth/', obtain_auth_token, name='api_token_auth'),
    path('cliente/',ClienteList.as_view(),name='cliente'),
   
    path('auditor/', AuditorList.as_view(),name='auditor'),
    path('auditor/<int:pk>', Auditor_detail),
    path('auditor_crear', CreateAuditor.as_view(),name='auditor crear'),
    path('tipo_auditor/', Tipo_AuditorList.as_view(),name='tipo_auditor'),

    path('factura/', FacturaList.as_view(),name='factura'),

    path('certificado/', CertificadoList.as_view(),name='certificado'),
    path('estado_certificado/', Estado_CertificadoList.as_view(),name='auditor'),
    path('certificado/<int:pk>',Certificado_detail),

    path('proforma/',ProformaList.as_view(),name='proforma'),
    path('proforma/<int:pk>',Proforma_detail),

    path('norma/',NormaList.as_view(),name='norma'),

    path('sendemail', SendEmail.as_view(),name='Send Email'),

 



]
