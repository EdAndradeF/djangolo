from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from list.models import Lista, ListaItem
from list.serializers import ListaSerializer, ListaItemSerializer


class ListaViewSet(ModelViewSet):
    queryset = Lista.objects.all()
    serializer_class = ListaSerializer


class ListaItemViewSet(ModelViewSet):
    queryset = ListaItem.objects.all()
    serializer_class = ListaItemSerializer
    filterset_fields = ('lista',)
