# Generated by Django 4.0.6 on 2022-08-28 21:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('informacoes', '0010_alter_especiebeneficio_dataultalt_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='especiebeneficio',
            name='dataUltAlt',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 28, 18, 45, 2, 82062)),
        ),
        migrations.AlterField(
            model_name='expectativasobrevida',
            name='dataUltAlt',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 28, 18, 45, 2, 80232)),
        ),
        migrations.AlterField(
            model_name='indicadores',
            name='dataCadastro',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 28, 18, 45, 2, 79748)),
        ),
        migrations.AlterField(
            model_name='indicadores',
            name='dataUltAlt',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 28, 18, 45, 2, 79730)),
        ),
        migrations.AlterField(
            model_name='indicesatualizacaomonetaria',
            name='dataUltAlt',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 28, 18, 45, 2, 80590)),
        ),
        migrations.AlterField(
            model_name='ipcamensal',
            name='dataUltAlt',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 28, 18, 45, 2, 81348)),
        ),
        migrations.AlterField(
            model_name='salariominimo',
            name='dataUltAlt',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 28, 18, 45, 2, 80980)),
        ),
    ]
