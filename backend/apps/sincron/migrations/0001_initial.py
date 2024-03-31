# Generated by Django 5.0.3 on 2024-03-31 14:44

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SyncIpca',
            fields=[
                ('syncId', models.AutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('dataSync', models.DateTimeField(default=django.utils.timezone.now)),
                ('qtdSync', models.IntegerField()),
            ],
            options={
                'db_table': 'SyncIpca',
            },
        ),
    ]
