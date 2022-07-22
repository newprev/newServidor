from rest_framework import serializers
from .models import ConvMon, TetosPrev, CarenciasLei91


class ConvMonSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConvMon
        exclude = ['convMonId', 'dataUltAlt', 'dataCadastro']


class TetosPrevSerializer(serializers.ModelSerializer):
    class Meta:
        model = TetosPrev
        exclude = ['dataUltAlt', 'dataCadastro']


class CarenciaLei91Serializer(serializers.ModelSerializer):
    class Meta:
        model = CarenciasLei91
        exclude = ['dataUltAlt', 'dataCadastro']
