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
        objeto1 = value.all().values('item__nome', "pk")
        #objeto1 = ListaItemSerializer(value, many=True)
        return objeto1




class ListaSerializer(ModelSerializer):
    itens_lista = ListaItensListaField(read_only=True)

    class Meta:
        model = Lista
        fields = (
            'pk',
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
        #resposta = super().update(instance, validated_data)
        if not instance.nome == validated_data['nome']:
            instance.nome = validated_data['nome']

        querylist = {}
        for query in ListaItem.objects.filter(lista_id=instance.id):
            querylist[query.id] = query.item_id


        upitens = {}
        ret = []
        for item in self.initial_data['itens_lista']:
            if type(item) == dict:
                item = item['item__nome']
            _item = Item.objects.filter(nome=item).first()

            if _item is None:
                _item = Item.objects.create(nome=item)
                _item = ListaItem.objects.create(lista_id=instance.pk, item=_item)
                upitens[_item.id] = _item.item_id





            upitens[_item.item_id] = _item.item
            ret.append(_item)

        for idlista, iditem in querylist.items():
            if iditem not in upitens:
                idlista.delete()

        return ret

    def create(self, validated_data):
        #resposta = super().create(validated_data)

        lista = Lista.objects.create(
            nome=validated_data['nome'],
            user=validated_data['user'],
        )
        for item in self.initial_data['itens_lista']:
            #created, item_criado = Item.object.get_or_create(nome=item)
            _item = Item.objects.filter(nome=item).first()
            if _item is None:
                _item = Item.objects.create(nome=item)

            ListaItem.objects.create(lista=lista, item=_item)

        return lista #resposta
