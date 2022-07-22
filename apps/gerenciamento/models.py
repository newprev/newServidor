from django.db import models
from apps.escritorio.models import Escritorio
from django.utils import timezone


class ChaveAcesso(models.Model):
    chaveId = models.AutoField('chaveId', primary_key=True, auto_created=True)
    escritorioId = models.ForeignKey(Escritorio, on_delete=models.CASCADE, related_name='Escritorio')
    qtdChaves = models.PositiveSmallIntegerField('qtdChaves', null=False)
    dataUltAlt = models.DateTimeField('dataUltAlt', default=timezone.now, null=False)
    dataCadastro = models.DateTimeField('dataCadastro', default=timezone.now, null=False)

    def __str__(self):
        return f'{self.chaveId} - {self.escritorioId.get_nomeFantasia()}'

    class Meta:
        db_table = "ChaveAcesso"
