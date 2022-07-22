from rest_framework import viewsets
from logging import error, info

from .serializers import *
from .models import Indicadores, ExpectativaSobrevida, IndicesAtualizacaoMonetaria, SalarioMinimo, IpcaMensal, TipoBeneficio, EspecieBeneficio


class IndicadoresViewSet(viewsets.ModelViewSet):
    """Exibe todos os possíveis indicadores do CNIS"""
    try:
        info("GET::/indicadores")
        queryset = Indicadores.objects.all()
        serializer_class = IndicadoresSerializer
    except Exception as err:
        error("erro::/indicadores")


class ExpectativaSobrevidaViewSet(viewsets.ModelViewSet):
    """Exibe todas as informações do IBGE pertinentes ao programa"""
    try:
        info("GET::/expSobrevida")
        queryset = ExpectativaSobrevida.objects.all()
        serializer_class = ExpSobrevidaSerializer
    except Exception as err:
        error("erro::/expSobrevida")


class IndicesAtuMonetariaViewSet(viewsets.ModelViewSet):
    """Exibe todos os índices de atualização monetária para cálculo do benefício"""
    try:
        info("GET::/indiceAtuMonetaria")
        queryset = IndicesAtualizacaoMonetaria.objects.all()
        serializer_class = IndicesAtuMonetariaSerializer
    except Exception as err:
        error("erro::/indiceAtuMonetaria")


class SalarioMinimoViewSet(viewsets.ModelViewSet):
    """Exibe todos os salários mínimos (R$) no Brasil desde 1994"""
    try:
        info("GET::/salarioMinimo")
        queryset = SalarioMinimo.objects.all()
        serializer_class = SalarioMinimoSerializer
    except Exception as err:
        error("/salarioMinimo")


class IpcaMensalViewSet(viewsets.ModelViewSet):
    """Exibe todos os IPCAs mensais desde Janeiro de 2011"""
    try:
        info("GET::/ipcaMensal")
        queryset = IpcaMensal.objects.all()
        serializer_class = IpcaMensalSerializer
    except Exception as err:
        error("/ipcaMensal")


class TipoBeneficioViewSet(viewsets.ModelViewSet):
    """Exibe todos os tipo de benefícios possíveis de trabalhar no NewPrev"""
    try:
        info("GET::/tipoBeneficio")
        queryset = TipoBeneficio.objects.all()
        serializer_class = TipoBeneficioSerializer
    except Exception as err:
        error("/tipoBeneficio")


class EspecieBeneficioViewSet(viewsets.ModelViewSet):
    """Exibe todos as espécies de benefícios existentes no NewPrev"""
    try:
        info("GET::/especieBeneficio")
        queryset = EspecieBeneficio.objects.all()
        serializer_class = EspecieBeneficioSerializer
    except Exception as err:
        error("/especieBeneficio")
