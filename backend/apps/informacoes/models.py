from datetime import datetime
from django.db import models


class Indicadores(models.Model):
    # db_table = 'indicadores'

    indicadorId = models.CharField(max_length=20, primary_key=True)
    resumo = models.CharField(max_length=300, null=False, blank=False)
    descricao = models.TextField(max_length=2000, null=False, blank=False)
    fonte = models.CharField(max_length=300, null=False, blank=False)
    dataUltAlt = models.DateTimeField(default=datetime.now(), null=False)
    dataCadastro = models.DateTimeField(default=datetime.now(), null=False)

    class Meta:
        db_table = "Indicadores"

    def __str__(self):
        return f"indicadorId: {self.indicadorId}, resumo: {self.resumo}"


class ExpectativaSobrevida(models.Model):
    # db_table = 'expSobrevida'

    infoId = models.AutoField(primary_key=True, unique=True, blank=False, auto_created=True)
    dataReferente = models.DateField(blank=False, null=False)
    idade = models.FloatField(help_text='Idade do cliente')
    genero = models.CharField(help_text='genero', max_length=1, null=False, blank=False)
    expectativaSobrevida = models.FloatField(help_text='Expectativa de vida de homens e mulheres no Brasil')
    dataUltAlt = models.DateTimeField(default=datetime.now(), null=False)
    dataCadastro = models.DateTimeField(auto_now=True, null=False)

    class Meta:
        db_table = "ExpSobrevida"

    def __str__(self):
        return f"infoId: {self.infoId}, dataReferente: {self.dataReferente}, idade: {self.idade}"


class IndicesAtualizacaoMonetaria(models.Model):
    # db_table = 'indiceAtuMonetaria'

    indiceId = models.AutoField(primary_key=True, unique=True, blank=False, auto_created=True)
    dataReferente = models.DateField(blank=False, null=False)
    dib = models.DateField(blank=False, null=False)
    fator = models.FloatField(blank=False, null=False)
    dataUltAlt = models.DateTimeField(default=datetime.now(), null=False)
    dataCadastro = models.DateTimeField(auto_now=True, null=False)

    class Meta:
        db_table = "IndiceAtuMonetaria"

    def __str__(self):
        return f"indiceId: {self.indiceId}, dib: {self.dib} dataReferente: {self.dataReferente}, fator: {self.fator}"


class SalarioMinimo(models.Model):
    # db_table = 'SalarioMinimo'

    SalarioId = models.AutoField(primary_key=True, unique=True, blank=False, auto_created=True)
    vigencia = models.DateField(blank=False, null=False)
    baseLegal = models.CharField(max_length=50, blank=True)
    valor = models.FloatField(blank=False, null=False)
    dataUltAlt = models.DateTimeField(default=datetime.now(), null=False)
    dataCadastro = models.DateTimeField(auto_now=True, null=False)

    class Meta:
        db_table = "SalarioMinimo"

    def __str__(self):
        return f"SalarioId: {self.SalarioId}, vigencia: {self.vigencia} baseLegal: {self.baseLegal}, valor: {self.valor}"


class IpcaMensal(models.Model):
    ipcaId = models.AutoField(primary_key=True, unique=True, blank=False, auto_created=True)
    dataReferente = models.DateField(blank=False, null=False)
    valor = models.FloatField(blank=False, null=False)
    dataUltAlt = models.DateTimeField(default=datetime.now(), null=False)
    dataCadastro = models.DateTimeField(auto_now=True, null=False)

    class Meta:
        db_table = "Ipca"

    def __str__(self):
        return f"ipcaId: {self.ipcaId}, dataReferente: {self.dataReferente} valor: {self.valor}"


class TipoBeneficio(models.Model):
    tipoId = models.IntegerField(unique=True, blank=False, auto_created=True)
    nome = models.CharField(max_length=20, null=False, blank=False)
    descricao = models.TextField(max_length=600, null=False, blank=False)
    ativo = models.BooleanField(default=True)

    class Meta:
        db_table = "TipoBeneficio"

    def __str__(self):
        return f"tipoId: {self.tipoId}, nome: {self.nome}, ativo: {self.ativo}"


class EspecieBeneficio(models.Model):
    especieId = models.IntegerField(unique=True, blank=False, auto_created=False)
    descricao = models.TextField(max_length=600, null=False, blank=False)
    ativo = models.BooleanField(default=True)
    dataUltAlt = models.DateTimeField(default=datetime.now(), null=False)
    dataCadastro = models.DateTimeField(auto_now=True, null=False)

    class Meta:
        db_table = "EspecieBeneficio"

    def __str__(self):
        return f"especieId: {self.especieId}, descricao: {self.descricao}"
