# Generated by Django 4.0.6 on 2022-08-28 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advogado', '0002_remove_contato_contatoid_contato_advogadoid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='telefone',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
    ]
