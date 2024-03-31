from rest_framework import viewsets
from logging import error, info

from .serializers import ConvMonSerializer, TetosPrevSerializer, CarenciaLei91Serializer
from .models import ConvMon, TetosPrev, CarenciasLei91


class ConvMonViewSet(viewsets.ModelViewSet):
    """Exibe todas as correções monetárias cadastradas"""
    try:
        info("GET::/convMon")
        queryset = ConvMon.objects.all()
        serializer_class = ConvMonSerializer
    except Exception as err:
        error("/convMon")


class TetosPrevViewSet(viewsets.ModelViewSet):
    """Exibe todos os tetos previdenciários cadastrados"""
    try:
        info("GET::/tetosPrev")
        queryset = TetosPrev.objects.all()
        serializer_class = TetosPrevSerializer
    except Exception as err:
        error("/tetosPrev")


class CarenciasLei91ViewSet(viewsets.ModelViewSet):
    """Exibe todas as datas de implementação da alteração do tempo mínimo de contribuição
    para aposentadorias até o ano de 2011"""
    try:
        info("GET::/carenciasLei91")
        queryset = CarenciasLei91.objects.all()
        serializer_class = CarenciaLei91Serializer
    except Exception as err:
        error("/carenciasLei91")
