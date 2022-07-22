# Generated by Django 4.0.6 on 2022-07-22 04:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('informacoes', '0004_alter_especiebeneficio_dataultalt_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='especiebeneficio',
            name='dataUltAlt',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 22, 1, 44, 52, 99218)),
        ),
        migrations.AlterField(
            model_name='expectativasobrevida',
            name='dataUltAlt',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 22, 1, 44, 52, 97371)),
        ),
        migrations.AlterField(
            model_name='indicadores',
            name='dataCadastro',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 22, 1, 44, 52, 97009)),
        ),
        migrations.AlterField(
            model_name='indicadores',
            name='dataUltAlt',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 22, 1, 44, 52, 96993)),
        ),
        migrations.AlterField(
            model_name='indicesatualizacaomonetaria',
            name='dataUltAlt',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 22, 1, 44, 52, 97798)),
        ),
        migrations.AlterField(
            model_name='ipcamensal',
            name='dataUltAlt',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 22, 1, 44, 52, 98496)),
        ),
        migrations.AlterField(
            model_name='salariominimo',
            name='dataUltAlt',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 22, 1, 44, 52, 98162)),
        ),
    ]