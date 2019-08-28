"""outmed URL Configuration

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
from django.urls import path, include

urlpatterns = [
    path('', include('app_outmed.urls')),
    path('cadastro/', include('app_outmed.urls')),
    path('cliente/', include('app_outmed.urls')),
    path('listar_cliente/', include('app_outmed.urls')),
    path('fornecedor/', include('app_outmed.urls')),
    #path('funcionario/', include('app_outmed.urls')),
    path('admin/', admin.site.urls),
]

admin.site.site_header = "OUTMED Admin"
admin.site.site_title = "OUTMED Admin Portal"
admin.site.index_title = "Bem vindo a área de cadastro da OutMed"