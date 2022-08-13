# Generated by Django 4.0.6 on 2022-08-13 01:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EspecieBeneficio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especieId', models.IntegerField(unique=True)),
                ('descricao', models.TextField(max_length=600)),
                ('ativo', models.BooleanField(default=True)),
                ('dataUltAlt', models.DateTimeField(default=datetime.datetime(2022, 8, 12, 22, 59, 6, 194333))),
                ('dataCadastro', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'EspecieBeneficio',
            },
        ),
        migrations.CreateModel(
            name='ExpectativaSobrevida',
            fields=[
                ('infoId', models.AutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('dataReferente', models.DateField()),
                ('idade', models.FloatField(help_text='Idade do cliente')),
                ('genero', models.CharField(help_text='genero', max_length=1)),
                ('expectativaSobrevida', models.FloatField(help_text='Expectativa de vida de homens e mulheres no Brasil')),
                ('dataUltAlt', models.DateTimeField(default=datetime.datetime(2022, 8, 12, 22, 59, 6, 192207))),
                ('dataCadastro', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'ExpSobrevida',
            },
        ),
        migrations.CreateModel(
            name='Indicadores',
            fields=[
                ('indicadorId', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('resumo', models.CharField(max_length=300)),
                ('descricao', models.TextField(max_length=2000)),
                ('fonte', models.CharField(max_length=300)),
                ('dataUltAlt', models.DateTimeField(default=datetime.datetime(2022, 8, 12, 22, 59, 6, 191827))),
                ('dataCadastro', models.DateTimeField(default=datetime.datetime(2022, 8, 12, 22, 59, 6, 191844))),
            ],
            options={
                'db_table': 'Indicadores',
            },
        ),
        migrations.CreateModel(
            name='IndicesAtualizacaoMonetaria',
            fields=[
                ('indiceId', models.AutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('dataReferente', models.DateField()),
                ('dib', models.DateField()),
                ('fator', models.FloatField()),
                ('dataUltAlt', models.DateTimeField(default=datetime.datetime(2022, 8, 12, 22, 59, 6, 192585))),
                ('dataCadastro', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'IndiceAtuMonetaria',
            },
        ),
        migrations.CreateModel(
            name='IpcaMensal',
            fields=[
                ('ipcaId', models.AutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('dataReferente', models.DateField()),
                ('valor', models.FloatField()),
                ('dataUltAlt', models.DateTimeField(default=datetime.datetime(2022, 8, 12, 22, 59, 6, 193493))),
                ('dataCadastro', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Ipca',
            },
        ),
        migrations.CreateModel(
            name='SalarioMinimo',
            fields=[
                ('SalarioId', models.AutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('vigencia', models.DateField()),
                ('baseLegal', models.CharField(blank=True, max_length=50)),
                ('valor', models.FloatField()),
                ('dataUltAlt', models.DateTimeField(default=datetime.datetime(2022, 8, 12, 22, 59, 6, 193106))),
                ('dataCadastro', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'SalarioMinimo',
            },
        ),
        migrations.CreateModel(
            name='TipoBeneficio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoId', models.IntegerField(auto_created=True, unique=True)),
                ('nome', models.CharField(max_length=20)),
                ('descricao', models.TextField(max_length=600)),
                ('ativo', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'TipoBeneficio',
            },
        ),
    ]
