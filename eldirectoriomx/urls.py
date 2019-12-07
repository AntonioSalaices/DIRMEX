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
from django.urls import re_path
from apps.registro.views import index, vista_login, vista_logout, CharData, resultados, view_project
from apps.api.api import ListEmpresasAPI
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    re_path(r'admin/', admin.site.urls),
    re_path(r'^$', index, name="index"),
    re_path(r'^resultados/', resultados, name="resultados"),
    re_path(r'^resultados/(?P<project_id>\d+)/$', view_project, name='view_project'),
    re_path(r'^listado/', ListEmpresasAPI.as_view()),
    re_path(r'^data/', CharData.as_view()),
    re_path(r'^login/', vista_login, name="login" ),
    re_path(r'^logout/',vista_logout,name='logout'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)