from datetime import datetime
from django.db import models
from utils.helpers import getEstados
from django.contrib.auth.models import AbstractUser
from utils.validators import validaCNPJ, validaEmail, validaApenasNumero


class Escritorio(AbstractUser):
    ESTADO = getEstados()

    escritorioId = models.AutoField(primary_key=True, auto_created=True)
    nomeFantasia = models.CharField(max_length=50, blank=True)
    cnpj = models.CharField(max_length=14, blank=True, null=True, unique=True, validators=[validaApenasNumero, validaCNPJ])
    telefone = models.CharField(max_length=11, blank=True, null=True, unique=True)
    email = models.EmailField(max_length=60, null=False, blank=False, unique=True, validators=[validaEmail])
    inscEstadual = models.CharField(max_length=9, blank=True, null=True, unique=True)
    endereco = models.CharField(max_length=80, blank=True)
    numero = models.IntegerField(null=True, blank=True, validators=[validaApenasNumero])
    cep = models.CharField(max_length=8, blank=True, validators=[validaApenasNumero])
    complemento = models.CharField(max_length=50, blank=True)
    cidade = models.CharField(max_length=30, blank=True)
    estado = models.CharField(max_length=2, choices=ESTADO, null=False, default='SP', blank=True)
    bairro = models.CharField(max_length=50, blank=True)
    ativo = models.BooleanField(default=True)
    qtdChaves = models.IntegerField(default=0, validators=[validaApenasNumero])
    dataUltAlt = models.DateTimeField(default=datetime.now(), null=False)
    dataCadastro = models.DateTimeField(default=datetime.now(), null=False)

    class Meta:
        db_table = "Escritorio"

    def get_nomeFantasia(self):
        return self.nomeFantasia

    def __str__(self):
        return self.username

    def retEmail(self):
        return self.email
