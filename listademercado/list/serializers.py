from django.conf.locale import id
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from list.models import Lista, ListaItem
from base.models import Item


class ListaItemSerializer(ModelSerializer):
    class Meta:
        model = ListaItem
        fields = '__all__'



class ListaItensListaField(serializers.Field):
    def to_representation(self, value):
        objeto1 = value.all().values('item__nome', "id")
        #objeto1 = ListaItemSerializer(value, many=True)
        return objeto1




class ListaSerializer(ModelSerializer):
    itens_lista = ListaItensListaField(read_only=True)

    class Meta:
        model = Lista
        fields = (
            'id',
            'nome',
            'user',
            'itens_lista',
            #'quantidade',
            #'medida',
        )

    def validate(self, attrs):
        resposta = super().validate(attrs)
        return resposta

    def update(self, instance, validated_data):
        resposta = super().update(instance, validated_data)


        querylist = []
        for query in ListaItem.objects.filter(lista_id=instance.id):
            querylist.append(query.item.id)

        upitens = []
        for item in self.initial_data['itens_lista']:
            if type(item) == dict:
                item = item['item__nome']
            _item = Item.objects.filter(nome=item).first()

            if _item is None:
                _item = Item.objects.create(nome=item)

            upitens.append(_item.id)
            u = upitens.index(_item.id)
            if len(upitens) <= len(querylist):
                i = ListaItem.objects.get(id=querylist[u])
                i.delete()
                ListaItem.objects.create(lista_id=instance.pk, item=_item)
            else:
                _item = ListaItem.objects.create(lista_id=instance.pk, item=_item)

        if len(querylist) > len(upitens):
            for u in range(len(upitens), len(querylist)-1):
                i = ListaItem.objects.get(id=querylist[u])
                i.delete()
        return instance

    def create(self, validated_data):
        resposta = super().create(validated_data)

        # lista = Lista.objects.create(
        #     nome=validated_data['nome'],
        #     user=validated_data['user'],
        # )
        # for item in self.initial_data['itens_lista']:
        #     #created, item_criado = Item.object.get_or_create(nome=item)
        #     _item = Item.objects.filter(nome=item).first()
        #     if _item is None:
        #         _item = Item.objects.create(nome=item)
        #
        #     ListaItem.objects.create(lista=lista, item=_item)

        return resposta
