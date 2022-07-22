from datetime import datetime
from django.db import models
from utils.helpers import getEstados
from django.contrib.auth.models import AbstractUser


class Escritorio(AbstractUser):
    ESTADO = getEstados()

    escritorioId = models.AutoField(primary_key=True, auto_created=True)
    nomeFantasia = models.CharField(max_length=50, blank=True)
    senha = models.CharField(max_length=80, blank=False, null=False, editable=False)
    cnpj = models.CharField(max_length=14, blank=True, null=True, unique=True)
    telefone = models.CharField(max_length=11, blank=True, null=True, unique=True)
    email = models.EmailField(max_length=60, null=False, blank=False, unique=True)
    inscEstadual = models.CharField(max_length=9, blank=True, null=True, unique=True)
    endereco = models.CharField(max_length=80, blank=True)
    numero = models.IntegerField(null=True, blank=True)
    cep = models.CharField(max_length=8, blank=True)
    complemento = models.CharField(max_length=50, blank=True)
    cidade = models.CharField(max_length=30, blank=True)
    estado = models.CharField(max_length=2, choices=ESTADO, null=False, default='SP', blank=True)
    bairro = models.CharField(max_length=50, blank=True)
    ativo = models.BooleanField(default=True)
    qtdChaves = models.IntegerField(default=0)
    dataUltAlt = models.DateTimeField(default=datetime.now(), null=False)
    dataCadastro = models.DateTimeField(default=datetime.now(), null=False)

    def get_nomeFantasia(self):
        return self.nomeFantasia

    class Meta:
        db_table = "Escritorio"

    def __str__(self):
        return self.username

    def retEmail(self):
        return self.email
