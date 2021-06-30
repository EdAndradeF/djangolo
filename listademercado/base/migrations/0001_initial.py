# Generated by Django 3.2.4 on 2021-06-29 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Loja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('categoria', models.CharField(max_length=15, null=True)),
                ('site', models.URLField(null=True)),
                ('estado', models.CharField(max_length=2)),
                ('cidade', models.CharField(max_length=30)),
                ('rua', models.CharField(max_length=60)),
                ('num', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('site', models.URLField(null=True)),
                ('nacionalidade', models.CharField(max_length=4, null=True)),
                ('localidade', models.CharField(max_length=45, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('quantidade', models.IntegerField(default=1)),
                ('medida', models.CharField(choices=[('kg', 'Kilo'), ('g', 'Grama'), ('u', 'Unidade'), ('l', 'Litro'), ('ml', 'MiniLitro')], default='u', max_length=3)),
                ('preco', models.FloatField(null=True)),
                ('marca', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.marca')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
