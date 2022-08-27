from django.utils import timezone
from apps.escritorio.models import Escritorio
from django.db import models


class Advogado(models.Model):

    advogadoId = models.AutoField(primary_key=True, auto_created=True)
    escritorioId = models.ForeignKey(Escritorio, on_delete=models.CASCADE)
    primeiroNome = models.CharField(max_length=20, null=False, blank=False)
    sobrenome = models.CharField(max_length=40, null=False, blank=False)
    email = models.EmailField(max_length=40, null=False, blank=False, unique=True)
    senha = models.CharField(max_length=30, null=False, blank=False)
    oab = models.CharField(max_length=9, null=False, blank=False, unique=True)
    cpf = models.CharField(max_length=11, null=False, blank=False, unique=True)
    nacionalidade = models.CharField(max_length=40, default='brasileiro', null=False, blank=False)
    estadoCivil = models.CharField(max_length=20, default='solteiro', null=False, blank=False)
    admin = models.BooleanField(default=False)
    ativo = models.BooleanField(default=True)
    confirmado = models.BooleanField(default=False)
    fotoPath = models.ImageField(upload_to='foto/%Y/%m', blank=True)
    dataUltAlt = models.DateTimeField(default=timezone.now, null=False)
    dataCadastro = models.DateTimeField(default=timezone.now, null=False)

    class Meta:
        db_table = "Advogados"

    def __str__(self):
        return f"id: {self.advogadoId}, nome: {self.primeiroNome}, email: {self.email}, OAB: {self.oab}"

    def toDict(self, enviaEscritorio: bool = True):
        return {
            "advogadoId": self.advogadoId,
            "escritorioId": self.escritorioId.toDict() if enviaEscritorio else self.escritorioId.escritorioId,
            "primeiroNome": self.primeiroNome,
            "sobrenome": self.sobrenome,
            "email": self.email,
            "senha": self.senha,
            "oab": self.oab,
            "cpf": self.cpf,
            "nacionalidade": self.nacionalidade,
            "estadoCivil": self.estadoCivil,
            "admin": self.admin,
            "ativo": self.ativo,
            "confirmado": self.confirmado,
            "fotoPath": self.fotoPath,
            "dataUltAlt": self.dataUltAlt,
            "dataCadastro": self.dataCadastro
        }


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


class EnderecoAdvogado(models.Model):
    enderecoId = models.AutoField(name='enderecoId', primary_key=True, auto_created=True)
    advogadoId = models.ForeignKey(Advogado, on_delete=models.CASCADE)
    endereco = models.CharField(name='endereco', blank=False, null=False, max_length=60)
    cidade = models.CharField(name='cidade', blank=False, null=False, max_length=60)
    estado = models.CharField(name='estado', blank=False, null=False, max_length=60)
    bairro = models.CharField(name='bairro', blank=False, null=False, max_length=60)
    cep = models.IntegerField(name='cep', blank=False, null=False)
    numero = models.CharField(name='numero', blank=False, null=False, max_length=60)
    complemento = models.CharField(name='complemento', blank=False, null=False, max_length=60)
    dataUltAlt = models.DateTimeField(default=timezone.now, null=False)
    dataCadastro = models.DateTimeField(default=timezone.now, null=False)

    class Meta:
        db_table = "EnderecoAdvogado"

    def toDict(self):
        return {
            "enderecoId": self.enderecoId,
            "advogadoId": self.advogadoId,
            "endereco": self.endereco,
            "cidade": self.cidade,
            "estado": self.estado,
            "bairro": self.bairro,
            "cep": self.cep,
            "numero": self.numero,
            "complemento": self.complemento,
            "dataUltAlt": self.dataUltAlt,
            "dataCadastro": self.dataCadastro
        }


class Contato(models.Model):
    Id = models.AutoField(name='Id', primary_key=True, auto_created=True)
    contatoId = models.IntegerField(name='contatoId', null=False, blank=False)
    telefone = models.IntegerField(name='telefone', null=True, blank=True)
    isWhatsapp = models.BooleanField(name='isWhatsapp', default=True)
    isTelegram = models.BooleanField(name='isTelegram', default=True)
    ativo = models.BooleanField(name='ativo', default=True)
    dataUltAlt = models.DateTimeField('dataUltAlt', default=timezone.now, null=False)
    dataCadastro = models.DateTimeField('dataCadastro', default=timezone.now, null=False)

    class Meta:
        db_table = "Contato"