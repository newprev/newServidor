# Generated by Django 5.0.3 on 2024-03-31 14:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escritorio', '0021_alter_escritorio_datacadastro_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='escritorio',
            name='dataCadastro',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 31, 11, 10, 56, 238800)),
        ),
        migrations.AlterField(
            model_name='escritorio',
            name='dataUltAlt',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 31, 11, 10, 56, 238784)),
        ),
    ]
