# Generated by Django 4.0.6 on 2022-08-21 01:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('informacoes', '0002_alter_especiebeneficio_dataultalt_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='especiebeneficio',
            name='dataUltAlt',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 20, 22, 43, 22, 311967)),
        ),
        migrations.AlterField(
            model_name='expectativasobrevida',
            name='dataUltAlt',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 20, 22, 43, 22, 310249)),
        ),
        migrations.AlterField(
            model_name='indicadores',
            name='dataCadastro',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 20, 22, 43, 22, 309810)),
        ),
        migrations.AlterField(
            model_name='indicadores',
            name='dataUltAlt',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 20, 22, 43, 22, 309795)),
        ),
        migrations.AlterField(
            model_name='indicesatualizacaomonetaria',
            name='dataUltAlt',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 20, 22, 43, 22, 310608)),
        ),
        migrations.AlterField(
            model_name='ipcamensal',
            name='dataUltAlt',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 20, 22, 43, 22, 311306)),
        ),
        migrations.AlterField(
            model_name='salariominimo',
            name='dataUltAlt',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 20, 22, 43, 22, 310969)),
        ),
    ]
