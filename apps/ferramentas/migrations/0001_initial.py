# Generated by Django 4.0.6 on 2022-08-21 01:33

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
                ('dataUltAlt', models.DateTimeField(default=datetime.datetime(2022, 8, 20, 22, 33, 43, 414471))),
                ('dataCadastro', models.DateTimeField(default=datetime.datetime(2022, 8, 20, 22, 33, 43, 414490))),
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
                ('dataUltAlt', models.DateTimeField(default=datetime.datetime(2022, 8, 20, 22, 33, 43, 413635))),
                ('dataCadastro', models.DateTimeField(default=datetime.datetime(2022, 8, 20, 22, 33, 43, 413655))),
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
                ('dataUltAlt', models.DateTimeField(default=datetime.datetime(2022, 8, 20, 22, 33, 43, 414083))),
                ('dataCadastro', models.DateTimeField(default=datetime.datetime(2022, 8, 20, 22, 33, 43, 414100))),
            ],
            options={
                'db_table': 'TetosPrev',
            },
        ),
    ]
