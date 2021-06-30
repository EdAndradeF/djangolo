from django.contrib.auth.models import User
from django.db import models
from base.models import Item, NamedModel



class Lista(NamedModel):
    user = models.ForeignKey(
        User,
        null=False,
        on_delete=models.CASCADE,
    )

class ListaItem(models.Model):
    lista = models.ForeignKey(
        Lista,
        related_name='itens_lista',
        null=False,
        on_delete=models.CASCADE,
    )
    item = models.ForeignKey(
        Item,
        related_name='listas_item',
        null=False,
        on_delete=models.CASCADE,
    )
    quantidade = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.pk} {self.item_id} {self.lista_id}'


