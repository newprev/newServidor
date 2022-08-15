from django.urls import path

from .viewPages import avaliaCadastroAdvogado


urlpatterns = [
    path('avaliaCadAdvogado', avaliaCadastroAdvogado, name='avaliaCadAdvogado'),
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
