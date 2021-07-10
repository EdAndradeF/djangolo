"""listademercado URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.views.static import serve

from . import settings
from .paginas import index, criar_item, criar_lista, criar_marca, cad_loja

urlpatterns = [
    path('', index),
    path('criar_item', criar_item),
    path('criar_lista', criar_lista),
    path('criar_marca', criar_marca),
    path('cad_loja', cad_loja),
    path('admin/', admin.site.urls),
    path('api/', include('base.urls')),
    path('user/', include('list.urls')),
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT})
]
