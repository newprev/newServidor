from rest_framework import serializers
from apps.sincron.models import SyncIpca


class SyncSerializer(serializers.ModelSerializer):
    class Meta:
        model = SyncIpca
        fields = ['syncId', 'dataSync', 'qtdSync']
