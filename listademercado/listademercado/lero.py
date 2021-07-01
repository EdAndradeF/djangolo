from django.shortcuts import render
from rest_framework.decorators import api_view

from base.models import Item, Marca


@api_view()
def index(request):
    itens = Item.objects.all()
    marcas = Marca.objects.all().values('nome', 'id')

    return render(request, 'index.html', {'itens': itens, 'marcas': marcas})
