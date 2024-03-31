from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views.viewsPages import *

# app_name = 'escritorio'

urlpatterns = [
    path('login/', login, name='login'),
    path('cadastro/', cadastro, name='cadastro'),
    path('esqSenha/', esqSenha, name='esqSenha'),
    path('dashboard/', dashboard, name='dashboard'),
    path('home/', home, name='home'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
