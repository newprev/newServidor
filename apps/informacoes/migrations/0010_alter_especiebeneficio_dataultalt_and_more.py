# Generated by Django 4.0.6 on 2022-08-28 21:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('informacoes', '0009_alter_especiebeneficio_dataultalt_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='especiebeneficio',
            name='dataUltAlt',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 28, 18, 37, 56, 399974)),
        ),
        migrations.AlterField(
            model_name='expectativasobrevida',
            name='dataUltAlt',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 28, 18, 37, 56, 398229)),
        ),
        migrations.AlterField(
            model_name='indicadores',
            name='dataCadastro',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 28, 18, 37, 56, 397799)),
        ),
        migrations.AlterField(
            model_name='indicadores',
            name='dataUltAlt',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 28, 18, 37, 56, 397781)),
        ),
        migrations.AlterField(
            model_name='indicesatualizacaomonetaria',
            name='dataUltAlt',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 28, 18, 37, 56, 398586)),
        ),
        migrations.AlterField(
            model_name='ipcamensal',
            name='dataUltAlt',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 28, 18, 37, 56, 399327)),
        ),
        migrations.AlterField(
            model_name='salariominimo',
            name='dataUltAlt',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 28, 18, 37, 56, 398950)),
        ),
    ]
