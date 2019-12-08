from django.contrib import admin
from apps.registro.models import Empresas, Categoria, Estados
from django.conf import settings
# Register your models here.



admin.site.site_header = "El Directorio de México";
admin.site.site_title = "Web";
admin.site.index_title = "Registro de Empresas";
# @admin.register(Empresas)
class EmpresasAdmin(admin.ModelAdmin):
    list_display = ('nombre','categoria', 'telefono','estado','municipio','created')
    search_fields = ('nombre',)
    list_filter = ['categoria', 'estado', 'municipio']

    fieldsets = (
        (None, {
            'fields': ( 'nombre','email','telefono','servicios','imagen','categoria','red_social', 'cp', 'estado','municipio','colonia','calle','noext','latitud','longitud')
        }),
    )

    class Media:
        if hasattr(settings, 'GOOGLE_MAPS_API_KEY') and settings.GOOGLE_MAPS_API_KEY:
            css = {
                'all': ('css/admin/location_picker.css',),
            }
            js = (
                'https://maps.googleapis.com/maps/api/js?key={}'.format(settings.GOOGLE_MAPS_API_KEY),
                'js/admin/location_picker.js',
            )
    
admin.site.register(Empresas, EmpresasAdmin)

admin.site.register(Categoria)
admin.site.register(Estados)
