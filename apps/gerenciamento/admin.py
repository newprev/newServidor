from django.contrib import admin
from apps.gerenciamento.models import ChaveAcesso


class AdminChaveAcesso(admin.ModelAdmin):
    list_display = ['chaveId', '_escritorio']
    exclude = ['dataCadastro']

    def _escritorio(self, instFK):
        return f'{instFK.escritorioId.get_nomeFantasia()}'
        # return '5'


admin.site.register(ChaveAcesso, AdminChaveAcesso)
