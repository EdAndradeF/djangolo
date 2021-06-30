from rest_framework.serializers import ModelSerializer

from .models import Marca, Loja, Item


class ItemSerializer(ModelSerializer):

    class Meta:
        model = Item
        fields = (
            'nome',
            'marca',
            'medida',
            'id',
        )

    def create(self, validated_data):
        return super().create(validated_data)

class MarcaSerializer(ModelSerializer):

    class Meta:
        model = Marca
        fields = (
            'nome',
            'site',
            'nacionalidade',
            'localidade',
            'id',
        )

class LojaSerializer(ModelSerializer):

    class Meta:
        model = Loja
        fields = (
            'nome',
            'categoria',
            'site',
            'estado',
            'cidade',
            'rua',
            'num',
            'id',
        )
