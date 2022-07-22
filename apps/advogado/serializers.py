from rest_framework import serializers
from .models import Advogado, TrocaSenha
from .validators import *


class AdvogadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advogado
        exclude = ['senha', 'dataUltAlt']

    def validate(self, data):
        if not validaCpf(data['cpf']):
            raise serializers.ValidationError({"cpf": "CPF inválido."})

        if not validaTamanhoNumOAB(data['numeroOAB']):
            raise serializers.ValidationError({"numeroOAB": "O número da OAB precisa ter 9 dígitos."})

        if not validaApenasNumerosOAB(data['numeroOAB']):
            raise serializers.ValidationError({"numeroOAB": "O número da OAB deve conter apenas números."})

        if not validanomeAdvogado(data['nomeAdvogado']):
            raise serializers.ValidationError({"nomeAdvogado": "O nome do advogado não deve conter números."})

        if not validaSobrenomeAdvogado(data['sobrenomeAdvogado']):
            raise serializers.ValidationError({"sobrenomeAdvogado": "O sobrenome do advogado não deve conter números."})

        return data


class ConfirmaAdvogadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advogado
        fields = ['senha', 'confirmado']


class AuthAdvogadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advogado
        fields = ['advogadoId', 'escritorioId', 'login', 'email', 'numeroOAB', 'confirmado']


class TrocaSenhaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrocaSenha
        exclude = []
