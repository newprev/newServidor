# Generated by Django 4.0.6 on 2022-08-28 21:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advogado', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contato',
            name='contatoId',
        ),
        migrations.AddField(
            model_name='contato',
            name='advogadoId',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='advogado.advogado'),
            preserve_default=False,
        ),
    ]
