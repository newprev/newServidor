# Generated by Django 5.0.3 on 2024-03-31 14:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gerenciamento', '0019_alter_planos_datacadastro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planos',
            name='dataCadastro',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 31, 11, 10, 58, 920474), editable=False, verbose_name='dataCadastro'),
        ),
    ]