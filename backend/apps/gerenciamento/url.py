from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import *

# app_name = 'gerenciamento'

urlpatterns = [
    path('addChaves/', addChaves, name='addChaves'),
    path('buscaPlanos/', buscaPlanos, name='buscaPlanos'),
    path('avaliaAddChave/<int:planoId>/', avaliaAddChave, name='avaliaAddChave'),
    path('minhasChaves/', minhasChaves, name='minhasChaves'),
    path('buscaMinhasChaves/', buscaMinhasChaves, name='buscaMinhasChaves'),
    path('buscaMinhasUltimasAquisicoes/', buscaMinhasUltimasAquisicoes, name='buscaMinhasUltimasAquisicoes'),
    path('atualizaCarrinho/', atualizaCarrinho, name="atualizaCarrinho"),
    path('deletaChaveCarrinho/<str:uuid>/', deletaChaveCarrinho, name='deletaChaveCarrinho'),
    path('efetivaCompraPlanos/', efetivaCompraPlanos, name='efetivaCompraPlanos'),
    path('efetivaAssociacao', efetivaAssociacao, name='efetivaAssociacao')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
