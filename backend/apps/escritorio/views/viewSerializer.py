from rest_framework import viewsets, filters
from logging import info, error

from ..models import Escritorio
from ..serializers import EscritoriosSerializer
from django_filters.rest_framework import DjangoFilterBackend


class EscritorioViewSet(viewsets.ModelViewSet):
    """Exibindo todos advogados cadastrados"""
    try:
        info('GET::api/escritorio/')
        queryset = Escritorio.objects.all()
        serializer_class = EscritoriosSerializer
        filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
        ordering_fields = ['nomeEscritorio']
        search_fields = ['nomeEscritorio', 'cnpj']
        filterset_fields = ['ativo']
    except Exception as err:
        error('erro::api/escritorio/')
