from datetime import datetime

from django.db import models
from utils.helpers import getTipoAuth


class NewAuth(models.Model):
    TIPO_AUTH = getTipoAuth()

    idAuth = models.IntegerField(auto_created=True, primary_key=True, null=False, blank=False)
    tipoAuth = models.CharField(max_length=2, choices=TIPO_AUTH, null=False, default='E', blank=True)
    escritorioId = models.IntegerField(null=True, blank=True)
    advogadoId = models.IntegerField(null=True, blank=True)
    horaAuth = models.DateTimeField(default=datetime.now(), null=False)
    dataCadastro = models.DateTimeField(default=datetime.now(), null=False)

    class Meta:
        db_table = "NewAuth"
