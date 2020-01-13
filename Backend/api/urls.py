from .views import *
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from django.views.decorators.csrf import csrf_exempt


urlpatterns =[

    #path('rest-auth/', obtain_auth_token, name='api_token_auth'),
    path('rest-auth/', csrf_exempt(CustomAuthToken.as_view()), name='api_token_auth'),

    #usuario
    path('usuario/create',CreateUsuario.as_view()),
    path('usuario/',UsuarioList.as_view(),name='usuario'),
    path('usuario/update/<int:pk>', UpdateUsuario.as_view()),
    path('usuario/<str:pk>', GetUsuario.as_view()),
    path('usuario/delete/<int:pk>', DeleteUsuario.as_view()),
    #end usuario 

    #cliente
    path('cliente/',ClienteList.as_view(),name='cliente'),
    path('cliente/<int:pk>',GetCliente.as_view()),
    path('cliente/create',CreateCliente.as_view()),
    path('cliente/update/<int:pk>',UpdateCliente.as_view()),
    path('cliente/delete/<int:pk>',DeleteCliente.as_view()),
    #end cliente

    #auditor
    path('auditor/', AuditorList.as_view(),name='auditor'),

    path('auditor/<int:pk>', GetAuditor.as_view(),),
    path('auditor/create', CreateAuditor.as_view(),),
    path('auditor/update/<int:pk>', UpdateAuditor.as_view(),),
    path('auditor/delete/<int:pk>', DeleteAuditor.as_view(),),
    #end auditor

    #proforma
    path('proforma/',ProformaList.as_view(),name='proforma'),
    path('proforma/<int:pk>',GetProforma.as_view()),
    path('proforma2/<int:pk>',GetProforma2.as_view()),
    path('proforma/create',CreateProforma.as_view()),
    path('proforma/update/<int:pk>',UpdateProforma.as_view()),
    path('proforma/delete/<int:pk>',DeleteProforma.as_view()),
    #end proforma

    #certificado
    path('certificado/',CertificadoList.as_view(),name='certificado'),
    path('certificado/<int:pk>',GetCertificado.as_view()),
    path('certificado/create',GetCertificado.as_view()),
    path('certificado/update/<int:pk>',UpdateCertificado.as_view()),
    path('certificado/delete/<int:pk>',DeleteCertificado.as_view()),
    #end certificado

    #cantidad cliente proforma
    path('cantidadcp/',CantidadCP.as_view()),

    #tipo auditor
    path('tipo_auditor/',GetTipoAuditor.as_view()),

    #norma
    path('norma/',GetNorma.as_view()),
    
    #Tipo certificado GetTipoCertificado
    path('tcertificado/',GetTipoCertificado.as_view()),
    path('certificado_estado/',GetEstadoCertificado.as_view()),
    #correo
    path('sendemail', SendEmail.as_view(),name='Send Email'),
    #end correo
    
    #GRAFICOS
    path('graficoPie/',GraficosApiTwo.as_view(),name='grafico'),
    path('graficoBar/',GraficosApi.as_view(),name='grafico'),
    path('graficoPie2/',GraficosApiThree.as_view(),name='grafico'),
    
    
    path('proforma/estado',GetEstadoProforma.as_view()),
]
