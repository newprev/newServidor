# Generated by Django 4.0.6 on 2022-08-26 05:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escritorio', '0006_alter_escritorio_datacadastro_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='escritorio',
            name='dataCadastro',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 26, 2, 16, 44, 825410)),
        ),
        migrations.AlterField(
            model_name='escritorio',
            name='dataUltAlt',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 26, 2, 16, 44, 825392)),
        ),
    ]
