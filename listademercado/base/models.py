from django.db import models


class NamedModel(models.Model):
    nome = models.CharField(
        null=False,
        blank=False,
        max_length=50,
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.nome


class Item(NamedModel):
    marca = models.ForeignKey(
        'Marca',
        null=True,
        on_delete=models.CASCADE,
        related_name='itens_da_marca'
    )

    medida_choices = [
        ('kg', 'Kilo',),
        ('g', 'Grama',),
        ('u', 'Unidade',),
        ('l', 'Litro',),
        ('ml', 'MiniLitro'),
    ]
    medida = models.CharField(
        max_length=3,
        choices=medida_choices,
        default='u'
    )



class Marca(NamedModel):
    site = models.URLField(null=True)
    nacionalidade = models.CharField(           #caso nacional com?
        max_length=4,                           #obrigatoriedade?
        null=True,                              #da localização?
    )
    localidade = models.CharField(
        max_length=45,
        null=True
    )

    def __str__(self):
        return self.nome


class Loja(NamedModel):
    categoria = models.CharField(max_length=15, null=True) #seletor com opçoes
    site = models.URLField(null=True)
    estado = models.CharField(max_length=2) #endereço com
    cidade = models.CharField(max_length=30)#possibilidade
    rua = models.CharField(max_length=60)   #busca por CEP
    num = models.IntegerField()

