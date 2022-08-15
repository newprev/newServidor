from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .viewPages import cadastroAdvogado, atualizaCadastro, efetivaAtualizaCadastro

# app_name = 'advogado'

urlpatterns = [
    path('cadastroAdvogado/', cadastroAdvogado, name='cadastroAdvogado'),
    path('atualizaCadastro/<int:advogadoId>', atualizaCadastro, name='atualizaCadastro'),
    path('efetivaAtualizaCadastro/', efetivaAtualizaCadastro, name='efetivaAtualizaCadastro'),
    # path('', pages.index, name='index'),
    # path('login', pages.login, name='login'),
    # path('id=<int:escritorioId>', pages.dashboard, name='dashboard'),
    # path('escritorio=<str:nomeEscritorio>', pages.dashboard, name='dashboard'),
    # path('logout', pages.logout, name='logout'),
    # path('novoAdv', pages.criaAdv, name='criaAdv'),
    # path('editaAdv/<int:advogadoId>/', pages.editaAdv, name='editaAdv'),
    # path('atualizaAdv', pages.atualizaAdv, name='atualizaAdv'),
    # path('deletaAdv/<int:advogadoId>/', pages.deletaAdv, name='deletaAdv'),
    # path('editaEscritorio/<str:nomeEscritorio>/', pages.editaEscritorio, name='editaEscritorio'),
    # path('atualizaEscritorio', pages.atualizaEscritorio, name='atualizaEscritorio')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
