from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Cliente)

admin.site.register(Factura)
admin.site.register(Certificado)
admin.site.register(Proforma)
admin.site.register(Norma)
admin.site.register(Auditor)

admin.site.register(Estado_Certificado)
admin.site.register(Estado_Factura)
admin.site.register(Estado_Proforma)
admin.site.register(Tipo_Auditor)
admin.site.register(Tipo_Certificado)


# Register your models here.
