from django.contrib import admin
from .models import ConvMon, TetosPrev, CarenciasLei91


class AdminConvMon(admin.ModelAdmin):
    list_display = ['convMonId', 'nomeMoeda', ]
    list_display_links = ['convMonId', 'nomeMoeda', ]
    search_fields = ['dataInicial', 'dataFinal']

admin.site.register(ConvMon, AdminConvMon)


class AdminTetosPrev(admin.ModelAdmin):
    list_display = ['tetosPrevId', 'dataValidade', 'valor']
    list_display_links = ['tetosPrevId', 'dataValidade', 'valor']
    search_fields = ['dataValidade', 'valor']
    list_per_page = 20

admin.site.register(TetosPrev, AdminTetosPrev)


class AdminCarenciasLei91(admin.ModelAdmin):
    list_display = ['carenciaId', 'dataImplemento', 'tempoContribuicao']
    list_display_links = ['carenciaId', 'dataImplemento', 'tempoContribuicao']
    search_fields = ['dataImplemento', 'tempoContribuicao']
    list_per_page = 20

admin.site.register(CarenciasLei91, AdminCarenciasLei91)