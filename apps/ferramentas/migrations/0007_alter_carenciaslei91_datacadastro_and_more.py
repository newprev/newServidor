# Generated by Django 4.0.6 on 2022-08-15 05:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ferramentas', '0006_alter_carenciaslei91_datacadastro_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carenciaslei91',
            name='dataCadastro',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 15, 2, 39, 40, 725070)),
        ),
        migrations.AlterField(
            model_name='carenciaslei91',
            name='dataUltAlt',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 15, 2, 39, 40, 725053)),
        ),
        migrations.AlterField(
            model_name='convmon',
            name='dataCadastro',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 15, 2, 39, 40, 724343)),
        ),
        migrations.AlterField(
            model_name='convmon',
            name='dataUltAlt',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 15, 2, 39, 40, 724327)),
        ),
        migrations.AlterField(
            model_name='tetosprev',
            name='dataCadastro',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 15, 2, 39, 40, 724738)),
        ),
        migrations.AlterField(
            model_name='tetosprev',
            name='dataUltAlt',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 15, 2, 39, 40, 724724)),
        ),
    ]
