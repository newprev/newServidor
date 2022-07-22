from rest_framework import viewsets
from apps.sincron.models import SyncIpca
from apps.informacoes.models import IpcaMensal
from apps.sincron.serializers import SyncSerializer
import requests as http
from datetime import datetime

from logging import info, warning, error


class SyncIpcaViewSet(viewsets.ModelViewSet):
    """Sincroniza e exibe todas as sincronizações dos valores do IPCA mensal"""
    serializer_class = SyncSerializer

    def get_queryset(self):
        return SyncIpca.objects.all()

    def buscaIpcas(self):
        info("GET::/syncIpca")
        qtdSync: int = 0
        apiPath: str = 'https://servicodados.ibge.gov.br/api/v3/agregados/6691/periodos/201411|201412|201501|201502|201503|201504|201505|201506|201507|201508|201509|201510|201511|201512|201601|201602|201603|201604|201605|201606|201607|201608|201609|201610|201611|201612|201701|201702|201703|201704|201705|201706|201707|201708|201709|201710|201711|201712|201801|201802|201803|201804|201805|201806|201807|201808|201809|201810|201811|201812|201901|201902|201903|201904|201905|201906|201907|201908|201909|201910|201911|201912|202001|202002|202003|202004|202005|202006|202007|202008|202009|202010|202011|202012|202101|202102|202103|202104|202105|202106|202107|202108|202109/variaveis/63?localidades=N1[all]'
        try:
            jsonIndices: dict = http.get(apiPath).json()[0]['resultados'][0]['series'][0]['serie']
            for data, valor in jsonIndices.items():
                dataRecebida = datetime.strptime(data, '%Y%m').date()
                valorRecebido = float(valor)

                try:
                    IpcaMensal.objects.get(dataReferente=dataRecebida, valor=valorRecebido)
                except IpcaMensal.DoesNotExist:
                    indice = IpcaMensal.objects.create(
                        dataReferente=dataRecebida,
                        valor=valorRecebido,
                    )
                    info(f"INSERT::buscaIpcas - {indice.dataReferente=}")
                    indice.save()
                    qtdSync += 1
                except Exception as err:
                    warning(f"erro::/syncIpca - {err}")
                    print(f'erro({type(err)}): {err}')

        except Exception as err:
            error(f"erro::/syncIpca - {err}")
            print(f"buscaIpcas<SyncIpcaViewSet>: {err} - ({type(err)})")
        finally:
            sync = SyncIpca.objects.create(qtdSync=qtdSync)
            info(f"UPDATE::buscaIpcas - {sync.dataSync=}")
            sync.save()
