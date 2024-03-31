# Generated by Django 4.0.6 on 2022-08-26 05:16

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('gerenciamento', '0005_alter_chaveacesso_uuid_alter_planos_datacadastro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chaveacesso',
            name='uuid',
            field=models.CharField(default=uuid.uuid4, max_length=100, verbose_name='uuid'),
        ),
        migrations.AlterField(
            model_name='planos',
            name='dataCadastro',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 26, 2, 16, 48, 510503), editable=False, verbose_name='dataCadastro'),
        ),
    ]
