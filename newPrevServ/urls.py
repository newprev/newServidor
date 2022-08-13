from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from apps.advogado.viewsSerializer import *
from apps.escritorio.views.viewSerializer import EscritorioViewSet
from apps.ferramentas.views import ConvMonViewSet, TetosPrevViewSet, CarenciasLei91ViewSet
from apps.informacoes.views import IndicadoresViewSet, ExpectativaSobrevidaViewSet, IndicesAtuMonetariaViewSet, SalarioMinimoViewSet, IpcaMensalViewSet, TipoBeneficioViewSet, \
    EspecieBeneficioViewSet
from apps.sincron.views import SyncIpcaViewSet

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="NewPrev - Servidor",
      default_version='0.0.11',
      description="API Rest para consumo do programa Desktop NewPrev Cliente",
      terms_of_service="#",
      contact=openapi.Contact(email="newprev.projeto@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


rotas = routers.DefaultRouter()
rotas.register('advogados', AdvogadosViewSet, basename='Advogados')
rotas.register('escritorio', EscritorioViewSet, basename='Escritorio')
rotas.register('convMon', ConvMonViewSet, basename='ConversaoMonetaria')
rotas.register('tetosPrev', TetosPrevViewSet, basename='TetosPrevidenciarios')
rotas.register('indicadores', IndicadoresViewSet, basename='Indicadores')
rotas.register('expSobrevida', ExpectativaSobrevidaViewSet, basename='Expectativa sobrevida')
rotas.register('indiceAtuMonetaria', IndicesAtuMonetariaViewSet, basename='Índices de atualização monetária')
rotas.register('carenciasLei91', CarenciasLei91ViewSet, basename='Carências da lei 821391')
rotas.register('salarioMinimo', SalarioMinimoViewSet, basename='Salários mínimos')
rotas.register('ipcaMensal', IpcaMensalViewSet, basename='IPCAs mensais')
rotas.register('tipoBeneficio', TipoBeneficioViewSet, basename='Tipos de benefício')
rotas.register('especieBeneficio', EspecieBeneficioViewSet, basename='EspecieBeneficios')
rotas.register('syncIpca', SyncIpcaViewSet, basename='Sync IPCAs')

urlpatterns = [
    path('escritorio/', include('apps.escritorio.urls')),
    path('authEscritorio/', include('apps.escritorio.authUrls')),
    path('authAdvogado/', include('apps.advogado.authUrls')),
    path('advogado/', include('apps.advogado.urls')),
    path('admin/', admin.site.urls),
    path('explorer/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/', include(rotas.urls)),
    path('api/escritorio/<int:pk>/advogado', ListaAdvogadosByEscritorio.as_view()),
    path('api/advogados/<int:pk>/confirmacao/', AdvogadosConfirmacaoViewSet.as_view()),
    path('api/advogados/auth/login/', AuthAdvogado.as_view()),
    path('api/advogados/auth/trocaSenha/', TrocaSenhaViewSet.as_view()),
    path('api/advogados/auth/autenticaCodAcesso/', AutenticaPrimeiroAcesso.as_view()),
]
