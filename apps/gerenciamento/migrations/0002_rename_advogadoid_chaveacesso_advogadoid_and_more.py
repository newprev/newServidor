# Generated by Django 4.0.6 on 2022-08-13 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gerenciamento', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chaveacesso',
            old_name='AdvogadoId',
            new_name='advogadoId',
        ),
        migrations.RemoveField(
            model_name='chaveacesso',
            name='qtdChaves',
        ),
    ]
