from rest_framework import serializers
from .models import Escritorio
from utils.validators import *


class EscritoriosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Escritorio
        exclude = [
            'password', 'last_login',
            'is_superuser', 'username',
            'first_name', 'last_name', 
            'is_staff', 'is_active',
            'date_joined', 'groups',
            'user_permissions', 'ativo',
            'dataUltAlt', 'dataCadastro'
        ]

    def validate(self, data):
        if not validaCNPJ(data['cnpj']):
            raise serializers.ValidationError({"cnpj": "O CNPJ inválido"})

        return data
