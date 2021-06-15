from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=12, null=False)
    idade = models.IntegerField()


class Aluno(Pessoa):
    nota = models.FloatField()
