from django.contrib import admin
from apps.registro.models import Empresas, Categoria, Estados
# Register your models here.



admin.site.site_header = "El Directorio de México";
admin.site.site_title = "Web";
admin.site.index_title = "Registro de Empresas";
class EmpresasAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'categoria', 'telefono','estado','municipio','created']
    list_filter = ['categoria', 'estado', 'municipio']

    
admin.site.register(Empresas, EmpresasAdmin)

admin.site.register(Categoria)
admin.site.register(Estados)