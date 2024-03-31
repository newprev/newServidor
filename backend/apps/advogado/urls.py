from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from apps.advogado.viewPages import *

# app_name = 'advogado'

urlpatterns = [
    path('cadastroAdvogado/', cadastroAdvogado, name='cadastroAdvogado'),
    path('atualizaCadastro/<int:advogadoId>/', atualizaCadastro, name='atualizaCadastro'),
    path('efetivaAtualizaCadastro/', efetivaAtualizaCadastro, name='efetivaAtualizaCadastro'),
    path('excluiAdvogado/<int:advogadoId>/', excluiAdvogado, name='excluiAdvogado'),
    path('desAtivaAdvogado/<int:advogadoId>/', desAtivaAdvogado, name='desAtivaAdvogado'),
    path('buscaAdvogados', buscaAdvogados, name='buscaAdvogados'),
    path('advogadosCadastrados', advogadosCadastrados, name='advogadosCadastrados'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
