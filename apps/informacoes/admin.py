from django.contrib import admin
from .models import Indicadores, ExpectativaSobrevida, IndicesAtualizacaoMonetaria, SalarioMinimo, IpcaMensal, TipoBeneficio


class AdminIndicadores(admin.ModelAdmin):
    list_display = ['indicadorId', 'resumo', 'fonte']
    list_display_links = ['indicadorId', 'resumo']
    list_per_page = 15


class AdminExpSobrevida(admin.ModelAdmin):
    list_display = ['dataReferente', 'idade', 'genero', 'expectativaSobrevida']
    list_display_links = ['dataReferente', 'idade', 'genero', 'expectativaSobrevida']
    list_per_page = 10


class AdminIndicesAtuMonetaria(admin.ModelAdmin):
    list_display = ['dataReferente', 'dib', 'fator']
    list_display_links = ['dataReferente', 'dib', 'fator']
    list_per_page = 30


class AdminSalarioMinimo(admin.ModelAdmin):
    list_display = ['vigencia', 'baseLegal', 'valor']
    list_display_links = ['vigencia', 'baseLegal', 'valor']
    list_per_page = 30


class AdminIpcaMensal(admin.ModelAdmin):
    list_display = ['dataReferente', 'valor']
    list_display_links = ['dataReferente', 'valor']
    list_per_page = 30


class AdminTipoBeneficio(admin.ModelAdmin):
    list_display = ['tipoId', 'nome', 'ativo']
    list_display_links = ['tipoId', 'nome', 'ativo']
    list_per_page = 30


class AdminEspecieBeneficio(admin.ModelAdmin):
    list_display = ['especieId', 'descricao', 'ativo']
    list_display_links = ['especieId', 'descricao', 'ativo']
    list_per_page = 25


admin.site.register(Indicadores, AdminIndicadores)
admin.site.register(ExpectativaSobrevida, AdminExpSobrevida)
admin.site.register(IndicesAtualizacaoMonetaria, AdminIndicesAtuMonetaria)
admin.site.register(SalarioMinimo, AdminSalarioMinimo)
admin.site.register(IpcaMensal, AdminIpcaMensal)
admin.site.register(TipoBeneficio, AdminTipoBeneficio)
