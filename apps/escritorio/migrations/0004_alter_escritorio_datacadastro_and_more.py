# Generated by Django 4.0.6 on 2022-08-21 01:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escritorio', '0003_alter_escritorio_datacadastro_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='escritorio',
            name='dataCadastro',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 20, 22, 48, 8, 163486)),
        ),
        migrations.AlterField(
            model_name='escritorio',
            name='dataUltAlt',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 20, 22, 48, 8, 163469)),
        ),
    ]
