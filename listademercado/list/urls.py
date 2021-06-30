from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter

from list.views import ListaViewSet, ListaItemViewSet

router = DefaultRouter()
router.register(r'lista', ListaViewSet, basename='lista')
router.register(r'listaitem', ListaItemViewSet, basename='listaitem')
urlpatterns = [
    url(r'', include(router.urls))
]
