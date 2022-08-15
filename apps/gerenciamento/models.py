from django.db import models

from apps.escritorio.models import Escritorio

from django.utils import timezone


class ChaveAcesso(models.Model):
    chaveId = models.AutoField('chaveId', primary_key=True, auto_created=True)
    escritorioId = models.ForeignKey(Escritorio, on_delete=models.CASCADE, related_name='Escritorio')
    advogadoId = models.IntegerField(name='advogadoId', null=True, blank=True)
    dataUltAlt = models.DateTimeField('dataUltAlt', default=timezone.now, null=False)
    dataAquisicao = models.DateTimeField('dataAquisicao', default=timezone.now, null=False)

    def __str__(self):
        return f'{self.chaveId} - {self.escritorioId.get_nomeFantasia()}'

    class Meta:
        db_table = "ChaveAcesso"

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
