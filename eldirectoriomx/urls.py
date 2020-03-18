"""eldirectoriomx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import re_path, include 
from apps.registro.views import index, vista_login, vista_logout, CharData, resultados, detalle, filtrado_dentistas, filtrado_hoteles, filtrado_agencias, filtrado_restaurantes, filtro_estado_giro, registro_view, listado_participantes
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    re_path(r'^admin/',include('admin_honeypot.urls', namespace="admin_honeypot")),
    re_path(r'^admin_mx/', admin.site.urls),
    re_path(r'^$', index, name="index"),
    re_path(r'^registro/', registro_view, name="registro"),
    re_path(r'^participantes/', listado_participantes, name="participantes"),
    re_path(r'^dentistas/', filtrado_dentistas, name="dentistas"),
    re_path(r'^hoteles/', filtrado_hoteles, name="hoteles"),
    re_path(r'^agencias/', filtrado_agencias, name="agencias"),
    re_path(r'^restaurantes/', filtrado_restaurantes, name="restaurantes"),
    re_path(r'^resultados/(?P<pk>\d+)/$', detalle, name="resultados"),
    re_path(r'^resultados/(?P<pk_estado>\d+)/(?P<pk_categoria>\d+)/$', filtro_estado_giro, name="resfil"),
    re_path(r'^data/', CharData.as_view()),
    re_path(r'^login/', vista_login, name="login" ),
    re_path(r'^logout/',vista_logout,name='logout'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
