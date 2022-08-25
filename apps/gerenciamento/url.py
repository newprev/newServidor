from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import *

# app_name = 'gerenciamento'

urlpatterns = [
    path('addChaves/', addChaves, name='addChaves'),
    path('buscaPlanos/<int:mensal>', buscaPlanos, name='buscaPlanos'),
    path('avaliaAddChave/<int:planoId>', avaliaAddChave, name='avaliaAddChave'),
    path('minhasChaves', minhasChaves, name='minhasChaves'),
    path('buscaMinhasChaves', buscaMinhasChaves, name='buscaMinhasChaves'),
    path('buscaMinhasUltimasAquisicoes', buscaMinhasUltimasAquisicoes, name='buscaMinhasUltimasAquisicoes'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
