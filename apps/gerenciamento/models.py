import datetime

from django.db import models

from apps.escritorio.models import Escritorio
from utils.helpers import frequenciaPlano

from django.utils import timezone


class Planos(models.Model):
    planoId = models.AutoField('planoId', primary_key=True, auto_created=True)
    titulo = models.CharField('titulo', max_length=50, null=False, blank=False)
    subtitulo = models.CharField('subtitulo', max_length=100, null=False, blank=False)
    valor = models.DecimalField('valor', decimal_places=2, max_digits=6, null=False, blank=False)
    melhorEscolha = models.BooleanField('melhorEscolha', default=False)
    freqCobranca = models.CharField('freqCobranca', max_length=2, choices=frequenciaPlano, default='ME')
    funcionalidades = models.TextField('funcionalidades', max_length=300, blank=False, null=False)
    ativo = models.BooleanField('ativo', default=True, null=False)
    icone = models.CharField('icone', null=True, max_length=30)
    dataInicio = models.DateTimeField('dataInicio')
    dataValidade = models.DateTimeField('dataValidade')
    dataUltAlt = models.DateTimeField('dataUltAlt')
    dataCadastro = models.DateTimeField('dataCadastro', default=datetime.datetime.now(), editable=False)

    def __str__(self):
        return f"{self.planoId}, {self.titulo}, {self.valor}, {self.dataInicio}, {self.dataValidade}"

    def toDict(self) -> dict:
        return {
            "planoId": self.planoId,
            "titulo": self.titulo,
            "subtitulo": self.subtitulo,
            "valor": self.valor,
            "melhorEscolha": self.melhorEscolha,
            "freqCobranca": self.freqCobranca,
            "funcionalidades": self.funcionalidades.split(';'),
            "ativo": self.ativo,
            "icone": self.icone,
            "dataInicio": self.dataInicio,
            "dataValidade": self.dataValidade,
            "dataUltAlt": self.dataUltAlt,
            "dataCadastro": self.dataCadastro,
        }

    class Meta:
        db_table = "Planos"


class ChaveAcesso(models.Model):
    chaveId = models.AutoField('chaveId', primary_key=True, auto_created=True)
    escritorioId = models.ForeignKey(Escritorio, on_delete=models.CASCADE, related_name='Escritorio')
    planoId = models.ForeignKey(Planos, on_delete=models.CASCADE, related_name='Planos')
    advogadoId = models.IntegerField(name='advogadoId', null=True, blank=True)
    ativo = models.BooleanField('ativo', default=True)
    dataUltAlt = models.DateTimeField('dataUltAlt', default=timezone.now, null=False)
    dataAquisicao = models.DateTimeField('dataAquisicao', default=timezone.now, null=False)

    def __str__(self):
        return f'{self.chaveId} - {self.escritorioId.get_nomeFantasia()}'

    def toDict(self):
        return {
            'chaveId': self.chaveId,
            'escritorioId': self.escritorioId,
            'planoId': self.planoId,
            'advogadoId': self.advogadoId,
            'ativo': self.ativo,
            'dataUltAlt': self.dataUltAlt,
            'dataAquisicao': self.dataAquisicao,
        }

    class Meta:
        db_table = "ChaveAcesso"
