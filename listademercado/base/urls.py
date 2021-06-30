from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter
from .views import MarcaViewSet, LojaViewSet, ItemViewSet

router = DefaultRouter()
router.register(r'item', ItemViewSet, basename='item')
router.register(r'marca', MarcaViewSet, basename='marca')
router.register(r'loja', LojaViewSet, basename='loja')
urlpatterns = [
    url(r'', include(router.urls))
]