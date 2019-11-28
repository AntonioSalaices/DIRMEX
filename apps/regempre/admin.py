from django.contrib import admin
from apps.regempre.models import Registro
# Register your models here.

admin.site.site_header = "El Directorio de México";
admin.site.site_title = "Web";
admin.site.index_title = "Registro de Empresas";
admin.site.register(Registro)