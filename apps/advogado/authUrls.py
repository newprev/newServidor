from django.urls import path

from .viewPages import avaliaCadastroAdvogado

# app_name = 'advogado'

urlpatterns = [
    path('avaliaCadAdvogado', avaliaCadastroAdvogado, name='avaliaCadAdvogado'),
]
