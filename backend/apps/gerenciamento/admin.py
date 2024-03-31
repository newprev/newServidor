from django.contrib import admin
from apps.gerenciamento.models import ChaveAcesso, Planos

from apps.advogado.models import Advogado


class AdminChaveAcesso(admin.ModelAdmin):
    list_display = ['chaveId', '_escritorio', '_advogado']
    exclude = ['dataCadastro']

    def _escritorio(self, instFK):
        return f'{instFK.escritorioId.get_nomeFantasia()}'

    def _advogado(self, inst):
        try:
            advogado: Advogado = Advogado.objects.get(advogadoId=inst.advogadoId)
            return advogado.primeiroNome
        except Exception as err:
            print(f"_advogado, {err=}")
            return '---'

class AdminPlanos(admin.ModelAdmin):
    list_display = ['planoId', 'titulo', 'valor', 'dataInicio', 'dataValidade']


admin.site.register(ChaveAcesso, AdminChaveAcesso)
admin.site.register(Planos, AdminPlanos)
