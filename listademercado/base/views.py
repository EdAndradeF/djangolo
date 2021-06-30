from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Marca, Loja, Item
from .serializers import MarcaSerializer, LojaSerializer, ItemSerializer


class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer


class LojaViewSet(ModelViewSet):
    queryset = Loja.objects.all()
    serializer_class = LojaSerializer