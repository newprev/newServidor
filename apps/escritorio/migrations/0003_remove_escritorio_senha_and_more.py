# Generated by Django 4.0.6 on 2022-07-31 00:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escritorio', '0002_alter_escritorio_cep_alter_escritorio_cnpj_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='escritorio',
            name='senha',
        ),
        migrations.AlterField(
            model_name='escritorio',
            name='dataCadastro',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 30, 21, 19, 38, 687005)),
        ),
        migrations.AlterField(
            model_name='escritorio',
            name='dataUltAlt',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 30, 21, 19, 38, 686987)),
        ),
    ]