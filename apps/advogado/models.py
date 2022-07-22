from django.utils import timezone
from apps.escritorio.models import Escritorio
from django.db import models


class Advogado(models.Model):

    advogadoId = models.AutoField(primary_key=True, auto_created=True)
    escritorioId = models.ForeignKey(Escritorio, on_delete=models.CASCADE)
    senha = models.CharField(max_length=30, null=False, blank=False)
    login = models.CharField(max_length=30, null=False, blank=False)
    email = models.EmailField(max_length=40, null=False, blank=False)
    numeroOAB = models.CharField(max_length=9, null=False, blank=False, unique=True)
    cpf = models.CharField(max_length=11, null=False, blank=False, unique=True)
    nomeAdvogado = models.CharField(max_length=20, null=False, blank=False)
    sobrenomeAdvogado = models.CharField(max_length=40, null=False, blank=False)
    nacionalidade = models.CharField(max_length=40, default='brasileiro', null=False, blank=False)
    estadoCivil = models.CharField(max_length=20, default='solteiro', null=False, blank=False)
    admin = models.BooleanField(default=False)
    ativo = models.BooleanField(default=True)
    confirmado = models.BooleanField(default=False)
    dataUltAlt = models.DateTimeField(default=timezone.now, null=False)
    dataCadastro = models.DateTimeField(default=timezone.now, null=False)

    class Meta:
        db_table = "Advogados"

    def __str__(self):
        return f"id: {self.advogadoId}, nome: {self.nomeAdvogado}, email: {self.email}, OAB: {self.numeroOAB}"


class TrocaSenha(models.Model):

    TIPO = (
        (1, 'PrimeiroAcesso'),
        (2, 'EsqueceuSenha')
    )

    acessoId = models.AutoField(primary_key=True, auto_created=True)
    advogadoId = models.ForeignKey(Advogado, on_delete=models.CASCADE)
    codAcesso = models.IntegerField(null=False, blank=False)
    primAcesso = models.BooleanField(null=False, default=True)
    verificado = models.BooleanField(null=False, blank=False, default=False)
    tipoTroca = models.IntegerField(choices=TIPO, default=1, null=False)
    dataUltAlt = models.DateTimeField(default=timezone.now, null=False)
    dataCadastro = models.DateTimeField(default=timezone.now, null=False)

    class Meta:
        db_table = "TrocaSenha"
