from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from apps.escritorio.views.viewsPages import fazerLogin, avaliaCadastro, fazerLogout

urlpatterns = [
    path('fazerLogin', fazerLogin, name='fazerLogin'),
    path('avaliaCadastro', avaliaCadastro, name='avaliaCadastro'),
    path('fazerLogout', fazerLogout, name='fazerLogout'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
