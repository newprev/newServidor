# Generated by Django 4.0.6 on 2022-08-21 01:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ferramentas', '0002_alter_carenciaslei91_datacadastro_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carenciaslei91',
            name='dataCadastro',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 20, 22, 43, 21, 596660)),
        ),
        migrations.AlterField(
            model_name='carenciaslei91',
            name='dataUltAlt',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 20, 22, 43, 21, 596642)),
        ),
        migrations.AlterField(
            model_name='convmon',
            name='dataCadastro',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 20, 22, 43, 21, 595912)),
        ),
        migrations.AlterField(
            model_name='convmon',
            name='dataUltAlt',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 20, 22, 43, 21, 595896)),
        ),
        migrations.AlterField(
            model_name='tetosprev',
            name='dataCadastro',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 20, 22, 43, 21, 596318)),
        ),
        migrations.AlterField(
            model_name='tetosprev',
            name='dataUltAlt',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 20, 22, 43, 21, 596303)),
        ),
    ]
