from django.urls import path

from apps.escritorio.views.viewsPages import fazerLogin, avaliaCadastro, fazerLogout

urlpatterns = [
    path('fazerLogin', fazerLogin, name='fazerLogin'),
    path('avaliaCadastro', avaliaCadastro, name='avaliaCadastro'),
    path('fazerLogout', fazerLogout, name='fazerLogout'),
]