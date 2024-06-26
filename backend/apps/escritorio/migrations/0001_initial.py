# Generated by Django 4.0.6 on 2022-08-21 01:33

import datetime
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone
import utils.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Escritorio',
            fields=[
                ('escritorioId', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('nomeFantasia', models.CharField(blank=True, max_length=50)),
                ('cnpj', models.CharField(blank=True, max_length=14, null=True, unique=True, validators=[utils.validators.validaApenasNumero, utils.validators.validaCNPJ])),
                ('telefone', models.CharField(blank=True, max_length=11, null=True, unique=True)),
                ('email', models.EmailField(max_length=60, unique=True, validators=[utils.validators.validaEmail])),
                ('inscEstadual', models.CharField(blank=True, max_length=9, null=True, unique=True)),
                ('endereco', models.CharField(blank=True, max_length=80)),
                ('numero', models.IntegerField(blank=True, null=True, validators=[utils.validators.validaApenasNumero])),
                ('cep', models.CharField(blank=True, max_length=8, validators=[utils.validators.validaApenasNumero])),
                ('complemento', models.CharField(blank=True, max_length=50)),
                ('cidade', models.CharField(blank=True, max_length=30)),
                ('estado', models.CharField(blank=True, choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], default='SP', max_length=2)),
                ('bairro', models.CharField(blank=True, max_length=50)),
                ('ativo', models.BooleanField(default=True)),
                ('logoPath', models.ImageField(blank=True, upload_to='logo/%Y/%m')),
                ('dataUltAlt', models.DateTimeField(default=datetime.datetime(2022, 8, 20, 22, 33, 42, 668137))),
                ('dataCadastro', models.DateTimeField(default=datetime.datetime(2022, 8, 20, 22, 33, 42, 668159))),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'Escritorio',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
