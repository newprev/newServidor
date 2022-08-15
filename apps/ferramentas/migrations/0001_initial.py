# Generated by Django 4.0.6 on 2022-08-14 21:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarenciasLei91',
            fields=[
                ('carenciaId', models.AutoField(primary_key=True, serialize=False)),
                ('dataImplemento', models.DateField()),
                ('tempoContribuicao', models.IntegerField()),
                ('dataUltAlt', models.DateTimeField(default=datetime.datetime(2022, 8, 14, 18, 57, 1, 481500))),
                ('dataCadastro', models.DateTimeField(default=datetime.datetime(2022, 8, 14, 18, 57, 1, 481517))),
            ],
            options={
                'db_table': 'CarenciasLei91',
            },
        ),
        migrations.CreateModel(
            name='ConvMon',
            fields=[
                ('convMonId', models.AutoField(primary_key=True, serialize=False)),
                ('nomeMoeda', models.CharField(max_length=20)),
                ('fator', models.BigIntegerField()),
                ('dataInicial', models.DateField()),
                ('dataFinal', models.DateField(blank=True, null=True)),
                ('conversao', models.CharField(choices=[('V', 'Valorizou'), ('D', 'Desvalorizou')], default='V', max_length=1)),
                ('moedaCorrente', models.BooleanField(default=False)),
                ('sinal', models.CharField(max_length=10)),
                ('dataUltAlt', models.DateTimeField(default=datetime.datetime(2022, 8, 14, 18, 57, 1, 480784))),
                ('dataCadastro', models.DateTimeField(default=datetime.datetime(2022, 8, 14, 18, 57, 1, 480799))),
            ],
            options={
                'db_table': 'ConvMon',
            },
        ),
        migrations.CreateModel(
            name='TetosPrev',
            fields=[
                ('tetosPrevId', models.AutoField(primary_key=True, serialize=False)),
                ('dataValidade', models.DateField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=19)),
                ('dataUltAlt', models.DateTimeField(default=datetime.datetime(2022, 8, 14, 18, 57, 1, 481169))),
                ('dataCadastro', models.DateTimeField(default=datetime.datetime(2022, 8, 14, 18, 57, 1, 481187))),
            ],
            options={
                'db_table': 'TetosPrev',
            },
        ),
    ]
