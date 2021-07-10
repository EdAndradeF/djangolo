from django.shortcuts import render
from rest_framework.decorators import api_view

from base.models import Item, Marca, Loja
from list.models import Lista, ListaItem



@api_view()
def index(request):
    itens = Item.objects.all()
    marcas = Marca.objects.all().values('nome', 'id')

    return render(request, 'index.html', {'itens': itens, 'marcas': marcas})


@api_view()
def criar_item(request):
    itens = Item.objects.all()
    marcas = Marca.objects.all().values('nome', 'id')

    return render(request, 'criar_item.html', {'itens': itens, 'marcas': marcas})


@api_view()
def criar_lista(request):
    lista = Lista.objects.all()
    listaitem = ListaItem.objects.all()

    return render(request, 'criar_lista.html', {'lista': lista, 'itens_lista': listaitem})


@api_view()
def criar_marca(request):
    marcas = Marca.objects.all()

    return render(request, 'criar_marca.html', {'marca': marcas})


@api_view()
def cad_loja(request):
    loja = Loja.objects.all()
    return render(request, 'criar_loja.html', {'loja': loja})
