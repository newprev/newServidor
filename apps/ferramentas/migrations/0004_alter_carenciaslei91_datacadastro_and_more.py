# Generated by Django 4.0.6 on 2022-08-21 01:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ferramentas', '0003_alter_carenciaslei91_datacadastro_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carenciaslei91',
            name='dataCadastro',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 20, 22, 48, 8, 890418)),
        ),
        migrations.AlterField(
            model_name='carenciaslei91',
            name='dataUltAlt',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 20, 22, 48, 8, 890400)),
        ),
        migrations.AlterField(
            model_name='convmon',
            name='dataCadastro',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 20, 22, 48, 8, 889693)),
        ),
        migrations.AlterField(
            model_name='convmon',
            name='dataUltAlt',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 20, 22, 48, 8, 889676)),
        ),
        migrations.AlterField(
            model_name='tetosprev',
            name='dataCadastro',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 20, 22, 48, 8, 890083)),
        ),
        migrations.AlterField(
            model_name='tetosprev',
            name='dataUltAlt',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 20, 22, 48, 8, 890069)),
        ),
    ]
