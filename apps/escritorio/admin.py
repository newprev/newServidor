from django.contrib import admin
from .models import Escritorio


class AdminEscritorio(admin.ModelAdmin):
    exclude = ['senha', 'first_name', 'last_name', 'username', 'password']

    list_display = ['escritorioId', 'nomeFantasia', 'cnpj', 'ativo']
    list_display_links = ['escritorioId', 'nomeFantasia', 'cnpj']
    list_per_page = 15
    readonly_fields = ['escritorioId', ]

    list_editable = ['ativo', ]


admin.site.register(Escritorio, AdminEscritorio)