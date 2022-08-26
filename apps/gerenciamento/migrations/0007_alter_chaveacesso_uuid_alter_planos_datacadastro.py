# Generated by Django 4.0.6 on 2022-08-26 05:17

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('gerenciamento', '0006_alter_chaveacesso_uuid_alter_planos_datacadastro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chaveacesso',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, verbose_name='uuid'),
        ),
        migrations.AlterField(
            model_name='planos',
            name='dataCadastro',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 26, 2, 17, 50, 652308), editable=False, verbose_name='dataCadastro'),
        ),
    ]
