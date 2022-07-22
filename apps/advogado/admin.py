from django.contrib import admin
from .models import Advogado, TrocaSenha
from django.contrib.auth.mixins import LoginRequiredMixin


@admin.register(Advogado)
class AdminAdvogado(admin.ModelAdmin, LoginRequiredMixin):
    list_display = ['advogadoId', 'nomeAdvogado', 'escritorioId', 'login', 'email', 'ativo', 'confirmado']
    list_display_links = ['advogadoId', 'escritorioId', 'login', 'email', 'nomeAdvogado']
    list_filter = ['escritorioId', ]
    list_editable = ['ativo', 'confirmado']
    readonly_fields = ['advogadoId', ]
    ordering = ['nomeAdvogado', ]
    list_per_page = 15

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        # form.base_fields["escritorioId"].label = "Escritorios:"
        return form

# admin.site.register(Advogado, AdminAdvogado)


@admin.register(TrocaSenha)
class AdminTrocaSenha(admin.ModelAdmin):
    list_display = ["acessoId", "advogadoId", "codAcesso", "tipoTroca", "dataUltAlt", "dataCadastro"]
    list_filter = ["dataCadastro", ]
    ordering = ["dataCadastro", ]
    list_per_page = 15

