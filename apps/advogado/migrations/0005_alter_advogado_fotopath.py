# Generated by Django 4.0.6 on 2022-08-15 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advogado', '0004_alter_advogado_fotopath'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advogado',
            name='fotoPath',
            field=models.ImageField(blank=True, upload_to='foto/%m/%Y'),
        ),
    ]
