# Generated by Django 4.0.6 on 2022-08-28 21:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gerenciamento', '0008_alter_planos_datacadastro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planos',
            name='dataCadastro',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 28, 18, 37, 58, 671572), editable=False, verbose_name='dataCadastro'),
        ),
    ]