# Generated by Django 4.0.6 on 2022-08-21 01:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('informacoes', '0003_alter_especiebeneficio_dataultalt_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='especiebeneficio',
            name='dataUltAlt',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 20, 22, 48, 9, 608004)),
        ),
        migrations.AlterField(
            model_name='expectativasobrevida',
            name='dataUltAlt',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 20, 22, 48, 9, 606234)),
        ),
        migrations.AlterField(
            model_name='indicadores',
            name='dataCadastro',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 20, 22, 48, 9, 605792)),
        ),
        migrations.AlterField(
            model_name='indicadores',
            name='dataUltAlt',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 20, 22, 48, 9, 605767)),
        ),
        migrations.AlterField(
            model_name='indicesatualizacaomonetaria',
            name='dataUltAlt',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 20, 22, 48, 9, 606596)),
        ),
        migrations.AlterField(
            model_name='ipcamensal',
            name='dataUltAlt',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 20, 22, 48, 9, 607343)),
        ),
        migrations.AlterField(
            model_name='salariominimo',
            name='dataUltAlt',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 20, 22, 48, 9, 606984)),
        ),
    ]