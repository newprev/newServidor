# Generated by Django 4.0.6 on 2022-07-22 04:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ferramentas', '0004_alter_carenciaslei91_datacadastro_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carenciaslei91',
            name='dataCadastro',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 22, 1, 44, 51, 651042)),
        ),
        migrations.AlterField(
            model_name='carenciaslei91',
            name='dataUltAlt',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 22, 1, 44, 51, 651028)),
        ),
        migrations.AlterField(
            model_name='convmon',
            name='dataCadastro',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 22, 1, 44, 51, 650244)),
        ),
        migrations.AlterField(
            model_name='convmon',
            name='dataUltAlt',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 22, 1, 44, 51, 650230)),
        ),
        migrations.AlterField(
            model_name='tetosprev',
            name='dataCadastro',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 22, 1, 44, 51, 650714)),
        ),
        migrations.AlterField(
            model_name='tetosprev',
            name='dataUltAlt',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 22, 1, 44, 51, 650700)),
        ),
    ]
